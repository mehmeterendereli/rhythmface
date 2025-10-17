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
    Generate premium quality rapper character avatar.

    Professional vector-style design with:
    - Smooth gradients and shading
    - Designer accessories
    - Perfect proportions
    - Modern minimalist aesthetic

    Args:
        size: Image dimensions (width, height)
        output_path: Optional path to save PNG

    Returns:
        PIL Image of base character (transparent background)
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    w, h = size
    cx, cy = w // 2, h // 2

    # === TORSO & CLOTHING ===
    # Black hoodie/jacket
    torso_y = cy + 150
    draw.polygon(
        [(cx - 150, h), (cx - 100, torso_y), (cx + 100, torso_y), (cx + 150, h)],
        fill=(28, 28, 32, 255),
    )

    # Hoodie shadow detail
    draw.polygon(
        [(cx - 95, torso_y + 10), (cx - 70, torso_y), (cx + 70, torso_y), (cx + 95, torso_y + 10)],
        fill=(18, 18, 22, 255),
    )

    # === PREMIUM GOLD CHAIN ===
    chain_y = torso_y + 35
    chain_width = 110

    # Chain links with depth
    for i in range(8):
        t = i / 7
        x = cx + (t - 0.5) * chain_width
        y = chain_y + (1 - abs(2 * t - 1)) * 12

        # Shadow
        draw.ellipse([x - 14, y - 13 + 2, x + 14, y + 13 + 2], fill=(180, 140, 0, 100))

        # Gold link
        draw.ellipse([x - 14, y - 13, x + 14, y + 13], fill=(255, 220, 60, 255), outline=(220, 180, 30, 255), width=2)

        # Highlight
        draw.ellipse([x - 8, y - 8, x + 3, y + 3], fill=(255, 245, 200, 180))

    # === NECK ===
    neck_y = torso_y - 10
    # Neck shadow
    draw.ellipse([cx - 43, neck_y - 42, cx + 43, neck_y + 18], fill=(130, 90, 65, 255))
    # Neck main
    draw.ellipse([cx - 40, neck_y - 45, cx + 40, neck_y + 15], fill=(210, 150, 110, 255))

    # === HEAD (REALISTIC PROPORTIONS) ===
    head_y = cy - 90
    head_w = 95
    head_h = 120

    # Drop shadow
    draw.ellipse([cx - head_w + 5, head_y + 5, cx + head_w + 5, head_y + head_h + 5], fill=(0, 0, 0, 40))

    # Face gradient (darker on edges)
    draw.ellipse([cx - head_w, head_y, cx + head_w, head_y + head_h], fill=(210, 150, 110, 255))

    # Face contour
    draw.ellipse([cx - head_w, head_y, cx + head_w, head_y + head_h], outline=(180, 130, 90, 255), width=3)

    # Cheek highlights
    draw.ellipse([cx - 55, head_y + 55, cx - 30, head_y + 75], fill=(230, 170, 130, 80))
    draw.ellipse([cx + 30, head_y + 55, cx + 55, head_y + 75], fill=(230, 170, 130, 80))

    # === EARS (DETAILED) ===
    ear_y = head_y + 52
    ear_w = 22
    ear_h = 38

    # Left ear
    draw.ellipse([cx - head_w - 8, ear_y, cx - head_w + ear_w - 8, ear_y + ear_h], fill=(200, 140, 100, 255), outline=(170, 120, 85, 255), width=2)
    draw.ellipse([cx - head_w - 3, ear_y + 12, cx - head_w + 10, ear_y + 26], fill=(180, 125, 90, 150))

    # Right ear
    draw.ellipse([cx + head_w - ear_w + 8, ear_y, cx + head_w + 8, ear_y + ear_h], fill=(200, 140, 100, 255), outline=(170, 120, 85, 255), width=2)
    draw.ellipse([cx + head_w - 10, ear_y + 12, cx + head_w + 3, ear_y + 26], fill=(180, 125, 90, 150))

    # === PREMIUM SNAPBACK CAP ===
    cap_y = head_y - 35

    # Cap shadow
    draw.ellipse([cx - 108, cap_y, cx + 108, cap_y + 58], fill=(12, 12, 15, 255))

    # Cap main body
    draw.ellipse([cx - 105, cap_y, cx + 105, cap_y + 55], fill=(22, 22, 26, 255), outline=(40, 40, 44, 255), width=3)

    # Brim (curved realistic)
    brim_points = [
        (cx - 120, cap_y + 42),
        (cx - 100, cap_y + 52),
        (cx + 70, cap_y + 52),
        (cx + 85, cap_y + 42),
        (cx + 70, cap_y + 45),
        (cx - 100, cap_y + 45),
    ]
    draw.polygon(brim_points, fill=(18, 18, 22, 255), outline=(35, 35, 39, 255), width=2)

    # Premium logo badge
    logo_x, logo_y = cx - 5, cap_y + 20
    draw.ellipse([logo_x - 26, logo_y, logo_x + 26, logo_y + 42], fill=(245, 245, 248, 255), outline=(200, 200, 203, 255), width=2)

    # Logo shadow
    draw.ellipse([logo_x - 15, logo_y + 28, logo_x + 15, logo_y + 35], fill=(180, 180, 185, 100))

    # === DESIGNER SUNGLASSES ===
    glass_y = head_y + 42
    lens_h = 34

    # Frame shadow
    draw.rounded_rectangle([cx - 82, glass_y + 2, cx + 82, glass_y + lens_h + 2], radius=10, fill=(0, 0, 0, 40))

    # Frame main
    draw.rounded_rectangle([cx - 80, glass_y, cx + 80, glass_y + lens_h], radius=10, fill=(22, 22, 26, 255), outline=(40, 40, 44, 255), width=3)

    # Left lens
    draw.rounded_rectangle([cx - 75, glass_y + 2, cx - 5, glass_y + lens_h - 2], radius=8, fill=(0, 0, 0, 255))

    # Right lens
    draw.rounded_rectangle([cx + 5, glass_y + 2, cx + 75, glass_y + lens_h - 2], radius=8, fill=(0, 0, 0, 255))

    # Bridge
    draw.rectangle([cx - 5, glass_y + 10, cx + 5, glass_y + 20], fill=(22, 22, 26, 255))

    # Lens highlights (glossy reflection)
    draw.arc([cx - 70, glass_y + 5, cx - 50, glass_y + 25], start=30, end=120, fill=(255, 255, 255, 60), width=4)
    draw.arc([cx + 50, glass_y + 5, cx + 70, glass_y + 25], start=30, end=120, fill=(255, 255, 255, 60), width=4)

    # Additional frame details (side arms hint)
    draw.line([(cx - 80, glass_y + lens_h // 2), (cx - 100, glass_y + lens_h // 2 + 5)], fill=(22, 22, 26, 255), width=4)
    draw.line([(cx + 80, glass_y + lens_h // 2), (cx + 100, glass_y + lens_h // 2 + 5)], fill=(22, 22, 26, 255), width=4)

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

    cx, cy = size[0] // 2, size[1] // 2

    # Closed lips with slight curve
    draw.arc([cx - 35, cy - 10, cx + 35, cy + 10], start=0, end=180, fill=(140, 65, 55, 255), width=8)

    # Upper lip shading
    draw.arc([cx - 32, cy - 8, cx + 32, cy + 2], start=0, end=180, fill=(160, 75, 65, 255), width=4)

    # Lower lip shading
    draw.arc([cx - 32, cy - 2, cx + 32, cy + 8], start=0, end=180, fill=(155, 72, 62, 230), width=4)

    # Highlight for glossy effect
    draw.arc([cx - 25, cy - 12, cx + 25, cy - 2], start=0, end=180, fill=(190, 100, 85, 140), width=3)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_a(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'A' mouth - open for "ah" sound.

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of A mouth
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = size[0] // 2, size[1] // 2
    mw, mh = 40, 30  # Slightly taller for 'A' sound

    # Mouth cavity shadow
    draw.ellipse([cx - mw + 2, cy - mh + 2, cx + mw + 2, cy + mh + 2], fill=(25, 10, 10, 150))

    # Mouth cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=(35, 15, 15, 255))

    # Tongue
    draw.ellipse([cx - 30, cy + 5, cx + 30, cy + 25], fill=(180, 80, 80, 255), outline=(160, 70, 70, 255), width=2)

    # Upper teeth
    draw.rounded_rectangle([cx - 35, cy - 25, cx + 35, cy - 5], radius=4, fill=(248, 248, 238, 255), outline=(230, 230, 220, 255), width=2)

    # Lower teeth hint
    draw.ellipse([cx - 30, cy + 10, cx + 30, cy + 22], fill=(243, 243, 233, 255), outline=(225, 225, 215, 255), width=1)

    # Outer lips
    draw.ellipse([cx - mw - 5, cy - mh - 5, cx + mw + 5, cy + mh + 5], outline=(140, 65, 55, 255), width=7)

    # Lip shading (top)
    draw.arc([cx - mw - 3, cy - mh - 8, cx + mw + 3, cy + 8], start=180, end=360, fill=(160, 75, 65, 255), width=8)

    # Lip shading (bottom)
    draw.arc([cx - mw - 3, cy - 5, cx + mw + 3, cy + mh + 5], start=0, end=180, fill=(155, 72, 62, 230), width=7)

    # Lip highlight
    draw.arc([cx - 30, cy - mh - 5, cx + 30, cy - 5], start=180, end=360, fill=(190, 100, 85, 140), width=4)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_o(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'O' mouth - round open for "oh" sound.

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of O mouth
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = size[0] // 2, size[1] // 2
    r = 25  # Round shape

    # Mouth cavity shadow
    draw.ellipse([cx - r + 2, cy - r + 2, cx + r + 2, cy + r + 2], fill=(25, 10, 10, 150))

    # Mouth cavity
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(35, 15, 15, 255))

    # Tongue/throat hint
    draw.ellipse([cx - 12, cy + 8, cx + 12, cy + 22], fill=(160, 70, 70, 150))

    # Upper teeth (slight visibility)
    draw.arc([cx - 22, cy - 24, cx + 22, cy - 5], start=180, end=360, fill=(240, 240, 230, 180), width=6)

    # Outer lips (perfect circle)
    draw.ellipse([cx - r - 6, cy - r - 6, cx + r + 6, cy + r + 6], outline=(140, 65, 55, 255), width=7)

    # Lip shading (top)
    draw.arc([cx - r - 3, cy - r - 8, cx + r + 3, cy + r - 8], start=180, end=360, fill=(160, 75, 65, 255), width=8)

    # Lip shading (bottom)
    draw.arc([cx - r - 3, cy - r + 8, cx + r + 3, cy + r + 8], start=0, end=180, fill=(155, 72, 62, 230), width=7)

    # Lip highlight (glossy effect)
    draw.arc([cx - 20, cy - r - 5, cx + 20, cy - 5], start=180, end=360, fill=(190, 100, 85, 140), width=4)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_e(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'E' mouth - wide smile for "eh" sound.

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of E mouth
    """
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = size[0] // 2, size[1] // 2

    # Wide horizontal smile
    mw, mh = 58, 20

    # Mouth cavity shadow
    draw.ellipse([cx - mw + 2, cy - mh + 2, cx + mw + 2, cy + mh + 2], fill=(25, 10, 10, 150))

    # Mouth cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=(35, 15, 15, 255))

    # Upper teeth (prominent)
    draw.rounded_rectangle([cx - 52, cy - 16, cx + 52, cy + 4], radius=4, fill=(248, 248, 238, 255), outline=(230, 230, 220, 255), width=2)

    # Individual teeth
    for i in range(-4, 5):
        tx = cx + i * 12
        draw.line([(tx, cy - 16), (tx, cy + 4)], fill=(235, 235, 225, 255), width=2)
        # Tooth shine
        draw.rectangle([tx - 4, cy - 15, tx - 1, cy - 8], fill=(255, 255, 250, 120))

    # Lower teeth hint
    draw.ellipse([cx - 48, cy + 5, cx + 48, cy + 17], fill=(243, 243, 233, 255), outline=(225, 225, 215, 255), width=1)

    # Tongue hint
    draw.ellipse([cx - 40, cy + 8, cx + 40, cy + 16], fill=(180, 80, 80, 100))

    # Outer lips (smiling shape)
    draw.ellipse([cx - mw - 5, cy - mh - 5, cx + mw + 5, cy + mh + 5], outline=(140, 65, 55, 255), width=6)

    # Upper lip (smile curve)
    draw.arc([cx - mw - 3, cy - mh - 8, cx + mw + 3, cy + 8], start=180, end=360, fill=(160, 75, 65, 255), width=7)

    # Lower lip
    draw.arc([cx - mw + 5, cy - 5, cx + mw - 5, cy + mh + 5], start=0, end=180, fill=(155, 70, 60, 240), width=6)

    # Lip shine (upper)
    draw.arc([cx - 45, cy - mh - 5, cx + 45, cy - 5], start=180, end=360, fill=(190, 100, 85, 130), width=3)

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
