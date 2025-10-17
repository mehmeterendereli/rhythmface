"""
Microphone audio capture and preprocessing.

This module provides the MicListener class for real-time audio capture
and feature extraction using sounddevice and librosa.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

import numpy as np
import numpy.typing as npt

from rhythmface.config import AudioConfig


@dataclass
class AudioFeatures:
    """
    Extracted audio features for a single frame.

    Attributes:
        rms_energy: Root mean square energy (amplitude)
        mfcc: Mel-frequency cepstral coefficients
        spectral_centroid: Center of mass of spectrum
        zero_crossing_rate: Rate of sign changes in signal
        is_speech: Whether frame contains speech-like audio
    """

    rms_energy: float
    mfcc: npt.NDArray[np.float32]
    spectral_centroid: float
    zero_crossing_rate: float
    is_speech: bool


class IAudioSource(ABC):
    """
    Abstract interface for audio sources.

    This interface allows for different audio input implementations
    (microphone, file, network stream, etc.) following the Strategy pattern.
    """

    @abstractmethod
    def start(self) -> None:
        """Start audio capture."""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Stop audio capture."""
        pass

    @abstractmethod
    def get_latest_features(self) -> Optional[AudioFeatures]:
        """
        Get most recent audio features.

        Returns:
            AudioFeatures if available, None otherwise
        """
        pass

    @abstractmethod
    def is_active(self) -> bool:
        """Check if audio source is currently active."""
        pass


class MicListener(IAudioSource):
    """
    Real-time microphone audio capture and feature extraction.

    This class captures audio from the system microphone, computes
    acoustic features (RMS, MFCC, spectral features), and provides
    them for lip-sync analysis.

    Example:
        >>> from rhythmface.config import AudioConfig
        >>> config = AudioConfig()
        >>> listener = MicListener(config)
        >>> listener.start()
        >>> features = listener.get_latest_features()
        >>> listener.stop()
    """

    def __init__(self, config: AudioConfig) -> None:
        """
        Initialize microphone listener.

        Args:
            config: Audio configuration
        """
        self.config = config
        self._is_active = False
        self._audio_buffer: Optional[npt.NDArray[np.float32]] = None
        self._latest_features: Optional[AudioFeatures] = None

        # TODO: Initialize sounddevice stream
        # TODO: Set up audio processing pipeline

    def start(self) -> None:
        """
        Start capturing audio from microphone.

        Raises:
            RuntimeError: If audio device cannot be opened
        """
        # TODO: Open sounddevice input stream
        # TODO: Start background thread for feature extraction
        self._is_active = True

    def stop(self) -> None:
        """Stop audio capture and cleanup resources."""
        # TODO: Stop sounddevice stream
        # TODO: Cleanup background threads
        self._is_active = False

    def get_latest_features(self) -> Optional[AudioFeatures]:
        """
        Get most recent audio features.

        Returns:
            AudioFeatures if available, None if no audio captured yet
        """
        return self._latest_features

    def is_active(self) -> bool:
        """
        Check if listener is actively capturing.

        Returns:
            True if capturing, False otherwise
        """
        return self._is_active

    def _audio_callback(
        self,
        indata: npt.NDArray[np.float32],
        frames: int,
        time_info: object,
        status: object,
    ) -> None:
        """
        Callback for sounddevice stream (called on audio thread).

        Args:
            indata: Input audio data
            frames: Number of frames
            time_info: Timing information
            status: Stream status
        """
        # TODO: Copy audio data to buffer
        # TODO: Trigger feature extraction
        pass

    def _extract_features(self, audio: npt.NDArray[np.float32]) -> AudioFeatures:
        """
        Extract acoustic features from audio chunk.

        Args:
            audio: Audio samples (mono, float32)

        Returns:
            AudioFeatures with computed features
        """
        # TODO: Compute RMS energy
        # TODO: Compute MFCC using librosa
        # TODO: Compute spectral centroid
        # TODO: Compute zero-crossing rate
        # TODO: Determine if speech is present (energy threshold)

        # Placeholder return
        return AudioFeatures(
            rms_energy=0.0,
            mfcc=np.zeros(13, dtype=np.float32),  # Default 13 MFCC coefficients
            spectral_centroid=0.0,
            zero_crossing_rate=0.0,
            is_speech=False,
        )

    @staticmethod
    def list_devices() -> list[dict[str, object]]:
        """
        List available audio input devices.

        Returns:
            List of device information dictionaries
        """
        # TODO: Use sounddevice.query_devices() to list inputs
        return []

