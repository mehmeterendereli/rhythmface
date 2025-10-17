"""
Pytest configuration and shared fixtures.
"""

import pytest


@pytest.fixture
def sample_audio_config():
    """Provide sample audio configuration for tests."""
    from rhythmface.config import AudioConfig
    return AudioConfig(
        sample_rate=44100,
        chunk_size=1024,
        channels=1,
        energy_threshold=0.05,
    )


@pytest.fixture
def sample_lipsync_config():
    """Provide sample lip-sync configuration for tests."""
    from rhythmface.config import LipSyncConfig
    return LipSyncConfig(
        fps=30,
        formant_detection=False,
        mfcc_coefficients=13,
        smoothing_window=3,
    )


@pytest.fixture
def sample_graphics_config():
    """Provide sample graphics configuration for tests."""
    from rhythmface.config import GraphicsConfig
    return GraphicsConfig(
        window_width=640,
        window_height=640,
        window_title="RhythmFace Test",
        background_color=(30, 30, 40),
        vsync=False,
        fullscreen=False,
    )

