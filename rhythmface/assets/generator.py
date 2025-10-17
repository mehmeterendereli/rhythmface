"""
PREMIUM flat-design character generation - Reference-quality implementation.

Generates professional vector-style assets with bold shapes, clean lines,
and modern flat-design aesthetic.
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
    Generate PREMIUM flat-design rapper character.
    
    Reference-quality with bold shapes and professional polish.
    
    Args:
        size: Image dimensions (width, height)
        output_path: Optional path to save PNG

    Returns:
        PIL Image of base character (transparent background)
    """
    # 5x super-sampling for MAXIMUM quality
    scale = 5
    w, h = size[0] * scale, size[1] * scale
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, h // 2

    # === BOLD COLOR PALETTE (Reference-inspired) ===
    skin = (218, 160, 116)
    skin_dark = (185, 130, 92)
    skin_light = (240, 185, 138)
    
    hair = (45, 30, 22)
    hair_mid = (60, 42, 32)
    hair_high = (78, 55, 42)
    
    black = (18, 18, 22)
    black_shadow = (10, 10, 12)
    
    gold = (225, 175, 48)
    gold_dark = (188, 145, 35)
    gold_shine = (242, 200, 82)
    
    frame = (14, 14, 18)
    lens = (24, 24, 28)

    # === BODY (STRONG TRAPEZOID) ===
    body_top = cy + 350
    body_bottom = h - 50
    shoulder = 650
    waist = 450

    # Main body
    draw.polygon([
        (cx - waist, body_bottom),
        (cx - shoulder, body_top),
        (cx + shoulder, body_top),
        (cx + waist, body_bottom),
    ], fill=black)

    # Body shadow
    draw.polygon([
        (cx - shoulder + 100, body_top + 50),
        (cx - waist + 75, body_bottom - 25),
        (cx + waist - 75, body_bottom - 25),
        (cx + shoulder - 100, body_top + 50),
    ], fill=black_shadow)

    # === NECK (WIDE AND SOLID) ===
    neck_top = body_top - 150
    neck_w = 130

    draw.rectangle([cx - neck_w - 18, neck_top, cx + neck_w + 18, body_top + 40],
                   fill=skin_dark)
    draw.rectangle([cx - neck_w, neck_top, cx + neck_w, body_top + 40],
                   fill=skin)

    # === GOLD CHAIN (PROMINENT) ===
    import math
    chain_y = body_top + 105
    bead = 52
    count = 12

    for i in range(count):
        t = i / (count - 1)
        angle = math.pi * (0.1 + 0.8 * t)
        x = cx + math.cos(angle - math.pi / 2) * 320
        y = chain_y + math.sin(angle - math.pi / 2) * 120

        # Shadow
        draw.ellipse([x - bead + 7, y - bead + 7, x + bead + 7, y + bead + 7],
                     fill=gold_dark)
        # Gold
        draw.ellipse([x - bead, y - bead, x + bead, y + bead], fill=gold)
        # Shine
        draw.ellipse([x - bead // 2 + 5, y - bead // 2 + 5,
                     x + bead // 4, y + bead // 4], fill=gold_shine)

    # === HEAD (PERFECT PROPORTIONS) ===
    head_bottom = neck_top + 45
    head_top = cy - 600
    head_w = 430
    head_h = head_bottom - head_top

    # Main head
    draw.ellipse([cx - head_w, head_top, cx + head_w, head_bottom], fill=skin)

    # Shadows and highlights
    draw.ellipse([cx - head_w, head_top, cx - head_w + 110, head_bottom],
                 fill=skin_dark)
    draw.ellipse([cx + head_w - 90, head_top, cx + head_w, head_bottom],
                 fill=skin_light)

    # === EARS (BOLD) ===
    ear_y = head_top + int(head_h * 0.36)
    ear_w = 72
    ear_h = 140

    # Left
    draw.ellipse([cx - head_w - 30, ear_y, cx - head_w + ear_w + 15, ear_y + ear_h],
                 fill=skin)
    draw.ellipse([cx - head_w - 10, ear_y + 30, cx - head_w + 40, ear_y + ear_h - 35],
                 fill=skin_dark)

    # Right
    draw.ellipse([cx + head_w - ear_w - 15, ear_y, cx + head_w + 30, ear_y + ear_h],
                 fill=skin)
    draw.ellipse([cx + head_w - 40, ear_y + 30, cx + head_w + 10, ear_y + ear_h - 35],
                 fill=skin_dark)

    # === HAIR (BOLD SHAPES) ===
    hair_base = head_top + 150

    # Main hair mass (simplified bold shape)
    hair_outline = [
        (cx - head_w - 45, hair_base),
        (cx - head_w + 10, head_top + 75),
        (cx - 350, head_top + 35),
        (cx - 250, head_top - 12),
        (cx - 150, head_top + 15),
        (cx - 50, head_top - 3),
        (cx + 50, head_top + 20),
        (cx + 150, head_top + 18),
        (cx + 250, head_top + 12),
        (cx + 350, head_top + 55),
        (cx + head_w - 15, head_top + 90),
        (cx + head_w + 28, hair_base),
    ]
    draw.polygon(hair_outline, fill=hair)

    # Bold hair chunks (fewer, bigger)
    chunks = [
        # Left
        [(cx - 250, head_top + 2), (cx - 220, head_top - 15), (cx - 190, head_top + 18)],
        [(cx - 150, head_top + 22), (cx - 120, head_top + 8), (cx - 90, head_top + 20)],
        # Center
        [(cx - 50, head_top + 12), (cx - 20, head_top - 8), (cx + 10, head_top + 12)],
        [(cx + 50, head_top + 25), (cx + 80, head_top + 12), (cx + 110, head_top + 22)],
        # Right
        [(cx + 150, head_top + 22), (cx + 180, head_top + 5), (cx + 210, head_top + 18)],
    ]
    
    for chunk in chunks:
        draw.polygon(chunk, fill=hair_mid)

    # Highlights
    highlights = [
        [(cx - 230, head_top + 10), (cx - 210, head_top - 8), (cx - 190, head_top + 15)],
        [(cx - 30, head_top + 15), (cx - 10, head_top - 3), (cx + 10, head_top + 18)],
        [(cx + 170, head_top + 15), (cx + 190, head_top + 2), (cx + 210, head_top + 20)],
    ]
    
    for hl in highlights:
        draw.polygon(hl, fill=hair_high)

    # === NOSE (BOLD TRIANGLE) ===
    nose_y = head_top + int(head_h * 0.62)
    draw.polygon([
        (cx - 30, nose_y - 10),
        (cx, nose_y + 40),
        (cx + 30, nose_y - 10),
    ], fill=skin_dark)

    # === SUNGLASSES (EXTRA BOLD) ===
    glass_y = head_top + int(head_h * 0.4)
    glass_h = 115
    glass_w = 348
    frame_t = 25

    # Mega-thick frame
    draw.rounded_rectangle(
        [cx - glass_w - frame_t, glass_y - frame_t,
         cx + glass_w + frame_t, glass_y + glass_h + frame_t],
        radius=30, fill=frame
    )

    # Lenses
    draw.rounded_rectangle([cx - glass_w, glass_y, cx - 20, glass_y + glass_h],
                          radius=20, fill=lens)
    draw.rounded_rectangle([cx + 20, glass_y, cx + glass_w, glass_y + glass_h],
                          radius=20, fill=lens)

    # Bridge
    draw.rectangle([cx - 20, glass_y + 30, cx + 20, glass_y + 70], fill=frame)

    # Bold reflections
    draw.arc([cx - glass_w + 40, glass_y + 20, cx - 130, glass_y + 62],
             start=25, end=135, fill=(255, 255, 255, 80), width=13)
    draw.arc([cx + 130, glass_y + 20, cx + glass_w - 40, glass_y + 62],
             start=45, end=155, fill=(255, 255, 255, 80), width=13)

    # Temples
    temple_y = glass_y + glass_h // 2
    draw.line([(cx - glass_w - frame_t, temple_y),
               (cx - glass_w - 125, temple_y + 25)],
              fill=frame, width=frame_t)
    draw.line([(cx + glass_w + frame_t, temple_y),
               (cx + glass_w + 125, temple_y + 25)],
              fill=frame, width=frame_t)

    # === MOUTH INDICATOR (CLOSED SMILE LINE) ===
    mouth_y = head_top + int(head_h * 0.78)
    draw.arc([cx - 80, mouth_y - 15, cx + 80, mouth_y + 15],
             start=0, end=180, fill=skin_dark, width=12)

    # Scale to target with maximum quality
    img = img.resize(size, Image.Resampling.LANCZOS)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_closed(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate closed mouth - BOLD style."""
    scale = 5
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    lip = (138, 62, 54)
    lip_dark = (110, 45, 40)
    lip_high = (160, 78, 68)

    # Bold smile
    draw.arc([cx - 165, cy - 35, cx + 165, cy + 35],
             start=0, end=180, fill=lip_dark, width=32)
    draw.arc([cx - 155, cy - 30, cx + 155, cy + 30],
             start=0, end=180, fill=lip, width=22)
    draw.arc([cx - 145, cy - 38, cx + 145, cy - 8],
             start=0, end=180, fill=lip_high, width=10)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_a(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'A' mouth - BOLD teeth."""
    scale = 5
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (25, 8, 8)
    lip = (138, 62, 54)
    lip_dark = (110, 45, 40)
    lip_high = (160, 78, 68)
    teeth = (255, 255, 253)
    teeth_sep = (232, 232, 228)
    tongue = (190, 95, 95)

    mw, mh = 172, 118

    # Cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=inside)

    # BOLD upper teeth
    draw.rounded_rectangle([cx - 147, cy - 102, cx + 147, cy - 20],
                          radius=12, fill=teeth)
    
    # Tooth lines (bold) + shine
    for i in range(-5, 6):
        tx = cx + i * 46
        draw.line([(tx, cy - 102), (tx, cy - 20)], fill=teeth_sep, width=5)
        # Tooth shine effect
        draw.rectangle([tx - 18, cy - 100, tx - 10, cy - 75], fill=(255, 255, 255))

    # Tongue
    draw.ellipse([cx - 110, cy + 20, cx + 110, cy + 72], fill=tongue)

    # Lips (extra bold)
    draw.ellipse([cx - mw - 12, cy - mh - 12, cx + mw + 12, cy + mh + 12],
                 outline=lip_dark, width=30)
    draw.ellipse([cx - mw - 5, cy - mh - 5, cx + mw + 5, cy + mh + 5],
                 outline=lip, width=16)
    draw.arc([cx - mw, cy - mh - 10, cx + mw, cy],
             start=180, end=360, fill=lip_high, width=12)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_o(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'O' mouth - BOLD circle."""
    scale = 5
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (25, 8, 8)
    lip = (138, 62, 54)
    lip_dark = (110, 45, 40)
    lip_high = (160, 78, 68)
    teeth = (252, 252, 248)

    r = 110

    # Cavity
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=inside)

    # Teeth arc
    draw.arc([cx - 85, cy - 95, cx + 85, cy - 25],
             start=180, end=360, fill=teeth, width=30)

    # Lips
    draw.ellipse([cx - r - 12, cy - r - 12, cx + r + 12, cy + r + 12],
                 outline=lip_dark, width=30)
    draw.ellipse([cx - r - 5, cy - r - 5, cx + r + 5, cy + r + 5],
                 outline=lip, width=16)
    draw.arc([cx - r - 10, cy - r - 15, cx + r + 10, cy],
             start=180, end=360, fill=lip_high, width=12)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_e(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'E' mouth - BOLD wide smile with full teeth."""
    scale = 5
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (25, 8, 8)
    lip = (138, 62, 54)
    lip_dark = (110, 45, 40)
    lip_high = (160, 78, 68)
    teeth = (255, 255, 253)
    teeth_sep = (232, 232, 228)
    teeth_low = (252, 252, 248)

    mw, mh = 272, 78

    # Cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=inside)

    # BOLD upper teeth (super prominent)
    draw.rounded_rectangle([cx - 232, cy - 62, cx + 232, cy + 8],
                          radius=11, fill=teeth)
    
    # Bold tooth lines
    for i in range(-8, 9):
        tx = cx + i * 53
        draw.line([(tx, cy - 62), (tx, cy + 8)], fill=teeth_sep, width=5)
        # Bold tooth shine
        draw.rectangle([tx - 20, cy - 60, tx - 10, cy - 40], fill=(255, 255, 255))

    # Lower teeth
    draw.ellipse([cx - 210, cy + 12, cx + 210, cy + 52], fill=teeth_low)

    # Extra bold lips
    draw.ellipse([cx - mw - 12, cy - mh - 12, cx + mw + 12, cy + mh + 12],
                 outline=lip_dark, width=25)
    draw.ellipse([cx - mw - 5, cy - mh - 5, cx + mw + 5, cy + mh + 5],
                 outline=lip, width=15)
    draw.arc([cx - mw + 15, cy - mh - 10, cx + mw - 15, cy],
             start=180, end=360, fill=lip_high, width=10)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_all_assets(force: bool = False) -> None:
    """Generate all PREMIUM-quality assets."""
    assets_dir = get_assets_dir()
    assets_dir.mkdir(exist_ok=True)

    assets = [
        ("base.png", generate_base_character, (512, 512)),
        ("mouth_closed.png", generate_mouth_closed, (256, 128)),
        ("mouth_A.png", generate_mouth_a, (256, 128)),
        ("mouth_O.png", generate_mouth_o, (256, 128)),
        ("mouth_E.png", generate_mouth_e, (256, 128)),
    ]

    print("=== PREMIUM Asset Generation (5x Supersampling) ===")
    for filename, generator_func, size in assets:
        output_path = assets_dir / filename

        if force or not output_path.exists():
            print(f"  Rendering: {filename}...")
            generator_func(size=size, output_path=output_path)
            file_size = output_path.stat().st_size
            print(f"    -> {file_size:,} bytes")
        else:
            print(f"  Cached: {filename}")

    print("=== Generation Complete ===\n")


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
