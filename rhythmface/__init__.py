"""
RhythmFace: Real-time lip-sync animation for a 2D 'rapper vibe' character.

This package provides a modular framework for capturing microphone audio,
analyzing it for speech characteristics, and rendering animated lip movements
on a 2D character in real-time.

The package is organized into the following modules:
- audio: Microphone capture and audio preprocessing
- logic: Lip-sync engine and mouth shape selection
- graphics: Pygame-based rendering engine
- assets: Asset generation and management
- config: Configuration management

Example:
    Basic usage from Python code:

    >>> from rhythmface.cli import main
    >>> main()

    Or from command line:
    $ poetry run rhythmface run
"""

__version__ = "0.1.0"
__author__ = "RhythmFace Contributors"
__license__ = "MIT"

from rhythmface.audio.mic_listener import MicListener
from rhythmface.graphics.renderer import Renderer
from rhythmface.logic.lipsync_engine import LipSyncEngine

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "MicListener",
    "Renderer",
    "LipSyncEngine",
]

