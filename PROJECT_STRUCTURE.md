# RhythmFace Project Structure

This document provides an overview of the project organization and key files.

## Directory Layout

```
rhythmface/
├── .github/                 # GitHub configuration
│   └── workflows/
│       └── ci.yml          # CI/CD pipeline (pytest, mypy, ruff, black)
│
├── docs/                    # Sphinx documentation
│   ├── api/                # API reference docs
│   ├── conf.py             # Sphinx configuration
│   ├── index.rst           # Documentation index
│   ├── modules.rst         # Modules overview
│   ├── development.rst     # Development guide
│   ├── contributing.rst    # Contributing guidelines
│   ├── Makefile           # Unix documentation build
│   └── make.bat           # Windows documentation build
│
├── rhythmface/             # Main package
│   ├── __init__.py        # Package initialization, version info
│   ├── config.py          # Configuration management (YAML + dataclasses)
│   ├── cli.py             # Command-line interface (argparse)
│   ├── py.typed           # PEP 561 type marker
│   │
│   ├── audio/             # Audio capture and processing
│   │   ├── __init__.py
│   │   └── mic_listener.py   # MicListener class, AudioFeatures
│   │
│   ├── logic/             # Lip-sync engine
│   │   ├── __init__.py
│   │   └── lipsync_engine.py # LipSyncEngine, strategies, MouthShape
│   │
│   ├── graphics/          # Rendering
│   │   ├── __init__.py
│   │   └── renderer.py    # Pygame-based renderer
│   │
│   └── assets/            # Asset generation
│       ├── __init__.py
│       └── generator.py   # Pillow-based PNG generation
│
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py        # Pytest fixtures
│   ├── test_audio.py      # Audio module tests
│   ├── test_logic.py      # Logic module tests
│   └── test_graphics.py   # Graphics module tests
│
├── .editorconfig           # Editor configuration
├── .gitignore             # Git ignore patterns
├── .dockerignore          # Docker ignore patterns
├── .pre-commit-config.yaml # Pre-commit hook configuration
├── pyproject.toml         # Poetry configuration, tool settings
├── setup.py               # Backward compatibility setup
├── py.typed               # Type checking marker
├── Makefile               # Development commands
│
├── README.md              # Main documentation
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Version history
├── QUICKSTART.md          # Quick start guide
├── PROJECT_STRUCTURE.md   # This file
├── LICENSE                # MIT License
│
└── example_config.yaml    # Example configuration file
```

## Key Files and Their Purposes

### Configuration Files

- **pyproject.toml**: Poetry configuration, dependencies, tool settings (Black, Ruff, mypy, pytest)
- **.pre-commit-config.yaml**: Pre-commit hooks (Black → isort → Ruff → mypy)
- **.github/workflows/ci.yml**: CI pipeline for automated testing and checks
- **example_config.yaml**: Example runtime configuration for the application

### Main Package (`rhythmface/`)

#### Entry Points
- **cli.py**: Command-line interface
  - Commands: `run`, `diagnose`
  - Configuration loading
  - Main entry point

#### Core Modules
- **config.py**: Configuration management
  - `AudioConfig`: Audio capture settings
  - `LipSyncConfig`: Lip-sync analysis settings
  - `GraphicsConfig`: Rendering settings
  - YAML loading/saving

#### Audio Module (`rhythmface/audio/`)
- **mic_listener.py**:
  - `IAudioSource`: Abstract audio source interface
  - `MicListener`: Real-time microphone capture
  - `AudioFeatures`: Audio feature dataclass (RMS, MFCC, etc.)
  - Feature extraction pipeline (placeholder)

#### Logic Module (`rhythmface/logic/`)
- **lipsync_engine.py**:
  - `MouthShape`: Enum for mouth positions (CLOSED, A, O, E)
  - `ILipSyncStrategy`: Strategy pattern interface
  - `EnergyBasedStrategy`: Simple energy-based lip-sync
  - `MFCCBasedStrategy`: MFCC-based vowel detection
  - `LipSyncEngine`: Main engine with temporal smoothing

#### Graphics Module (`rhythmface/graphics/`)
- **renderer.py**:
  - `IRenderer`: Abstract renderer interface
  - `Renderer`: Pygame-based implementation
  - Asset loading and compositing
  - Frame rendering and event handling

