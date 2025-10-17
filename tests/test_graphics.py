"""
Tests for graphics module (pygame renderer).
"""

import pytest

from rhythmface.config import GraphicsConfig
from rhythmface.graphics.renderer import Renderer
from rhythmface.logic.lipsync_engine import MouthShape


class TestRenderer:
    """Test Renderer class."""

    def test_renderer_initialization(self) -> None:
        """Test renderer can be initialized with config."""
        config = GraphicsConfig()
        renderer = Renderer(config)

        assert renderer.config == config
        assert not renderer.initialized

    def test_renderer_asset_paths(self) -> None:
        """Test asset directory path is set correctly."""
        config = GraphicsConfig()
        renderer = Renderer(config)

        assert renderer.assets_dir.exists()
        assert renderer.assets_dir.name == "assets"

    def test_renderer_initialize(self) -> None:
        """Test renderer initialization (smoke test)."""
        config = GraphicsConfig()
        renderer = Renderer(config)

        # This is a placeholder test - actual pygame init would require display
        renderer.initialize()
        assert renderer.initialized

    def test_renderer_render_frame(self) -> None:
        """Test rendering a frame (smoke test)."""
        config = GraphicsConfig()
        renderer = Renderer(config)
        renderer.initialize()

        # Should not crash even with placeholder implementation
        renderer.render_frame(MouthShape.CLOSED)
        renderer.render_frame(MouthShape.A)

    def test_renderer_handle_events(self) -> None:
        """Test event handling (smoke test)."""
        config = GraphicsConfig()
        renderer = Renderer(config)
        renderer.initialize()

        # Should return True to continue running (placeholder)
        result = renderer.handle_events()
        assert isinstance(result, bool)

    def test_renderer_cleanup(self) -> None:
        """Test renderer cleanup."""
        config = GraphicsConfig()
        renderer = Renderer(config)
        renderer.initialize()

        renderer.cleanup()
        assert not renderer.initialized

    def test_renderer_get_fps(self) -> None:
        """Test FPS getter."""
        config = GraphicsConfig()
        renderer = Renderer(config)
        renderer.initialize()

        fps = renderer.get_fps()
        assert isinstance(fps, float)
        assert fps >= 0.0

    def test_renderer_set_window_title(self) -> None:
        """Test setting window title."""
        config = GraphicsConfig()
        renderer = Renderer(config)
        renderer.initialize()

        # Should not crash
        renderer.set_window_title("Test Title")


class TestRendererIntegration:
    """Integration tests for renderer."""

    def test_full_render_cycle(self) -> None:
        """Test complete render cycle (smoke test)."""
        config = GraphicsConfig()
        renderer = Renderer(config)

        renderer.initialize()

        # Render a few frames with different mouth shapes
        shapes = [MouthShape.CLOSED, MouthShape.A, MouthShape.O, MouthShape.E]
        for shape in shapes:
            renderer.render_frame(shape)
            should_continue = renderer.handle_events()
            assert isinstance(should_continue, bool)

        renderer.cleanup()
        assert not renderer.initialized


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

