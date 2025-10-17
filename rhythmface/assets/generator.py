"""
Automatic asset generation using Pillow.

This module generates placeholder PNG assets for the character base
and mouth shapes with a 'street rapper vibe' aesthetic.
"""

from pathlib import Path

from PIL import Image, ImageDraw


def get_assets_dir() -> Path:
    """
    Get the assets directory path.

    Returns:
        Path to assets directory
    """
    return Path(__file__).parent


def generate_base_character(
    size: tuple[int, int] = (512, 512),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate base character silhouette with 'rapper vibe' aesthetic.

    Creates a stylized character silhouette with:
    - Head/body outline
    - Cap/headwear
    - Space for mouth overlay

    Args:
        size: Image dimensions (width, height)
        output_path: Optional path to save PNG

    Returns:
        PIL Image of base character
    """
    # TODO: Implement character generation
    # 1. Create transparent image
    # 2. Draw character silhouette (head, shoulders, cap)
    # 3. Use 'street' color palette (dark tones, gold accents)
    # 4. Leave mouth area blank for overlay
    # 5. Add style elements (chains, sunglasses, etc.)

    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Placeholder: Simple head circle
    center_x, center_y = size[0] // 2, size[1] // 2
    head_radius = size[0] // 3

    # Draw head (dark skin tone)
    draw.ellipse(
        [
            center_x - head_radius,
            center_y - head_radius,
            center_x + head_radius,
            center_y + head_radius,
        ],
        fill=(139, 90, 60, 255),  # Skin tone
        outline=(80, 50, 30, 255),
        width=3,
    )

    # Draw cap/hat (placeholder)
    cap_y = center_y - head_radius
    draw.rectangle(
        [
            center_x - head_radius - 20,
            cap_y - 60,
            center_x + head_radius + 20,
            cap_y + 10,
        ],
        fill=(20, 20, 20, 255),  # Black cap
        outline=(10, 10, 10, 255),
        width=2,
    )

    # Draw sunglasses placeholder
    glasses_y = center_y - 20
    draw.rectangle(
        [center_x - 60, glasses_y, center_x - 10, glasses_y + 25],
        fill=(10, 10, 10, 255),
    )
    draw.rectangle(
        [center_x + 10, glasses_y, center_x + 60, glasses_y + 25],
        fill=(10, 10, 10, 255),
    )

    # Erase mouth area (for overlay)
    mouth_y = center_y + 40
    draw.ellipse(
        [
            center_x - 50,
            mouth_y - 15,
            center_x + 50,
            mouth_y + 15,
        ],
        fill=(0, 0, 0, 0),  # Transparent
    )

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_closed(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate closed mouth shape.

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of closed mouth
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center_x, center_y = size[0] // 2, size[1] // 2

    # Draw closed mouth line
    draw.line(
        [
            (center_x - 40, center_y),
            (center_x + 40, center_y),
        ],
        fill=(80, 40, 40, 255),
        width=4,
    )

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_a(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'A' mouth shape (open, low vowel).

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of A mouth
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center_x, center_y = size[0] // 2, size[1] // 2

    # Draw open mouth (oval)
    draw.ellipse(
        [
            center_x - 35,
            center_y - 25,
            center_x + 35,
            center_y + 25,
        ],
        fill=(50, 20, 20, 255),  # Dark interior
        outline=(100, 50, 50, 255),  # Lips
        width=3,
    )

    # Add teeth hint
    draw.ellipse(
        [
            center_x - 25,
            center_y - 20,
            center_x + 25,
            center_y - 5,
        ],
        fill=(220, 220, 200, 200),  # Teeth
    )

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_o(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'O' mouth shape (rounded, back vowel).

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of O mouth
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center_x, center_y = size[0] // 2, size[1] // 2

    # Draw rounded mouth (circle)
    draw.ellipse(
        [
            center_x - 30,
            center_y - 30,
            center_x + 30,
            center_y + 30,
        ],
        fill=(50, 20, 20, 255),
        outline=(100, 50, 50, 255),
        width=4,
    )

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_e(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'E' mouth shape (wide, front vowel).

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of E mouth
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    center_x, center_y = size[0] // 2, size[1] // 2

    # Draw wide mouth
    draw.ellipse(
        [
            center_x - 50,
            center_y - 15,
            center_x + 50,
            center_y + 15,
        ],
        fill=(50, 20, 20, 255),
        outline=(100, 50, 50, 255),
        width=3,
    )

    # Add teeth
    draw.rectangle(
        [
            center_x - 40,
            center_y - 10,
            center_x + 40,
            center_y + 2,
        ],
        fill=(220, 220, 200, 200),
    )

    if output_path:
        img.save(output_path)

    return img


def generate_all_assets(force: bool = False) -> None:
    """
    Generate all placeholder assets.

    Creates base character and all mouth shapes in the assets directory.

    Args:
        force: If True, regenerate even if files exist
    """
    assets_dir = get_assets_dir()
    assets_dir.mkdir(exist_ok=True)

    # Define assets to generate
    assets = [
        ("base.png", generate_base_character, (512, 512)),
        ("mouth_closed.png", generate_mouth_closed, (256, 128)),
        ("mouth_A.png", generate_mouth_a, (256, 128)),
        ("mouth_O.png", generate_mouth_o, (256, 128)),
        ("mouth_E.png", generate_mouth_e, (256, 128)),
    ]

    for filename, generator_func, size in assets:
        output_path = assets_dir / filename

        if force or not output_path.exists():
            print(f"Generating asset: {filename}")
            generator_func(size=size, output_path=output_path)
        else:
            print(f"Asset already exists: {filename}")


def ensure_assets_exist() -> bool:
    """
    Check if all required assets exist, generate if missing.

    Returns:
        True if all assets exist or were generated successfully
    """
    required_assets = [
        "base.png",
        "mouth_closed.png",
        "mouth_A.png",
        "mouth_O.png",
        "mouth_E.png",
    ]

    assets_dir = get_assets_dir()
    missing = [asset for asset in required_assets if not (assets_dir / asset).exists()]

    if missing:
        print(f"Missing assets: {', '.join(missing)}")
        print("Generating missing assets...")
        generate_all_assets()
        return True

    return True


if __name__ == "__main__":
    # Allow running as script to regenerate assets
    import sys

    force = "--force" in sys.argv
    generate_all_assets(force=force)
    print("Asset generation complete!")
