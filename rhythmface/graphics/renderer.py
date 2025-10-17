"""
Pygame-based renderer for 2D character animation.

This module provides the Renderer class for displaying the character
and animating mouth movements in real-time.
"""

from abc import ABC, abstractmethod
from pathlib import Path

import pygame

from rhythmface.config import GraphicsConfig
from rhythmface.logic.lipsync_engine import MouthShape


class IRenderer(ABC):
    """
    Abstract interface for renderers.

    Allows different rendering backends (pygame, OpenGL, web canvas, etc.)
    following the Strategy pattern.
    """

    @abstractmethod
    def initialize(self) -> None:
        """Initialize rendering system."""
        pass

    @abstractmethod
    def render_frame(self, mouth_shape: MouthShape) -> None:
        """
        Render a single frame with given mouth shape.

        Args:
            mouth_shape: Current mouth shape to display
        """
        pass

    @abstractmethod
    def handle_events(self) -> bool:
        """
        Process window events.

        Returns:
            True if should continue running, False to quit
        """
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """Cleanup resources."""
        pass


class Renderer(IRenderer):
    """
    Pygame-based renderer for character animation.

    This class manages the pygame window, loads assets, and composites
    the base character image with the appropriate mouth shape each frame.

    The renderer maintains its own timing loop to ensure consistent FPS
    independent of the audio/logic processing rate.

    Example:
        >>> from rhythmface.config import GraphicsConfig
        >>> from rhythmface.logic.lipsync_engine import MouthShape
        >>> config = GraphicsConfig()
        >>> renderer = Renderer(config)
        >>> renderer.initialize()
        >>> while renderer.handle_events():
        ...     renderer.render_frame(MouthShape.A)
        >>> renderer.cleanup()
    """

    def __init__(self, config: GraphicsConfig) -> None:
        """
        Initialize renderer with configuration.

        Args:
            config: Graphics configuration
        """
        self.config = config
        self.window: pygame.Surface | None = None
        self.clock: pygame.time.Clock | None = None

        # Asset surfaces
        self.base_image: pygame.Surface | None = None
        self.mouth_images: dict[MouthShape, pygame.Surface] = {}

        # Asset paths
        self.assets_dir = Path(__file__).parent.parent / "assets"

        # State
        self.initialized = False

    def initialize(self) -> None:
        """
        Initialize pygame and load assets.

        Raises:
            RuntimeError: If pygame initialization fails
            FileNotFoundError: If required assets are missing
        """
        pygame.init()

        # Create display window
        flags = 0
        if self.config.fullscreen:
            flags = pygame.FULLSCREEN
        self.window = pygame.display.set_mode(
            (self.config.window_width, self.config.window_height),
            flags
        )

        # Set window title
        pygame.display.set_caption(self.config.window_title)

        # Create clock for FPS control
        self.clock = pygame.time.Clock()

        # Load assets
        self._load_assets()

        self.initialized = True

    def _load_assets(self) -> None:
        """
        Load character and mouth images from assets directory.

        Raises:
            FileNotFoundError: If asset files are missing
        """
        # Load base character image
        base_path = self.assets_dir / "base.png"
        if not base_path.exists():
            raise FileNotFoundError(f"Base image not found: {base_path}")
        self.base_image = pygame.image.load(str(base_path)).convert_alpha()

        # Load mouth shape images
        for shape in MouthShape:
            mouth_path = self.assets_dir / f"mouth_{shape.value}.png"
            if not mouth_path.exists():
                raise FileNotFoundError(f"Mouth image not found: {mouth_path}")
            self.mouth_images[shape] = pygame.image.load(str(mouth_path)).convert_alpha()

    def render_frame(self, mouth_shape: MouthShape) -> None:
        """
        Render a single frame with the given mouth shape.

        This composites the base character with the appropriate mouth
        image and displays it in the window.

        Args:
            mouth_shape: Mouth shape to render
        """
        if not self.initialized or self.window is None:
            return

        # Clear screen with background color
        self.window.fill(self.config.background_color)

        # Draw base character image (centered)
        if self.base_image:
            base_rect = self.base_image.get_rect(center=self.window.get_rect().center)
            self.window.blit(self.base_image, base_rect)

        # Draw mouth shape overlay (positioned on character)
        if mouth_shape in self.mouth_images:
            mouth_img = self.mouth_images[mouth_shape]
            mouth_rect = mouth_img.get_rect(center=(
                self.window.get_rect().centerx,
                self.window.get_rect().centery + 50  # Adjust Y offset for mouth position
            ))
            self.window.blit(mouth_img, mouth_rect)

        # Update display
        pygame.display.flip()

        # Maintain FPS
        if self.clock:
            self.clock.tick(30)

    def handle_events(self) -> bool:
        """
        Process pygame events (keyboard, mouse, window close).

        Returns:
            True to continue running, False to quit
        """
        if not self.initialized:
            return False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_f:
                    # Toggle fullscreen
                    pygame.display.toggle_fullscreen()

        return True

    def cleanup(self) -> None:
        """Cleanup pygame resources."""
        pygame.quit()
        self.initialized = False

    def get_fps(self) -> float:
        """
        Get current rendering FPS.

        Returns:
            Current frames per second
        """
        if self.clock:
            return self.clock.get_fps()
        return 0.0

    def set_window_title(self, title: str) -> None:
        """
        Update window title (useful for showing FPS, etc.).

        Args:
            title: New window title
        """
        if self.initialized:
            pygame.display.set_caption(title)
