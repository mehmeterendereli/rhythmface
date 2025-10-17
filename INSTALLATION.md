# RhythmFace Installation Guide

Complete installation instructions for RhythmFace.

## Prerequisites

Before installing RhythmFace, ensure you have:

- **Python 3.10 or higher**
  ```bash
  python --version
  # Should show Python 3.10.x or higher
  ```

- **Poetry** (Python dependency manager)
  ```bash
  pip install poetry
  # Or use official installer:
  # curl -sSL https://install.python-poetry.org | python3 -
  ```

- **Working microphone** connected to your system

- **Audio drivers** properly installed (ALSA on Linux, CoreAudio on macOS, WASAPI on Windows)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rhythmface.git
cd rhythmface
```

### 2. Install Dependencies

```bash
# Install all dependencies (including development tools)
poetry install --with dev

# Or install only runtime dependencies
poetry install
```

This will:
- Create a virtual environment
- Install all required packages
- Set up the `rhythmface` command

### 3. Install Pre-commit Hooks (Optional but Recommended)

If you plan to contribute or modify the code:

```bash
poetry run pre-commit install
```

This installs Git hooks that automatically:
- Format code with Black
- Sort imports with isort
- Lint with Ruff
- Type-check with mypy

### 4. Generate Placeholder Assets

RhythmFace needs character and mouth images:

```bash
poetry run python -m rhythmface.assets.generator
```

This creates:
- `rhythmface/assets/base.png` - Character silhouette
- `rhythmface/assets/mouth_closed.png` - Closed mouth
- `rhythmface/assets/mouth_A.png` - "Ah" vowel
- `rhythmface/assets/mouth_O.png` - "Oh" vowel
- `rhythmface/assets/mouth_E.png` - "Eh" vowel

### 5. Verify Installation

Run diagnostics to ensure everything works:

```bash
poetry run rhythmface diagnose
```

This will:
- List available audio input devices
- Test microphone capture
- Test rendering system
- Display FPS information

## Platform-Specific Notes

### Windows

- Make sure you have Visual C++ Redistributable installed (required for some audio libraries)
- Allow microphone access in Windows Privacy Settings
- If audio doesn't work, try running as Administrator

### macOS

- Grant microphone permissions when prompted
- You may need to install `portaudio`:
  ```bash
  brew install portaudio
  ```

### Linux

- Install system audio libraries:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-dev portaudio19-dev
  
  # Fedora
  sudo dnf install python3-devel portaudio-devel
  
  # Arch
  sudo pacman -S portaudio
  ```

- Ensure your user is in the `audio` group:
  ```bash
  sudo usermod -a -G audio $USER
  ```

## Verifying Audio Setup

### List Audio Devices

```bash
poetry run python -c "import sounddevice; print(sounddevice.query_devices())"
```

### Test Microphone

```bash
poetry run rhythmface diagnose
```

Look for:
- ✅ Microphone detected
- ✅ Audio levels responding to sound
- ✅ RMS energy values changing

## Running RhythmFace

### Basic Usage

```bash
poetry run rhythmface run
```

### With Custom Configuration

```bash
# Copy example config
cp example_config.yaml config.yaml

# Edit config.yaml with your preferences
nano config.yaml  # or any editor

# Run with config
poetry run rhythmface run --config config.yaml
```

### Specifying Audio Device

If you have multiple microphones:

1. List devices:
   ```bash
   poetry run rhythmface diagnose
   ```

2. Note the device ID (e.g., `3`)

3. Create/edit `config.yaml`:
   ```yaml
   audio:
     device_id: 3  # Your device ID
   ```

4. Run:
   ```bash
   poetry run rhythmface run --config config.yaml
   ```

## Troubleshooting

### "ModuleNotFoundError"

```bash
# Ensure dependencies are installed
poetry install

# Activate the virtual environment
poetry shell
```

### "No audio input device found"

- Check microphone is connected
- Verify permissions (especially on macOS/Linux)
- Try different USB port if using external mic
- Restart audio services:
  ```bash
  # Linux
  pulseaudio -k && pulseaudio --start
  
  # macOS
  sudo killall coreaudiod
  ```

### "pygame.error: No available video device"

- Ensure display server is running (Linux)
- Try setting SDL environment variables:
  ```bash
  export SDL_VIDEODRIVER=x11  # or wayland
  poetry run rhythmface run
  ```

### Low FPS / Laggy Animation

- Reduce window size in config:
  ```yaml
  graphics:
    window_width: 480
    window_height: 480
  ```

- Disable formant detection:
  ```yaml
  lipsync:
    formant_detection: false
  ```

- Disable vsync:
  ```yaml
  graphics:
    vsync: false
  ```

### Type Checking Errors (Development)

```bash
# Update mypy stubs
poetry run pip install types-pyyaml
```

## Updating RhythmFace

```bash
cd rhythmface
git pull origin main
poetry install
```

## Uninstallation

```bash
# Remove virtual environment
poetry env remove python

# Or manually delete the project directory
cd ..
rm -rf rhythmface
```

## Docker Installation (Alternative)

If you prefer Docker:

```bash
# Build image
docker build -t rhythmface .

# Run with audio device access
docker run --device /dev/snd rhythmface
```

*Note: Docker support is planned for future releases.*

## Next Steps

- Read [QUICKSTART.md](QUICKSTART.md) for usage guide
- Check [README.md](README.md) for features
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Browse [docs/](docs/) for full documentation

## Getting Help

If you encounter issues:

1. Check [GitHub Issues](https://github.com/yourusername/rhythmface/issues)
2. Search existing solutions
3. Create a new issue with:
   - Your OS and Python version
   - Error messages
   - Steps to reproduce

---

**Enjoy RhythmFace!** 🎤

