.. RhythmFace documentation master file

RhythmFace Documentation
========================

**RhythmFace** is a real-time lip-sync animation system for 2D characters with a "rapper vibe" aesthetic.
It captures microphone audio, analyzes speech features, and animates a character's mouth movements in real-time.

Features
--------

* Real-time audio capture and processing
* MFCC-based vowel detection for accurate lip-sync
* Modular architecture with strategy pattern support
* Pygame-based rendering with smooth animations
* Comprehensive test coverage
* Professional development tooling (Black, Ruff, mypy, pre-commit)

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/yourusername/rhythmface.git
   cd rhythmface

   # Install Poetry (if not already installed)
   pip install poetry

   # Install dependencies
   poetry install

   # Install pre-commit hooks
   poetry run pre-commit install

Running the Application
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run the main application
   poetry run rhythmface run

   # Run diagnostics
   poetry run rhythmface diagnose

Configuration
~~~~~~~~~~~~~

Create a ``config.yaml`` file to customize settings:

.. code-block:: yaml

   audio:
     sample_rate: 44100
     chunk_size: 1024
     energy_threshold: 0.05

   lipsync:
     fps: 30
     formant_detection: true

   graphics:
     window_width: 640
     window_height: 640

Then run with:

.. code-block:: bash

   poetry run rhythmface run --config config.yaml

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   api
   development
   contributing

API Reference
-------------

.. toctree::
   :maxdepth: 2
   :caption: API:

   api/audio
   api/logic
   api/graphics
   api/config

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

