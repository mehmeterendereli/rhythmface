"""
Automatic asset generation using Pillow.

High-quality flat-design character generation with proper proportions.
"""

from pathlib import Path

from PIL import Image, ImageDraw


def get_assets_dir() -> Path:
    """Get the assets directory path."""
    return Path(__file__).parent


def generate_base_character(
    size: tuple[int, int] = (512, 512),
    output_path: Path | None = None,
) -> Image.Image:
    """
    Generate high-quality flat-design rapper character.

    Args:
        size: Image dimensions (width, height)
        output_path: Optional path to save PNG

    Returns:
        PIL Image of base character (transparent background)
    """
    # High-res for quality
    scale = 2
    w, h = size[0] * scale, size[1] * scale
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, h // 2

    # === COLOR PALETTE ===
    skin = (220, 160, 115)
    skin_dark = (190, 135, 95)
    hair = (55, 35, 25)
    hair_light = (75, 50, 38)
    black = (20, 20, 24)
    black_dark = (12, 12, 15)
    gold = (235, 185, 50)
    gold_dark = (195, 150, 35)
    gold_light = (255, 215, 95)

    # === BODY (TORSO + SHOULDERS) ===
    # Main hoodie body - trapezoidal shape
    body_top = cy + 140
    body_bottom = h - 20
    shoulder_w = 260
    waist_w = 180

    body = [
        (cx - waist_w, body_bottom),
        (cx - shoulder_w, body_top),
        (cx + shoulder_w, body_top),
        (cx + waist_w, body_bottom),
    ]
    draw.polygon(body, fill=black)

    # Hoodie shadow/depth
    draw.polygon([
        (cx - shoulder_w + 40, body_top + 20),
        (cx - waist_w + 30, body_bottom),
        (cx + waist_w - 30, body_bottom),
        (cx + shoulder_w - 40, body_top + 20),
    ], fill=black_dark)

    # === NECK ===
    neck_top = body_top - 60
    neck_w = 55

    # Neck cylinder
    draw.rectangle([cx - neck_w, neck_top, cx + neck_w, body_top + 10], fill=skin_dark)
    draw.rectangle([cx - neck_w + 8, neck_top, cx + neck_w - 8, body_top + 10], fill=skin)

    # === GOLD CHAIN ===
    import math
    chain_center_y = body_top + 50
    chain_r = 22

    # Circular necklace path
    for i in range(13):
        angle = math.pi * (0.2 + 0.6 * i / 12)
        x = cx + math.cos(angle - math.pi / 2) * 130
        y = chain_center_y + math.sin(angle - math.pi / 2) * 50

        # Shadow
        draw.ellipse([x - chain_r + 3, y - chain_r + 3, x + chain_r + 3, y + chain_r + 3],
                     fill=gold_dark)
        # Gold piece
        draw.ellipse([x - chain_r, y - chain_r, x + chain_r, y + chain_r], fill=gold)
        # Highlight
        draw.ellipse([x - chain_r // 2, y - chain_r // 2, x + chain_r // 3, y + chain_r // 3],
                     fill=gold_light)

    # === HEAD (OVAL, PROPORTIONAL) ===
    head_bottom = neck_top + 15
    head_top = cy - 240
    head_w = 175
    head_h = head_bottom - head_top

    # Main head oval
    draw.ellipse([cx - head_w, head_top, cx + head_w, head_bottom], fill=skin)

    # Shading (left side)
    draw.ellipse([cx - head_w, head_top, cx - head_w + 50, head_bottom], fill=skin_dark)

    # === EARS ===
    ear_top = head_top + head_h // 3
    ear_h = 65
    ear_w = 32

    # Left ear
    draw.ellipse([cx - head_w - 12, ear_top, cx - head_w + ear_w, ear_top + ear_h], fill=skin)
    draw.ellipse([cx - head_w - 2, ear_top + 12, cx - head_w + 18, ear_top + ear_h - 15],
                 fill=skin_dark)

    # Right ear
    draw.ellipse([cx + head_w - ear_w, ear_top, cx + head_w + 12, ear_top + ear_h], fill=skin)
    draw.ellipse([cx + head_w - 18, ear_top + 12, cx + head_w + 2, ear_top + ear_h - 15],
                 fill=skin_dark)

    # === HAIR (SPIKY/MESSY STYLE) ===
    hair_bottom = head_top + 60

    # Hair silhouette
    hair_shape = [
        (cx - head_w - 15, hair_bottom),
        (cx - 140, head_top + 20),
        (cx - 95, head_top - 10),
        (cx - 50, head_top + 5),
        (cx - 10, head_top - 5),
        (cx + 30, head_top + 8),
        (cx + 70, head_top + 3),
        (cx + 110, head_top + 15),
        (cx + 145, head_top + 30),
        (cx + head_w + 10, hair_bottom),
    ]
    draw.polygon(hair_shape, fill=hair)

    # Hair highlights (spikes)
    draw.polygon([
        (cx - 100, head_top),
        (cx - 80, head_top - 8),
        (cx - 65, head_top + 8),
    ], fill=hair_light)

    draw.polygon([
        (cx - 10, head_top + 2),
        (cx + 5, head_top - 10),
        (cx + 20, head_top + 10),
    ], fill=hair_light)

    # === NOSE ===
    nose_y = head_top + head_h * 0.6
    draw.polygon([
        (cx - 12, nose_y - 8),
        (cx, nose_y + 18),
        (cx + 12, nose_y - 8),
    ], fill=skin_dark)

    # === SUNGLASSES (FLAT, MODERN) ===
    glass_top = head_top + head_h * 0.38
    glass_h = 50
    glass_w = 140
    frame = 10

    # Frame background
    draw.rounded_rectangle(
        [cx - glass_w - frame, glass_top - frame,
         cx + glass_w + frame, glass_top + glass_h + frame],
        radius=12, fill=black
    )

    # Left lens
    draw.rounded_rectangle(
        [cx - glass_w, glass_top, cx - 8, glass_top + glass_h],
        radius=8, fill=(30, 30, 35)
    )

    # Right lens
    draw.rounded_rectangle(
        [cx + 8, glass_top, cx + glass_w, glass_top + glass_h],
        radius=8, fill=(30, 30, 35)
    )

    # Bridge
    draw.rectangle([cx - 8, glass_top + 12, cx + 8, glass_top + 30], fill=black)

    # Reflections on lenses
    draw.arc([cx - glass_w + 15, glass_top + 8, cx - 50, glass_top + 28],
             start=30, end=140, fill=(255, 255, 255, 40), width=5)
    draw.arc([cx + 50, glass_top + 8, cx + glass_w - 15, glass_top + 28],
             start=40, end=150, fill=(255, 255, 255, 40), width=5)

    # Temples (arms going to ears)
    draw.line([(cx - glass_w - frame, glass_top + glass_h // 2),
               (cx - glass_w - 50, glass_top + glass_h // 2 + 12)],
              fill=black, width=frame)
    draw.line([(cx + glass_w + frame, glass_top + glass_h // 2),
               (cx + glass_w + 50, glass_top + glass_h // 2 + 12)],
              fill=black, width=frame)

    # Scale down with antialiasing
    img = img.resize(size, Image.Resampling.LANCZOS)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_closed(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate closed mouth (simple line)."""
    scale = 2
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    lip = (150, 70, 60)
    lip_dark = (120, 50, 45)

    # Horizontal mouth line with slight smile
    draw.arc([cx - 65, cy - 15, cx + 65, cy + 15], start=0, end=180, fill=lip_dark, width=14)
    draw.arc([cx - 60, cy - 12, cx + 60, cy + 12], start=0, end=180, fill=lip, width=10)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_a(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'A' mouth - vertical oval with teeth."""
    scale = 2
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (35, 15, 15)
    lip = (150, 70, 60)
    lip_dark = (120, 50, 45)
    teeth = (255, 255, 248)
    teeth_dark = (240, 240, 235)

    mw, mh = 70, 50

    # Inner cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=inside)

    # Upper teeth
    draw.rounded_rectangle([cx - 60, cy - 42, cx + 60, cy - 8], radius=6, fill=teeth)

    # Tooth lines
    for i in range(-2, 3):
        tx = cx + i * 24
        draw.line([(tx, cy - 42), (tx, cy - 8)], fill=teeth_dark, width=2)

    # Tongue hint
    draw.ellipse([cx - 45, cy + 8, cx + 45, cy + 30], fill=(180, 85, 85))

    # Lip outlines
    draw.ellipse([cx - mw - 5, cy - mh - 5, cx + mw + 5, cy + mh + 5],
                 outline=lip_dark, width=12)
    draw.ellipse([cx - mw - 2, cy - mh - 2, cx + mw + 2, cy + mh + 2],
                 outline=lip, width=7)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_o(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'O' mouth - round circle."""
    scale = 2
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (35, 15, 15)
    lip = (150, 70, 60)
    lip_dark = (120, 50, 45)

    r = 48

    # Inner cavity
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=inside)

    # Teeth hint (top)
    draw.arc([cx - 35, cy - 40, cx + 35, cy - 10], start=180, end=360,
             fill=(240, 240, 230), width=12)

    # Lip outlines
    draw.ellipse([cx - r - 5, cy - r - 5, cx + r + 5, cy + r + 5],
                 outline=lip_dark, width=12)
    draw.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2],
                 outline=lip, width=7)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_e(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'E' mouth - wide horizontal smile with visible teeth."""
    scale = 2
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (35, 15, 15)
    lip = (150, 70, 60)
    lip_dark = (120, 50, 45)
    teeth = (255, 255, 248)
    teeth_dark = (240, 240, 235)

    mw, mh = 110, 32

    # Inner cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=inside)

    # Upper teeth (prominent)
    draw.rounded_rectangle([cx - 95, cy - 25, cx + 95, cy + 3], radius=5, fill=teeth)

    # Tooth separations
    for i in range(-4, 5):
        tx = cx + i * 22
        draw.line([(tx, cy - 25), (tx, cy + 3)], fill=teeth_dark, width=2)

    # Lower teeth hint
    draw.ellipse([cx - 85, cy + 5, cx + 85, cy + 22], fill=(245, 245, 238))

    # Lip outlines
    draw.ellipse([cx - mw - 5, cy - mh - 5, cx + mw + 5, cy + mh + 5],
                 outline=lip_dark, width=10)
    draw.ellipse([cx - mw - 2, cy - mh - 2, cx + mw + 2, cy + mh + 2],
                 outline=lip, width=6)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_all_assets(force: bool = False) -> None:
    """Generate all high-quality assets."""
    assets_dir = get_assets_dir()
    assets_dir.mkdir(exist_ok=True)

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
            print(f"Generating: {filename}")
            generator_func(size=size, output_path=output_path)
            print(f"  -> Saved to {output_path}")
        else:
            print(f"Exists: {filename}")


def ensure_assets_exist() -> bool:
    """Check if all required assets exist, generate if missing."""
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
    import sys

    force = "--force" in sys.argv
    generate_all_assets(force=force)
    print("\n=== Asset generation complete! ===")
