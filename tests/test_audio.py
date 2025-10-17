"""
Tests for audio module (microphone capture and feature extraction).
"""

import numpy as np
import pytest

from rhythmface.audio.mic_listener import AudioFeatures, MicListener
from rhythmface.config import AudioConfig


class TestAudioFeatures:
    """Test AudioFeatures dataclass."""

    def test_audio_features_creation(self) -> None:
        """Test creating AudioFeatures instance."""
        mfcc = np.zeros(13, dtype=np.float32)
        features = AudioFeatures(
            rms_energy=0.5,
            mfcc=mfcc,
            spectral_centroid=1000.0,
            zero_crossing_rate=0.1,
            is_speech=True,
        )

        assert features.rms_energy == 0.5
        assert features.is_speech is True
        assert len(features.mfcc) == 13


class TestMicListener:
    """Test MicListener class."""

    def test_mic_listener_initialization(self) -> None:
        """Test MicListener can be instantiated with config."""
        config = AudioConfig()
        listener = MicListener(config)

        assert listener.config == config
        assert not listener.is_active()

    def test_mic_listener_start_stop(self) -> None:
        """Test starting and stopping listener."""
        config = AudioConfig()
        listener = MicListener(config)

        # Initial state
        assert not listener.is_active()

        # Start (placeholder, won't actually capture)
        listener.start()
        assert listener.is_active()

        # Stop
        listener.stop()
        assert not listener.is_active()

    def test_get_latest_features_returns_none_initially(self) -> None:
        """Test that get_latest_features returns None before any audio."""
        config = AudioConfig()
        listener = MicListener(config)

        features = listener.get_latest_features()
        assert features is None

    def test_list_devices_returns_list(self) -> None:
        """Test that list_devices returns a list (may be empty in test env)."""
        devices = MicListener.list_devices()
        assert isinstance(devices, list)


class TestAudioIntegration:
    """Integration tests for audio pipeline."""

    def test_mock_audio_processing(self) -> None:
        """Test audio feature extraction with mock data."""
        # TODO: Implement when feature extraction is complete
        # 1. Create synthetic audio signal
        # 2. Pass through feature extraction
        # 3. Verify MFCC, RMS, etc. are computed
        pass

    def test_energy_threshold(self) -> None:
        """Test energy threshold for speech detection."""
        # TODO: Implement speech detection test
        # 1. Create low-energy signal (silence)
        # 2. Create high-energy signal (speech)
        # 3. Verify is_speech flag is set correctly
        pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

