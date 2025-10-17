Development Guide
=================

This guide covers development workflows, tooling, and best practices for contributing to RhythmFace.

Development Setup
-----------------

Prerequisites
~~~~~~~~~~~~~

* Python 3.10 or higher
* Poetry (for dependency management)
* Git

Initial Setup
~~~~~~~~~~~~~

.. code-block:: bash

   # Clone repository
   git clone https://github.com/yourusername/rhythmface.git
   cd rhythmface

   # Install dependencies
   poetry install --with dev

   # Install pre-commit hooks
   poetry run pre-commit install

   # Generate placeholder assets
   poetry run python -m rhythmface.assets.generator

Development Tools
-----------------

Code Formatting
~~~~~~~~~~~~~~~

The project uses **Black** for code formatting:

.. code-block:: bash

   # Format all code
   poetry run black rhythmface tests

   # Check formatting without changes
   poetry run black --check rhythmface tests

Import Sorting
~~~~~~~~~~~~~~

**isort** maintains import organization:

.. code-block:: bash

   # Sort imports
   poetry run isort rhythmface tests

   # Check import order
   poetry run isort --check rhythmface tests

Linting
~~~~~~~

**Ruff** provides fast Python linting:

.. code-block:: bash

   # Run linter
   poetry run ruff check rhythmface tests

   # Auto-fix issues
   poetry run ruff check --fix rhythmface tests

Type Checking
~~~~~~~~~~~~~

**mypy** enforces static type checking with strict mode:

.. code-block:: bash

   # Run type checker
   poetry run mypy --strict rhythmface

Testing
-------

Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   poetry run pytest

   # Run with coverage
   poetry run pytest --cov=rhythmface

   # Run specific test file
   poetry run pytest tests/test_audio.py

   # Run with verbose output
   poetry run pytest -v

Writing Tests
~~~~~~~~~~~~~

Tests are located in the ``tests/`` directory and follow pytest conventions:

* Test files: ``test_*.py``
* Test classes: ``Test*``
* Test functions: ``test_*``

Example test structure:

.. code-block:: python

   import pytest
   from rhythmface.audio.mic_listener import MicListener

   class TestMicListener:
       def test_initialization(self) -> None:
           listener = MicListener(config)
           assert listener is not None

Pre-commit Hooks
----------------

The project uses pre-commit hooks to ensure code quality. Hooks run automatically on ``git commit``:

1. **black**: Format code
2. **isort**: Sort imports
3. **ruff**: Lint code
4. **mypy**: Type check

Manual hook execution:

.. code-block:: bash

   # Run all hooks on all files
   poetry run pre-commit run --all-files

   # Run specific hook
   poetry run pre-commit run black --all-files

Documentation
-------------

Building Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd docs
   poetry run make html

   # Open in browser
   open _build/html/index.html

The documentation uses Sphinx with the Read the Docs theme.

Architecture
------------

Module Organization
~~~~~~~~~~~~~~~~~~~

The project follows a modular architecture:

* **audio/**: Microphone capture and feature extraction
* **logic/**: Lip-sync engine with strategy pattern
* **graphics/**: Pygame rendering
* **assets/**: Asset generation
* **config**: Configuration management
* **cli**: Command-line interface

Design Patterns
~~~~~~~~~~~~~~~

* **Strategy Pattern**: Lip-sync algorithms (``ILipSyncStrategy``)
* **Strategy Pattern**: Audio sources (``IAudioSource``)
* **Strategy Pattern**: Renderers (``IRenderer``)
* **Plugin System**: Easy extension via interface implementation

Adding New Features
-------------------

Adding a New Lip-Sync Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Implement ``ILipSyncStrategy`` interface
2. Add strategy to ``rhythmface.logic.lipsync_engine``
3. Add tests in ``tests/test_logic.py``
4. Update documentation

.. code-block:: python

   from rhythmface.logic.lipsync_engine import ILipSyncStrategy, MouthShape
   from rhythmface.audio.mic_listener import AudioFeatures

   class MyCustomStrategy(ILipSyncStrategy):
       def analyze(self, features: AudioFeatures) -> MouthShape:
           # Your custom logic here
           return MouthShape.A

Adding a New Audio Source
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Implement ``IAudioSource`` interface
2. Add source to ``rhythmface.audio``
3. Add tests
4. Update CLI to support new source

Continuous Integration
----------------------

The project uses GitHub Actions for CI. The workflow runs on every push and PR:

1. Install dependencies with Poetry
2. Run Ruff linter
3. Check Black formatting
4. Run mypy type checking
5. Execute pytest with coverage

See ``.github/workflows/ci.yml`` for details.

Release Process
---------------

1. Update version in ``pyproject.toml`` and ``rhythmface/__init__.py``
2. Update CHANGELOG.md
3. Create git tag: ``git tag v0.1.0``
4. Push tag: ``git push origin v0.1.0``
5. Build package: ``poetry build``
6. Publish: ``poetry publish``

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Poetry lock file out of sync**

.. code-block:: bash

   poetry lock --no-update
   poetry install

**Pre-commit hooks failing**

.. code-block:: bash

   poetry run pre-commit run --all-files

**Type checking errors**

Check that all imports have type stubs or are added to mypy ignore list in ``pyproject.toml``.

