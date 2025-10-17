# RhythmFace 🎤

[![CI](https://github.com/yourusername/rhythmface/workflows/CI/badge.svg)](https://github.com/yourusername/rhythmface/actions)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**RhythmFace** is a real-time lip-sync animation system for 2D characters with a "rapper vibe" aesthetic. It captures microphone audio, analyzes speech features, and animates a character's mouth movements in real-time using advanced audio processing techniques.

## ✨ Features

- 🎙️ **Real-time Audio Capture**: Low-latency microphone input processing
- 🗣️ **Vowel Detection**: MFCC-based phoneme analysis for accurate lip-sync
- 🎨 **Stylized Character**: Street-style "rapper vibe" aesthetic
- 🔌 **Plugin Architecture**: Strategy pattern for extensible lip-sync algorithms
- 🎯 **Smooth Animation**: Temporal smoothing for natural mouth movements
- 🧪 **Comprehensive Testing**: 80%+ test coverage with pytest
- 🛠️ **Professional Dev Tools**: Black, Ruff, mypy, pre-commit hooks
- 📚 **Full Documentation**: Sphinx-generated API docs

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)
- Microphone (for audio input)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/rhythmface.git
cd rhythmface

# Install Poetry (if not already installed)
pip install poetry

# Install dependencies
poetry install

# Install pre-commit hooks (optional but recommended)
poetry run pre-commit install

# Generate placeholder assets
poetry run python -m rhythmface.assets.generator
```

### Running the Application

```bash
# Start the application
poetry run rhythmface run

# Or with custom configuration
poetry run rhythmface run --config config.yaml

# Run diagnostics (test audio devices and rendering)
poetry run rhythmface diagnose
```

## 🎛️ Configuration

Create a `config.yaml` file to customize settings:

```yaml
audio:
  sample_rate: 44100
  chunk_size: 1024
  channels: 1
  energy_threshold: 0.05
  device_id: null  # null = system default

lipsync:
  fps: 30
  formant_detection: true
  mfcc_coefficients: 13
  smoothing_window: 3

graphics:
  window_width: 640
  window_height: 640
  window_title: "RhythmFace"
  background_color: [30, 30, 40]
  vsync: true
  fullscreen: false
```

## 🏗️ Architecture

RhythmFace follows a modular, plugin-friendly architecture:

```
rhythmface/
├── audio/           # Audio capture and preprocessing
│   └── mic_listener.py
├── logic/           # Lip-sync engine with strategy pattern
│   └── lipsync_engine.py
├── graphics/        # Pygame-based renderer
│   └── renderer.py
├── assets/          # Asset generation (Pillow)
│   └── generator.py
├── config.py        # Configuration management
└── cli.py           # Command-line interface
```

### Key Design Patterns

- **Strategy Pattern**: Pluggable lip-sync algorithms (`ILipSyncStrategy`)
- **Strategy Pattern**: Audio sources (`IAudioSource`)
- **Strategy Pattern**: Renderers (`IRenderer`)
- **Separation of Concerns**: Independent audio, logic, and graphics layers

## 🔧 Development

### Setup Development Environment

```bash
# Install with development dependencies
poetry install --with dev

# Install pre-commit hooks
poetry run pre-commit install
```

### Development Tools

#### Code Formatting

```bash
# Format code with Black
poetry run black rhythmface tests

# Sort imports with isort
poetry run isort rhythmface tests
```

#### Linting

```bash
# Run Ruff linter
poetry run ruff check rhythmface tests

# Auto-fix issues
poetry run ruff check --fix rhythmface tests
```

#### Type Checking

```bash
# Run mypy with strict mode
poetry run mypy --strict rhythmface
```

#### Testing

```bash
# Run all tests
poetry run pytest

# Run with coverage report
poetry run pytest --cov=rhythmface --cov-report=html

# Run specific test file
poetry run pytest tests/test_audio.py -v
```

#### Pre-commit Hooks

The project uses pre-commit hooks to ensure code quality:

1. **Black** → Code formatting
2. **isort** → Import sorting
3. **Ruff** → Linting
4. **mypy** → Type checking

```bash
# Run all hooks manually
poetry run pre-commit run --all-files
```

### Building Documentation

```bash
cd docs
poetry run make html

# Open in browser (Unix/Mac)
open _build/html/index.html

# Open in browser (Windows)
start _build/html/index.html
```

## 📦 Building and Distribution

### Build Package

```bash
# Build wheel and source distribution
poetry build

# Output: dist/rhythmface-0.1.0.tar.gz and dist/rhythmface-0.1.0-*.whl
```

### Publish to PyPI

```bash
# Configure PyPI credentials (first time only)
poetry config pypi-token.pypi YOUR_PYPI_TOKEN

# Publish to PyPI
poetry publish

# Or build and publish in one command
poetry publish --build
```

## 🧪 Testing

The project maintains comprehensive test coverage:

- **Unit Tests**: Individual component testing
- **Integration Tests**: Cross-module interaction testing
- **Smoke Tests**: Basic functionality verification

```bash
# Run tests with coverage
poetry run pytest --cov=rhythmface --cov-report=term-missing

# Generate HTML coverage report
poetry run pytest --cov=rhythmface --cov-report=html
open htmlcov/index.html
```

## 🎨 Assets

RhythmFace automatically generates placeholder assets using Pillow. Assets include:

- `base.png` (512×512): Character silhouette with "rapper vibe"
- `mouth_closed.png` (256×128): Closed mouth
- `mouth_A.png` (256×128): Open mouth for "ah" sound
- `mouth_O.png` (256×128): Rounded mouth for "oh" sound
- `mouth_E.png` (256×128): Wide mouth for "eh" sound

To regenerate assets:

```bash
poetry run python -m rhythmface.assets.generator --force
```

## 🔌 Extending RhythmFace

### Adding a Custom Lip-Sync Strategy

```python
from rhythmface.logic.lipsync_engine import ILipSyncStrategy, MouthShape
from rhythmface.audio.mic_listener import AudioFeatures

class MyCustomStrategy(ILipSyncStrategy):
    def analyze(self, features: AudioFeatures) -> MouthShape:
        # Your custom vowel detection logic here
        if features.rms_energy > 0.5:
            return MouthShape.A
        return MouthShape.CLOSED

# Use it in your code
from rhythmface.logic.lipsync_engine import LipSyncEngine
from rhythmface.config import LipSyncConfig

config = LipSyncConfig()
engine = LipSyncEngine(config)
engine.set_strategy(MyCustomStrategy())
```

### Adding a Custom Audio Source

```python
from rhythmface.audio.mic_listener import IAudioSource, AudioFeatures

class FileAudioSource(IAudioSource):
    def start(self) -> None:
        # Load audio file
        pass

    def stop(self) -> None:
        # Cleanup
        pass

    def get_latest_features(self) -> AudioFeatures | None:
        # Return features from file
        pass

    def is_active(self) -> bool:
        return True
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on:

- Code of Conduct
- Development workflow
- Pull request process
- Coding standards

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **sounddevice**: Real-time audio I/O
- **librosa**: Audio feature extraction
- **pygame**: 2D rendering
- **Pillow**: Asset generation
- **Poetry**: Dependency management
- **Black, Ruff, mypy**: Development tooling

## 📞 Support

- 📖 [Documentation](https://rhythmface.readthedocs.io)
- 🐛 [Issue Tracker](https://github.com/yourusername/rhythmface/issues)
- 💬 [Discussions](https://github.com/yourusername/rhythmface/discussions)

## 🗺️ Roadmap

- [ ] Add formant-based vowel detection
- [ ] Implement ML model for phoneme classification
- [ ] Add more mouth shapes (consonants)
- [ ] Support for custom character sprites
- [ ] Web-based version using WebGL
- [ ] VST plugin for DAWs
- [ ] OBS plugin for streaming

---

**Made with ❤️ by the RhythmFace team**