#### Assets Module (`rhythmface/assets/`)
- **generator.py**:
  - Automatic PNG generation using Pillow
  - Character base image generation
  - Mouth shape image generation
  - Asset verification and regeneration

### Tests (`tests/`)

- **conftest.py**: Shared pytest fixtures
- **test_audio.py**: Audio module tests (MicListener, AudioFeatures)
- **test_logic.py**: Logic module tests (LipSyncEngine, strategies)
- **test_graphics.py**: Graphics module tests (Renderer)

### Documentation (`docs/`)

- **index.rst**: Main documentation page
- **api/**: Auto-generated API documentation
- **development.rst**: Development setup and workflows
- **contributing.rst**: Contribution guidelines

## Architecture Patterns

### Strategy Pattern

Used throughout for pluggable implementations:

1. **Lip-sync Strategies** (`ILipSyncStrategy`)
   - Energy-based
   - MFCC-based
   - Future: ML-based, formant-based

2. **Audio Sources** (`IAudioSource`)
   - Microphone
   - Future: File, network stream

3. **Renderers** (`IRenderer`)
   - Pygame
   - Future: OpenGL, web canvas

### Separation of Concerns

- **Audio**: Capture and feature extraction
- **Logic**: Analysis and decision making
- **Graphics**: Rendering and display
- **Config**: Centralized configuration
- **CLI**: User interface

### Type Safety

- Full type hints with mypy strict mode
- PEP 561 compliance (`py.typed` marker)
- Abstract base classes for interfaces

## Development Workflow

### Setup
```bash
poetry install --with dev
poetry run pre-commit install
```

### Development Commands
```bash
make test          # Run tests
make lint          # Run linter
make format        # Format code
make type-check    # Type checking
make docs          # Build documentation
make run           # Run application
```

### Pre-commit Hooks
Runs automatically on `git commit`:
1. Black (formatting)
2. isort (import sorting)
3. Ruff (linting)
4. mypy (type checking)

### CI/CD
GitHub Actions workflow on push/PR:
1. Install dependencies
2. Run Ruff
3. Check Black formatting
4. Run mypy
5. Execute pytest with coverage

## Extension Points

### Adding a New Lip-Sync Strategy

1. Implement `ILipSyncStrategy` in `logic/lipsync_engine.py`
2. Add tests in `tests/test_logic.py`
3. Document in `docs/api/logic.rst`

### Adding a New Audio Source

1. Implement `IAudioSource` in `audio/` module
2. Add tests in `tests/test_audio.py`
3. Update CLI to support new source

### Adding a New Renderer

1. Implement `IRenderer` in `graphics/` module
2. Add tests in `tests/test_graphics.py`
3. Update CLI to support new renderer

## Dependencies

### Runtime Dependencies
- **sounddevice**: Audio I/O
- **numpy**: Numerical computing
- **pygame**: 2D rendering
- **pillow**: Image generation
- **librosa**: Audio analysis
- **pyyaml**: Configuration files

### Development Dependencies
- **black**: Code formatting
- **isort**: Import sorting
- **ruff**: Fast linting
- **mypy**: Type checking
- **pytest**: Testing framework
- **pytest-cov**: Coverage reporting
- **sphinx**: Documentation generation
- **pre-commit**: Git hooks

## Asset Generation

Placeholder assets are auto-generated using Pillow:

- **base.png**: Character silhouette (512×512)
- **mouth_closed.png**: Closed mouth (256×128)
- **mouth_A.png**: "Ah" vowel (256×128)
- **mouth_O.png**: "Oh" vowel (256×128)
- **mouth_E.png**: "Eh" vowel (256×128)

Generate with:
```bash
poetry run python -m rhythmface.assets.generator
```

## Configuration

Runtime configuration via `config.yaml`:

- **audio**: Microphone settings, sample rate, thresholds
- **lipsync**: FPS, vowel detection, smoothing
- **graphics**: Window size, colors, vsync

See `example_config.yaml` for full options.

## Future Enhancements

Planned additions (see CONTRIBUTING.md for details):

- Formant-based vowel detection
- ML model integration
- Additional mouth shapes (consonants)
- Custom character sprites
- Web-based version
- VST/OBS plugins

---

For more details, see:
- [README.md](README.md): Project overview
- [CONTRIBUTING.md](CONTRIBUTING.md): Contribution guide
- [QUICKSTART.md](QUICKSTART.md): Quick start guide
- [docs/](docs/): Full documentation

