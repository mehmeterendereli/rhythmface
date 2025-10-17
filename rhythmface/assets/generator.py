"""
Automatic asset generation using Pillow.

This module generates high-quality flat-design PNG assets for the character base
and mouth shapes with a professional 'street rapper vibe' aesthetic.
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
    Generate high-quality flat-design rapper character.

    Professional vector-style design with:
    - Flat colors (minimal gradients)
    - Clean geometric shapes
    - Sharp edges and smooth curves
    - Modern minimalist aesthetic

    Args:
        size: Image dimensions (width, height)
        output_path: Optional path to save PNG

    Returns:
        PIL Image of base character (transparent background)
    """
    # High-res for quality, then scale down with antialiasing
    scale = 2
    hires_size = (size[0] * scale, size[1] * scale)
    img = Image.new("RGBA", hires_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    w, h = hires_size
    cx, cy = w // 2, h // 2

    # Color palette - flat design
    skin_tone = (220, 160, 115)
    skin_shadow = (195, 140, 100)
    hair_color = (60, 40, 30)
    hair_highlight = (80, 55, 42)
    black_shirt = (28, 28, 32)
    shirt_shadow = (18, 18, 22)
    gold_chain = (235, 180, 50)
    gold_dark = (200, 150, 40)
    gold_light = (255, 210, 90)
    glass_frame = (15, 15, 18)
    glass_lens = (25, 25, 30)

    # === TORSO & HOODIE ===
    torso_y = cy + 300
    # Main body shape
    body_points = [
        (cx - 300, h),
        (cx - 200, torso_y),
        (cx - 180, torso_y - 50),
        (cx + 180, torso_y - 50),
        (cx + 200, torso_y),
        (cx + 300, h),
    ]
    draw.polygon(body_points, fill=black_shirt)

    # Hoodie shadow/collar
    collar_points = [
        (cx - 160, torso_y - 30),
        (cx - 120, torso_y - 80),
        (cx + 120, torso_y - 80),
        (cx + 160, torso_y - 30),
    ]
    draw.polygon(collar_points, fill=shirt_shadow)

    # === NECK ===
    neck_y = torso_y - 70
    neck_points = [
        (cx - 80, neck_y - 10),
        (cx - 70, neck_y - 80),
        (cx + 70, neck_y - 80),
        (cx + 80, neck_y - 10),
    ]
    draw.polygon(neck_points, fill=skin_shadow)
    
    # Neck front
    neck_front_points = [
        (cx - 70, neck_y - 10),
        (cx - 60, neck_y - 80),
        (cx + 60, neck_y - 80),
        (cx + 70, neck_y - 10),
    ]
    draw.polygon(neck_front_points, fill=skin_tone)

    # === GOLD CHAIN ===
    chain_y = neck_y + 50
    chain_radius = 30
    chain_positions = []
    
    # Create circular chain
    import math
    for i in range(12):
        angle = (i / 12) * math.pi - math.pi / 2
        x = cx + math.sin(angle) * 140
        y = chain_y + math.cos(angle) * 60 - 30
        chain_positions.append((x, y))
    
    # Draw chain links
    for x, y in chain_positions:
        # Shadow
        draw.ellipse([x - chain_radius + 4, y - chain_radius + 4, 
                     x + chain_radius + 4, y + chain_radius + 4], 
                     fill=gold_dark)
        # Main gold
        draw.ellipse([x - chain_radius, y - chain_radius, 
                     x + chain_radius, y + chain_radius], 
                     fill=gold_chain)
        # Highlight
        draw.ellipse([x - chain_radius // 2, y - chain_radius // 2, 
                     x + chain_radius // 3, y + chain_radius // 3], 
                     fill=gold_light)

    # === HEAD ===
    head_y = cy - 180
    head_w = 190
    head_h = 240

    # Head shape (oval)
    draw.ellipse([cx - head_w, head_y, cx + head_w, head_y + head_h], 
                 fill=skin_tone)
    
    # Face shadow (side)
    draw.ellipse([cx - head_w, head_y, cx - head_w + 40, head_y + head_h], 
                 fill=skin_shadow)

    # === EARS ===
    ear_y = head_y + 100
    ear_w = 35
    ear_h = 60
    
    # Left ear
    draw.ellipse([cx - head_w - 15, ear_y, cx - head_w + ear_w, ear_y + ear_h], 
                 fill=skin_tone)
    # Inner ear detail
    draw.ellipse([cx - head_w - 5, ear_y + 15, cx - head_w + 15, ear_y + 45], 
                 fill=skin_shadow)
    
    # Right ear
    draw.ellipse([cx + head_w - ear_w, ear_y, cx + head_w + 15, ear_y + ear_h], 
                 fill=skin_tone)
    # Inner ear detail
    draw.ellipse([cx + head_w - 15, ear_y + 15, cx + head_w + 5, ear_y + 45], 
                 fill=skin_shadow)

    # === HAIR (SPIKY/WAVY STYLE) ===
    hair_y = head_y - 30
    
    # Hair base
    hair_points = [
        (cx - head_w - 20, hair_y + 100),
        (cx - head_w - 10, hair_y + 50),
        (cx - 140, hair_y + 20),
        (cx - 100, hair_y),
        (cx - 60, hair_y + 10),
        (cx - 20, hair_y + 5),
        (cx + 20, hair_y + 15),
        (cx + 60, hair_y + 20),
        (cx + 100, hair_y + 10),
        (cx + 140, hair_y + 30),
        (cx + head_w - 10, hair_y + 60),
        (cx + head_w, hair_y + 100),
        (cx, hair_y + 80),
    ]
    draw.polygon(hair_points, fill=hair_color)
    
    # Hair highlights (spiky effect)
    highlight_points = [
        (cx - 100, hair_y + 5),
        (cx - 80, hair_y - 5),
        (cx - 60, hair_y + 15),
    ]
    draw.polygon(highlight_points, fill=hair_highlight)
    
    highlight_points2 = [
        (cx - 20, hair_y + 10),
        (cx, hair_y),
        (cx + 20, hair_y + 20),
    ]
    draw.polygon(highlight_points2, fill=hair_highlight)

    # === NOSE ===
    nose_y = head_y + 140
    nose_points = [
        (cx - 15, nose_y),
        (cx, nose_y + 25),
        (cx + 15, nose_y),
    ]
    draw.polygon(nose_points, fill=skin_shadow)

    # === SUNGLASSES (FLAT DESIGN) ===
    glass_y = head_y + 80
    glass_w = 150
    glass_h = 55
    
    # Frame outline (thick)
    frame_thickness = 12
    draw.rounded_rectangle(
        [cx - glass_w - frame_thickness, glass_y - frame_thickness, 
         cx + glass_w + frame_thickness, glass_y + glass_h + frame_thickness],
        radius=15, fill=glass_frame
    )
    
    # Left lens
    draw.rounded_rectangle(
        [cx - glass_w, glass_y, cx - 10, glass_y + glass_h],
        radius=8, fill=glass_lens
    )
    
    # Right lens
    draw.rounded_rectangle(
        [cx + 10, glass_y, cx + glass_w, glass_y + glass_h],
        radius=8, fill=glass_lens
    )
    
    # Bridge
    draw.rectangle([cx - 10, glass_y + 15, cx + 10, glass_y + 35], fill=glass_frame)
    
    # Lens reflection (minimal)
    draw.rounded_rectangle(
        [cx - glass_w + 10, glass_y + 8, cx - 40, glass_y + 25],
        radius=5, fill=(255, 255, 255, 30)
    )
    draw.rounded_rectangle(
        [cx + 40, glass_y + 8, cx + glass_w - 10, glass_y + 25],
        radius=5, fill=(255, 255, 255, 30)
    )
    
    # Temples (side arms)
    draw.line([(cx - glass_w - frame_thickness, glass_y + glass_h // 2), 
               (cx - glass_w - 60, glass_y + glass_h // 2 + 10)], 
              fill=glass_frame, width=frame_thickness)
    draw.line([(cx + glass_w + frame_thickness, glass_y + glass_h // 2), 
               (cx + glass_w + 60, glass_y + glass_h // 2 + 10)], 
              fill=glass_frame, width=frame_thickness)

    # Scale down to target size with high-quality antialiasing
    img = img.resize(size, Image.Resampling.LANCZOS)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_closed(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate closed mouth (flat design style).

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of closed mouth
    """
    scale = 2
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    # Flat design colors
    lip_color = (160, 80, 70)
    lip_dark = (130, 60, 50)

    # Simple horizontal line mouth
    draw.arc([cx - 70, cy - 20, cx + 70, cy + 20], start=0, end=180, 
             fill=lip_dark, width=16)
    draw.arc([cx - 65, cy - 18, cx + 65, cy + 18], start=0, end=180, 
             fill=lip_color, width=12)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_a(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'A' mouth - open oval (flat design).

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of A mouth
    """
    scale = 2
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    # Colors
    mouth_inside = (40, 20, 20)
    lip_color = (160, 80, 70)
    lip_dark = (130, 60, 50)
    teeth = (255, 255, 245)

    mw, mh = 75, 55

    # Mouth cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=mouth_inside)

    # Teeth (upper)
    draw.arc([cx - 65, cy - 45, cx + 65, cy - 5], start=180, end=360, 
             fill=teeth, width=25)

    # Lips outline
    draw.ellipse([cx - mw - 6, cy - mh - 6, cx + mw + 6, cy + mh + 6], 
                 outline=lip_dark, width=14)
    draw.ellipse([cx - mw - 2, cy - mh - 2, cx + mw + 2, cy + mh + 2], 
                 outline=lip_color, width=8)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_o(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'O' mouth - round open (flat design).

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of O mouth
    """
    scale = 2
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    # Colors
    mouth_inside = (40, 20, 20)
    lip_color = (160, 80, 70)
    lip_dark = (130, 60, 50)

    r = 50

    # Mouth cavity (perfect circle)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=mouth_inside)

    # Lips outline (circular)
    draw.ellipse([cx - r - 6, cy - r - 6, cx + r + 6, cy + r + 6], 
                 outline=lip_dark, width=14)
    draw.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], 
                 outline=lip_color, width=8)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_e(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate 'E' mouth - wide smile (flat design).

    Args:
        size: Image dimensions
        output_path: Optional path to save PNG

    Returns:
        PIL Image of E mouth
    """
    scale = 2
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    # Colors
    mouth_inside = (40, 20, 20)
    lip_color = (160, 80, 70)
    lip_dark = (130, 60, 50)
    teeth = (255, 255, 245)

    mw, mh = 115, 35

    # Mouth cavity (wide horizontal)
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=mouth_inside)

    # Teeth (visible top)
    draw.rounded_rectangle([cx - 100, cy - 28, cx + 100, cy + 5], 
                          radius=8, fill=teeth)
    
    # Tooth separations (subtle)
    for i in range(-3, 4):
        tx = cx + i * 28
        draw.line([(tx, cy - 28), (tx, cy + 5)], fill=(245, 245, 235), width=3)

    # Lips outline
    draw.ellipse([cx - mw - 6, cy - mh - 6, cx + mw + 6, cy + mh + 6], 
                 outline=lip_dark, width=12)
    draw.ellipse([cx - mw - 2, cy - mh - 2, cx + mw + 2, cy + mh + 2], 
                 outline=lip_color, width=7)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_all_assets(force: bool = False) -> None:
    """
    Generate all high-quality flat-design assets.

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
            print(f"Generating high-quality asset: {filename}")
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
    print("High-quality asset generation complete!")
