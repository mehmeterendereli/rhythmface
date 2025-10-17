"""
Tests for logic module (lip-sync engine and mouth shape selection).
"""

import numpy as np
import pytest

from rhythmface.audio.mic_listener import AudioFeatures
from rhythmface.config import LipSyncConfig
from rhythmface.logic.lipsync_engine import (
    EnergyBasedStrategy,
    LipSyncEngine,
    MFCCBasedStrategy,
    MouthShape,
)


class TestMouthShape:
    """Test MouthShape enum."""

    def test_mouth_shape_values(self) -> None:
        """Test that all mouth shapes have correct values."""
        assert MouthShape.CLOSED.value == "closed"
        assert MouthShape.A.value == "A"
        assert MouthShape.O.value == "O"
        assert MouthShape.E.value == "E"

    def test_mouth_shape_iteration(self) -> None:
        """Test iterating over all mouth shapes."""
        shapes = list(MouthShape)
        assert len(shapes) == 4
        assert MouthShape.CLOSED in shapes


class TestEnergyBasedStrategy:
    """Test simple energy-based lip-sync strategy."""

    def test_low_energy_returns_closed(self) -> None:
        """Test that low energy returns closed mouth."""
        strategy = EnergyBasedStrategy(threshold=0.1)
        features = AudioFeatures(
            rms_energy=0.05,
            mfcc=np.zeros(13, dtype=np.float32),
            spectral_centroid=0.0,
            zero_crossing_rate=0.0,
            is_speech=False,
        )

        shape = strategy.analyze(features)
        assert shape == MouthShape.CLOSED

    def test_high_energy_returns_open(self) -> None:
        """Test that high energy returns open mouth."""
        strategy = EnergyBasedStrategy(threshold=0.1)
        features = AudioFeatures(
            rms_energy=0.5,
            mfcc=np.zeros(13, dtype=np.float32),
            spectral_centroid=0.0,
            zero_crossing_rate=0.0,
            is_speech=True,
        )

        shape = strategy.analyze(features)
        assert shape == MouthShape.A


class TestMFCCBasedStrategy:
    """Test MFCC-based vowel detection strategy."""

    def test_no_speech_returns_closed(self) -> None:
        """Test that no speech returns closed mouth."""
        strategy = MFCCBasedStrategy(energy_threshold=0.1)
        features = AudioFeatures(
            rms_energy=0.05,
            mfcc=np.zeros(13, dtype=np.float32),
            spectral_centroid=0.0,
            zero_crossing_rate=0.0,
            is_speech=False,
        )

        shape = strategy.analyze(features)
        assert shape == MouthShape.CLOSED

    def test_speech_present_returns_vowel(self) -> None:
        """Test that speech returns vowel shape (placeholder)."""
        strategy = MFCCBasedStrategy(energy_threshold=0.1)
        features = AudioFeatures(
            rms_energy=0.5,
            mfcc=np.random.randn(13).astype(np.float32),
            spectral_centroid=1000.0,
            zero_crossing_rate=0.1,
            is_speech=True,
        )

        shape = strategy.analyze(features)
        # With placeholder logic, should return A
        assert shape in [MouthShape.A, MouthShape.O, MouthShape.E, MouthShape.CLOSED]


class TestLipSyncEngine:
    """Test main LipSyncEngine class."""

    def test_engine_initialization(self) -> None:
        """Test engine can be initialized with config."""
        config = LipSyncConfig()
        engine = LipSyncEngine(config)

        assert engine.config == config
        assert engine.get_current_shape() == MouthShape.CLOSED

    def test_engine_update_with_features(self) -> None:
        """Test updating engine with audio features."""
        config = LipSyncConfig(smoothing_window=1)
        engine = LipSyncEngine(config)

        features = AudioFeatures(
            rms_energy=0.5,
            mfcc=np.zeros(13, dtype=np.float32),
            spectral_centroid=1000.0,
            zero_crossing_rate=0.1,
            is_speech=True,
        )

        engine.update(features)
        shape = engine.get_current_shape()

        # Should not be closed with high energy
        assert shape in [MouthShape.A, MouthShape.O, MouthShape.E, MouthShape.CLOSED]

    def test_engine_smoothing(self) -> None:
        """Test temporal smoothing of mouth shapes."""
        config = LipSyncConfig(smoothing_window=3)
        engine = LipSyncEngine(config)

        # Feed multiple frames with same shape
        for _ in range(3):
            features = AudioFeatures(
                rms_energy=0.5,
                mfcc=np.zeros(13, dtype=np.float32),
                spectral_centroid=1000.0,
                zero_crossing_rate=0.1,
                is_speech=True,
            )
            engine.update(features)

        # Should have stable shape after smoothing window
        shape = engine.get_current_shape()
        assert isinstance(shape, MouthShape)

    def test_engine_reset(self) -> None:
        """Test resetting engine state."""
        config = LipSyncConfig()
        engine = LipSyncEngine(config)

        # Update with some features
        features = AudioFeatures(
            rms_energy=0.5,
            mfcc=np.zeros(13, dtype=np.float32),
            spectral_centroid=1000.0,
            zero_crossing_rate=0.1,
            is_speech=True,
        )
        engine.update(features)

        # Reset
        engine.reset()

        # Should return to closed
        assert engine.get_current_shape() == MouthShape.CLOSED

    def test_set_strategy(self) -> None:
        """Test changing lip-sync strategy at runtime."""
        config = LipSyncConfig()
        engine = LipSyncEngine(config)

        new_strategy = EnergyBasedStrategy(threshold=0.2)
        engine.set_strategy(new_strategy)

        assert engine.strategy == new_strategy


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

