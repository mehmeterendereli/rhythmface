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
        self.character_scale = 1.0  # Dynamic scale factor for character sizing

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
        """Load PNG assets from disk."""
        assets_dir = Path(__file__).parent.parent / "assets"

        # Load base character
        base_path = assets_dir / "base.png"
        if base_path.exists():
            self.base_image = pygame.image.load(base_path).convert_alpha()
            
            # SCALE character to fit window dynamically (80% of window)
            # Window is 640x640, so character will be ~512x512
            target_size = int(self.config.window_width * 0.8)
            self.base_image = pygame.transform.smoothscale(
                self.base_image,
                (target_size, target_size)
            )
            self.character_scale = target_size / 512.0  # Scale factor for mouth positioning
        else:
            print(f"Warning: base.png not found at {base_path}")

        # Load mouth shapes (these stay standard size, will be scaled relative to character)
        mouth_files = {
            MouthShape.CLOSED: "mouth_closed.png",
            MouthShape.A: "mouth_A.png",
            MouthShape.O: "mouth_O.png",  # noqa: E741
            MouthShape.E: "mouth_E.png",
        }

        for shape, filename in mouth_files.items():
            mouth_path = assets_dir / filename
            if mouth_path.exists():
                mouth_img = pygame.image.load(mouth_path).convert_alpha()
                self.mouth_images[shape] = mouth_img
            else:
                print(f"Warning: {filename} not found at {mouth_path}")

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

        # Draw mouth shape overlay (positioned on character's face)
        if mouth_shape in self.mouth_images:
            mouth_img = self.mouth_images[mouth_shape]
            
            # Scale mouth proportionally - smaller for larger character
            # Base scale: 1.2x (was 2.0x), adjusted by character_scale factor
            mouth_scale = 1.2 * self.character_scale
            mouth_scaled = pygame.transform.smoothscale(
                mouth_img,
                (int(mouth_img.get_width() * mouth_scale), 
                 int(mouth_img.get_height() * mouth_scale))
            )
            
            # Position mouth dynamically - HIGHER on character
            # Y offset scales with character size (was 75, now 40)
            mouth_y_offset = int(40 * self.character_scale)
            mouth_rect = mouth_scaled.get_rect(center=(
                self.window.get_rect().centerx,
                self.window.get_rect().centery + mouth_y_offset
            ))
            self.window.blit(mouth_scaled, mouth_rect)

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
