"""
Audio processing module for RhythmFace.

This module handles real-time microphone input capture, preprocessing,
and feature extraction for lip-sync analysis.
"""

from rhythmface.audio.mic_listener import AudioFeatures, MicListener

__all__ = ["MicListener", "AudioFeatures"]
