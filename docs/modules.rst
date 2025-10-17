Modules Overview
================

RhythmFace is organized into several modules, each with a specific responsibility:

Audio Module
------------

The audio module handles real-time microphone capture and feature extraction.

* ``rhythmface.audio.mic_listener``: Microphone capture and preprocessing

Logic Module
------------

The logic module implements the lip-sync engine and mouth shape selection.

* ``rhythmface.logic.lipsync_engine``: Main lip-sync engine with strategy pattern support

Graphics Module
---------------

The graphics module provides pygame-based rendering.

* ``rhythmface.graphics.renderer``: Real-time character rendering

Assets Module
-------------

The assets module generates placeholder character and mouth images.

* ``rhythmface.assets.generator``: Automatic asset generation using Pillow

Configuration
-------------

Configuration management for the application.

* ``rhythmface.config``: Configuration dataclasses and YAML loading

