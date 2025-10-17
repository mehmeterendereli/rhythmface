# RhythmFace Quick Start Guide

This guide will help you get RhythmFace up and running in minutes.

## Installation

### 1. Prerequisites

Make sure you have:
- Python 3.10+ installed
- Poetry installed (run `pip install poetry` if needed)
- A working microphone

### 2. Clone and Install

```bash
# Clone the repository
git clone https://github.com/yourusername/rhythmface.git
cd rhythmface

# Install dependencies
poetry install

# Generate placeholder assets (character and mouth shapes)
poetry run python -m rhythmface.assets.generator
```

## Running the Application

### Basic Usage

```bash
# Start RhythmFace with default settings
poetry run rhythmface run
```

The application will:
1. Open a window showing the character
2. Start capturing audio from your default microphone
3. Animate the character's mouth based on your speech

Press `ESC` or `Q` to quit.

### Test Your Setup

```bash
# Run diagnostics to verify audio devices and rendering
poetry run rhythmface diagnose
```

This will show:
- Available audio input devices
- Microphone capture test
- Rendering FPS test

### Custom Configuration

Create a `config.yaml` file:

```yaml
audio:
  sample_rate: 44100
  energy_threshold: 0.05

lipsync:
  fps: 30
  formant_detection: true

graphics:
  window_width: 800
  window_height: 800
```

Run with your config:

```bash
poetry run rhythmface run --config config.yaml
```

## Troubleshooting

### No audio input

If the application doesn't respond to audio:

1. Check microphone permissions
2. List available devices: `poetry run rhythmface diagnose`
3. Specify device in config: `device_id: 1`

### Low FPS

If rendering is slow:

1. Disable vsync: `vsync: false` in config
2. Reduce window size: `window_width: 480`
3. Disable formant detection: `formant_detection: false`

### Import errors

Make sure dependencies are installed:

```bash
poetry install
```

## Next Steps

- Read the [full documentation](https://rhythmface.readthedocs.io)
- Explore [example configurations](example_config.yaml)
- Check out [contributing guidelines](CONTRIBUTING.md) to add features
- Join the community on GitHub Discussions

## Controls

- `ESC` or `Q`: Quit application
- `F`: Toggle fullscreen (when implemented)

## Performance Tips

For best results:
- Use a good quality microphone
- Minimize background noise
- Speak clearly toward the microphone
- Adjust `energy_threshold` if mouth movements are too sensitive/insensitive

---

Enjoy using RhythmFace! 🎤

