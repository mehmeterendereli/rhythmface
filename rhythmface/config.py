"""
Configuration management for RhythmFace.

This module provides configuration loading and validation using pydantic-style
dataclasses. Default values are provided, and users can override them via YAML
files or programmatic API.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class AudioConfig:
    """Audio capture and processing configuration."""

    sample_rate: int = 44100
    """Sample rate for audio capture (Hz)."""

    chunk_size: int = 1024
    """Number of audio samples per processing chunk."""

    channels: int = 1
    """Number of audio channels (1 = mono, 2 = stereo)."""

    energy_threshold: float = 0.015
    """Minimum RMS energy to trigger mouth movement (0.0-1.0)."""

    device_id: int | None = None
    """Audio input device ID. None = system default."""


@dataclass
class LipSyncConfig:
    """Lip-sync analysis configuration."""

    fps: int = 30
    """Target frames per second for animation."""

    formant_detection: bool = True
    """Enable formant-based vowel detection (more accurate but slower)."""

    mfcc_coefficients: int = 13
    """Number of MFCC coefficients to compute."""

    smoothing_window: int = 3
    """Number of frames to average for mouth shape smoothing."""


@dataclass
class GraphicsConfig:
    """Rendering and display configuration."""

    window_width: int = 640
    """Window width in pixels."""

    window_height: int = 640
    """Window height in pixels."""

    window_title: str = "RhythmFace"
    """Window title text."""

    background_color: tuple[int, int, int] = (25, 25, 35)
    """Background color as RGB tuple (dark modern theme)."""

    vsync: bool = True
    """Enable vertical sync."""

    fullscreen: bool = False
    """Start in fullscreen mode."""


@dataclass
class RhythmFaceConfig:
    """Master configuration for RhythmFace application."""

    audio: AudioConfig = field(default_factory=AudioConfig)
    lipsync: LipSyncConfig = field(default_factory=LipSyncConfig)
    graphics: GraphicsConfig = field(default_factory=GraphicsConfig)

    @classmethod
    def from_yaml(cls, path: Path) -> "RhythmFaceConfig":
        """
        Load configuration from YAML file.

        Args:
            path: Path to YAML configuration file

        Returns:
            RhythmFaceConfig instance with loaded values

        Raises:
            FileNotFoundError: If config file doesn't exist
            yaml.YAMLError: If YAML parsing fails
        """
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return cls.from_dict(data or {})

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "RhythmFaceConfig":
        """
        Create configuration from dictionary.

        Args:
            data: Configuration dictionary with nested audio/lipsync/graphics keys

        Returns:
            RhythmFaceConfig instance
        """
        audio_data = data.get("audio", {})
        lipsync_data = data.get("lipsync", {})
        graphics_data = data.get("graphics", {})

        return cls(
            audio=AudioConfig(**audio_data),
            lipsync=LipSyncConfig(**lipsync_data),
            graphics=GraphicsConfig(**graphics_data),
        )

    def to_yaml(self, path: Path) -> None:
        """
        Save configuration to YAML file.

        Args:
            path: Output path for YAML file
        """
        data = {
            "audio": {
                "sample_rate": self.audio.sample_rate,
                "chunk_size": self.audio.chunk_size,
                "channels": self.audio.channels,
                "energy_threshold": self.audio.energy_threshold,
                "device_id": self.audio.device_id,
            },
            "lipsync": {
                "fps": self.lipsync.fps,
                "formant_detection": self.lipsync.formant_detection,
                "mfcc_coefficients": self.lipsync.mfcc_coefficients,
                "smoothing_window": self.lipsync.smoothing_window,
            },
            "graphics": {
                "window_width": self.graphics.window_width,
                "window_height": self.graphics.window_height,
                "window_title": self.graphics.window_title,
                "background_color": self.graphics.background_color,
                "vsync": self.graphics.vsync,
                "fullscreen": self.graphics.fullscreen,
            },
        }

        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, default_flow_style=False)


def get_default_config() -> RhythmFaceConfig:
    """
    Get default configuration.

    Returns:
        RhythmFaceConfig with all default values
    """
    return RhythmFaceConfig()
