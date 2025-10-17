"""
Lip-sync engine for analyzing audio and determining mouth shapes.

This module implements the core lip-sync logic, including vowel detection,
mouth shape selection, and temporal smoothing.
"""

from abc import ABC, abstractmethod
from collections import deque
from enum import Enum
from typing import Deque, Optional

import numpy as np
import numpy.typing as npt

from rhythmface.audio.mic_listener import AudioFeatures
from rhythmface.config import LipSyncConfig


class MouthShape(Enum):
    """
    Available mouth shapes for animation.

    These correspond to the PNG assets in rhythmface/assets/:
    - CLOSED: Default closed mouth (rest position)
    - A: Open mouth for 'ah' sound (low vowels)
    - O: Rounded mouth for 'oh' sound (mid-back vowels)
    - E: Wide mouth for 'eh' sound (mid-front vowels)
    """

    CLOSED = "closed"
    A = "A"
    O = "O"
    E = "E"


class ILipSyncStrategy(ABC):
    """
    Abstract interface for lip-sync strategies.

    This allows different lip-sync algorithms to be plugged in:
    - Simple energy-based
    - MFCC-based vowel detection
    - ML model-based (future)
    - Formant analysis (future)
    """

    @abstractmethod
    def analyze(self, features: AudioFeatures) -> MouthShape:
        """
        Analyze audio features and determine mouth shape.

        Args:
            features: Extracted audio features

        Returns:
            Recommended mouth shape
        """
        pass


class EnergyBasedStrategy(ILipSyncStrategy):
    """
    Simple energy-based lip-sync strategy.

    Uses RMS energy thresholds to determine when mouth should be open.
    Good for testing but not phonetically accurate.
    """

    def __init__(self, threshold: float) -> None:
        """
        Initialize strategy.

        Args:
            threshold: Energy threshold for mouth opening
        """
        self.threshold = threshold

    def analyze(self, features: AudioFeatures) -> MouthShape:
        """
        Analyze audio features using energy thresholds.

        Args:
            features: Audio features

        Returns:
            MouthShape.CLOSED if energy below threshold, MouthShape.A otherwise
        """
        if features.rms_energy > self.threshold:
            return MouthShape.A
        return MouthShape.CLOSED


class MFCCBasedStrategy(ILipSyncStrategy):
    """
    MFCC-based vowel detection strategy.

    Uses MFCC coefficients to classify vowel sounds and select
    appropriate mouth shapes. More accurate than energy-based.
    """

    def __init__(self, energy_threshold: float) -> None:
        """
        Initialize strategy.

        Args:
            energy_threshold: Minimum energy for speech detection
        """
        self.energy_threshold = energy_threshold

    def analyze(self, features: AudioFeatures) -> MouthShape:
        """
        Analyze MFCC features to detect vowel type.

        Args:
            features: Audio features with MFCC

        Returns:
            Appropriate MouthShape based on vowel classification
        """
        # TODO: Implement vowel classification logic
        # 1. Check if speech is present (energy threshold)
        # 2. Analyze MFCC coefficients for vowel characteristics
        # 3. Classify as A (low), O (back), or E (front) vowel
        # 4. Return appropriate mouth shape

        if not features.is_speech:
            return MouthShape.CLOSED

        # Placeholder logic
        return MouthShape.A


class LipSyncEngine:
    """
    Main lip-sync engine coordinating audio analysis and mouth shape selection.

    This class manages the lip-sync pipeline:
    1. Receives audio features from MicListener
    2. Applies lip-sync strategy to determine mouth shape
    3. Smooths results over time to avoid jitter
    4. Provides current mouth shape to renderer

    The engine uses the Strategy pattern to allow different lip-sync
    algorithms, and includes temporal smoothing for natural animation.

    Example:
        >>> from rhythmface.config import LipSyncConfig
        >>> config = LipSyncConfig(fps=30, formant_detection=True)
        >>> engine = LipSyncEngine(config)
        >>> features = audio_listener.get_latest_features()
        >>> if features:
        ...     engine.update(features)
        >>> current_shape = engine.get_current_shape()
    """

    def __init__(self, config: LipSyncConfig) -> None:
        """
        Initialize lip-sync engine.

        Args:
            config: Lip-sync configuration
        """
        self.config = config

        # Select strategy based on configuration
        if config.formant_detection:
            self.strategy: ILipSyncStrategy = MFCCBasedStrategy(0.05)
        else:
            self.strategy = EnergyBasedStrategy(0.05)

        # Smoothing buffer for temporal consistency
        self._shape_history: Deque[MouthShape] = deque(
            maxlen=config.smoothing_window
        )
        self._current_shape: MouthShape = MouthShape.CLOSED

    def update(self, features: AudioFeatures) -> None:
        """
        Update engine with new audio features.

        This should be called for each audio analysis frame.

        Args:
            features: Latest audio features from MicListener
        """
        # Analyze features with current strategy
        detected_shape = self.strategy.analyze(features)

        # Add to history buffer
        self._shape_history.append(detected_shape)

        # Update current shape with smoothing
        self._current_shape = self._smooth_shapes()

    def get_current_shape(self) -> MouthShape:
        """
        Get current mouth shape for rendering.

        Returns:
            Current smoothed mouth shape
        """
        return self._current_shape

    def _smooth_shapes(self) -> MouthShape:
        """
        Apply temporal smoothing to mouth shape history.

        Uses mode (most common) shape in recent history to reduce jitter.

        Returns:
            Smoothed mouth shape
        """
        if not self._shape_history:
            return MouthShape.CLOSED

        # TODO: Implement more sophisticated smoothing
        # Current: Simple mode (most frequent)
        # Future: Weighted average, hysteresis, transition rules

        # Count occurrences of each shape
        shape_counts: dict[MouthShape, int] = {}
        for shape in self._shape_history:
            shape_counts[shape] = shape_counts.get(shape, 0) + 1

        # Return most common shape
        return max(shape_counts.keys(), key=lambda s: shape_counts[s])

    def set_strategy(self, strategy: ILipSyncStrategy) -> None:
        """
        Change lip-sync strategy at runtime (plugin system).

        Args:
            strategy: New lip-sync strategy to use
        """
        self.strategy = strategy

    def reset(self) -> None:
        """Reset engine state (clear history, return to closed mouth)."""
        self._shape_history.clear()
        self._current_shape = MouthShape.CLOSED

