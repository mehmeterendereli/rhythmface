"""
Microphone audio capture and preprocessing.

This module provides the MicListener class for real-time audio capture
and feature extraction using sounddevice and librosa.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

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
    def get_latest_features(self) -> AudioFeatures | None:
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
        self._audio_buffer: npt.NDArray[np.float32] | None = None
        self._latest_features: AudioFeatures | None = None
        self._stream: object | None = None

    def start(self) -> None:
        """
        Start capturing audio from microphone.

        Raises:
            RuntimeError: If audio device cannot be opened
        """
        import sounddevice as sd

        try:
            self._stream = sd.InputStream(
                samplerate=self.config.sample_rate,
                channels=self.config.channels,
                blocksize=self.config.chunk_size,
                device=self.config.device_id,
                callback=self._audio_callback,
                dtype=np.float32,
            )
            self._stream.start()  # type: ignore
            self._is_active = True
        except Exception as e:
            raise RuntimeError(f"Failed to open audio device: {e}") from e

    def stop(self) -> None:
        """Stop audio capture and cleanup resources."""
        if self._stream is not None:
            self._stream.stop()  # type: ignore
            self._stream.close()  # type: ignore
            self._stream = None
        self._is_active = False

    def get_latest_features(self) -> AudioFeatures | None:
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
        # Silently handle stream status (overflow is normal in real-time audio)
        if status and "overflow" not in str(status).lower():
            print(f"Audio stream status: {status}")

        # Copy audio data
        audio = indata[:, 0].copy() if indata.ndim > 1 else indata.copy()

        # Extract features
        self._latest_features = self._extract_features(audio)

    def _extract_features(self, audio: npt.NDArray[np.float32]) -> AudioFeatures:
        """
        Extract acoustic features from audio chunk.

        Args:
            audio: Audio samples (mono, float32)

        Returns:
            AudioFeatures with computed features
        """
        import librosa

        # Compute RMS energy
        rms_energy = float(np.sqrt(np.mean(audio**2)))

        # Compute MFCC using librosa
        # Use n_fft that matches our chunk size to avoid warnings
        n_fft = min(2048, len(audio))
        mfccs = librosa.feature.mfcc(
            y=audio,
            sr=self.config.sample_rate,
            n_mfcc=13,
            n_fft=n_fft,
            hop_length=len(audio),  # Single frame
        )
        mfcc = mfccs[:, 0].astype(np.float32)

        # Compute spectral centroid
        centroid = librosa.feature.spectral_centroid(
            y=audio, sr=self.config.sample_rate, n_fft=n_fft, hop_length=len(audio)
        )
        spectral_centroid = float(centroid[0, 0]) if centroid.size > 0 else 0.0

        # Compute zero-crossing rate
        zcr = librosa.feature.zero_crossing_rate(y=audio, hop_length=len(audio))
        zero_crossing_rate = float(zcr[0, 0]) if zcr.size > 0 else 0.0

        # Determine if speech is present (energy threshold)
        is_speech = rms_energy > self.config.energy_threshold

        return AudioFeatures(
            rms_energy=rms_energy,
            mfcc=mfcc,
            spectral_centroid=spectral_centroid,
            zero_crossing_rate=zero_crossing_rate,
            is_speech=is_speech,
        )

    @staticmethod
    def list_devices() -> list[dict[str, object]]:
        """
        List available audio input devices.

        Returns:
            List of device information dictionaries
        """
        import sounddevice as sd

        devices = sd.query_devices()
        input_devices = []
        for idx, device in enumerate(devices):  # type: ignore
            if device["max_input_channels"] > 0:  # type: ignore
                input_devices.append(
                    {
                        "index": idx,
                        "name": device["name"],  # type: ignore
                        "channels": device["max_input_channels"],  # type: ignore
                        "sample_rate": device["default_samplerate"],  # type: ignore
                    }
                )
        return input_devices
