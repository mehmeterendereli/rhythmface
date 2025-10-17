"""
Asset generation module for RhythmFace.

This module provides automatic generation of placeholder character and mouth
assets using Pillow. Assets are generated on first run if not already present.
"""

from rhythmface.assets.generator import ensure_assets_exist, generate_all_assets

__all__ = ["generate_all_assets", "ensure_assets_exist"]
