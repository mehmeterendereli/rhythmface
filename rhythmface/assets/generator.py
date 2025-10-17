"""
Ultra-professional flat-design character asset generation.

Generates vector-quality PNG assets with clean shapes, bold colors,
and professional polish matching modern design standards.
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
    Generate ultra-professional flat-design rapper character.
    
    Reference quality: Clean vector-style with bold shapes and colors.
    
    Args:
        size: Image dimensions (width, height)
        output_path: Optional path to save PNG

    Returns:
        PIL Image of base character (transparent background)
    """
    # 4x super-sampling for maximum sharpness
    scale = 4
    w, h = size[0] * scale, size[1] * scale
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, h // 2

    # === PROFESSIONAL COLOR PALETTE ===
    # Skin tones
    skin_base = (218, 160, 116)
    skin_shadow = (190, 135, 98)
    skin_highlight = (238, 180, 135)
    
    # Hair colors
    hair_base = (48, 32, 24)
    hair_mid = (65, 45, 35)
    hair_highlight = (82, 58, 45)
    
    # Clothing
    black_base = (20, 20, 24)
    black_deep = (12, 12, 15)
    black_highlight = (32, 32, 36)
    
    # Gold chain
    gold_base = (228, 178, 52)
    gold_shadow = (192, 148, 38)
    gold_shine = (245, 205, 88)
    
    # Sunglasses
    frame_black = (16, 16, 20)
    lens_dark = (26, 26, 30)

    # === BODY/HOODIE ===
    body_top_y = cy + 280
    body_bottom_y = h - 40
    shoulder_w = 520
    waist_w = 360

    # Main hoodie shape
    hoodie_shape = [
        (cx - waist_w, body_bottom_y),
        (cx - shoulder_w, body_top_y),
        (cx + shoulder_w, body_top_y),
        (cx + waist_w, body_bottom_y),
    ]
    draw.polygon(hoodie_shape, fill=black_base)

    # Hoodie depth/shadow
    hoodie_shadow = [
        (cx - shoulder_w + 80, body_top_y + 40),
        (cx - waist_w + 60, body_bottom_y - 20),
        (cx + waist_w - 60, body_bottom_y - 20),
        (cx + shoulder_w - 80, body_top_y + 40),
    ]
    draw.polygon(hoodie_shadow, fill=black_deep)

    # Hoodie highlights (collar area)
    hoodie_highlight = [
        (cx - shoulder_w + 40, body_top_y + 10),
        (cx - shoulder_w + 120, body_top_y),
        (cx - shoulder_w + 160, body_top_y + 20),
    ]
    draw.polygon(hoodie_highlight, fill=black_highlight)

    # === NECK ===
    neck_top_y = body_top_y - 120
    neck_w = 105

    # Neck with gradient effect
    draw.rectangle([cx - neck_w - 15, neck_top_y, cx + neck_w + 15, body_top_y + 30],
                   fill=skin_shadow)
    draw.rectangle([cx - neck_w, neck_top_y, cx + neck_w, body_top_y + 30],
                   fill=skin_base)
    # Neck highlight (front)
    draw.rectangle([cx - neck_w + 20, neck_top_y, cx + neck_w - 20, body_top_y + 30],
                   fill=skin_base)

    # === PREMIUM GOLD CHAIN ===
    import math
    chain_center_y = body_top_y + 85
    bead_size = 42
    num_beads = 12

    for i in range(num_beads):
        t = i / (num_beads - 1)
        angle = math.pi * (0.12 + 0.76 * t)
        x = cx + math.cos(angle - math.pi / 2) * 258
        y = chain_center_y + math.sin(angle - math.pi / 2) * 98

        # Shadow
        draw.ellipse([x - bead_size + 6, y - bead_size + 6,
                     x + bead_size + 6, y + bead_size + 6],
                     fill=gold_shadow)
        
        # Main gold bead
        draw.ellipse([x - bead_size, y - bead_size,
                     x + bead_size, y + bead_size],
                     fill=gold_base)
        
        # Shine (top-left)
        draw.ellipse([x - bead_size // 2, y - bead_size // 2,
                     x + bead_size // 4, y + bead_size // 4],
                     fill=gold_shine)

    # === HEAD (PERFECT OVAL) ===
    head_bottom_y = neck_top_y + 35
    head_top_y = cy - 480
    head_w = 345
    head_h = head_bottom_y - head_top_y

    # Main head
    draw.ellipse([cx - head_w, head_top_y, cx + head_w, head_bottom_y],
                 fill=skin_base)

    # Left shadow
    draw.ellipse([cx - head_w, head_top_y, cx - head_w + 90, head_bottom_y],
                 fill=skin_shadow)

    # Right highlight
    draw.ellipse([cx + head_w - 70, head_top_y, cx + head_w, head_bottom_y],
                 fill=skin_highlight)

    # Cheek highlights (blush)
    draw.ellipse([cx - 105, head_top_y + int(head_h * 0.58),
                 cx - 58, head_top_y + int(head_h * 0.72)],
                 fill=skin_highlight)
    draw.ellipse([cx + 58, head_top_y + int(head_h * 0.58),
                 cx + 105, head_top_y + int(head_h * 0.72)],
                 fill=skin_highlight)

    # === EARS (DETAILED) ===
    ear_top_y = head_top_y + int(head_h * 0.38)
    ear_w = 58
    ear_h = 112

    # Left ear
    draw.ellipse([cx - head_w - 24, ear_top_y,
                 cx - head_w + ear_w + 10, ear_top_y + ear_h],
                 fill=skin_base)
    # Inner ear shadow
    draw.ellipse([cx - head_w - 8, ear_top_y + 24,
                 cx - head_w + 32, ear_top_y + ear_h - 28],
                 fill=skin_shadow)

    # Right ear
    draw.ellipse([cx + head_w - ear_w - 10, ear_top_y,
                 cx + head_w + 24, ear_top_y + ear_h],
                 fill=skin_base)
    # Inner ear shadow
    draw.ellipse([cx + head_w - 32, ear_top_y + 24,
                 cx + head_w + 8, ear_top_y + ear_h - 28],
                 fill=skin_shadow)

    # === HAIR (TEXTURED, WAVY) ===
    hair_bottom_y = head_top_y + 120

    # Main hair outline (complex shape)
    hair_main = [
        (cx - head_w - 35, hair_bottom_y),
        (cx - head_w + 8, head_top_y + 60),
        (cx - 280, head_top_y + 28),
        (cx - 200, head_top_y - 8),
        (cx - 120, head_top_y + 12),
        (cx - 40, head_top_y - 2),
        (cx + 40, head_top_y + 18),
        (cx + 120, head_top_y + 15),
        (cx + 200, head_top_y + 10),
        (cx + 280, head_top_y + 45),
        (cx + head_w - 12, head_top_y + 72),
        (cx + head_w + 22, hair_bottom_y),
    ]
    draw.polygon(hair_main, fill=hair_base)

    # Hair texture waves (multiple layers)
    wave_sets = [
        # Left waves
        [(cx - 200, head_top_y), (cx - 175, head_top_y - 12), (cx - 150, head_top_y + 10)],
        [(cx - 120, head_top_y + 18), (cx - 95, head_top_y + 5), (cx - 70, head_top_y + 15)],
        # Center waves
        [(cx - 40, head_top_y + 5), (cx - 15, head_top_y - 8), (cx + 10, head_top_y + 8)],
        [(cx + 40, head_top_y + 22), (cx + 65, head_top_y + 10), (cx + 90, head_top_y + 20)],
        # Right waves
        [(cx + 120, head_top_y + 18), (cx + 145, head_top_y + 5), (cx + 170, head_top_y + 15)],
    ]
    
    for wave in wave_sets:
        draw.polygon(wave, fill=hair_mid)

    # Hair highlights (brightest strands)
    highlight_strands = [
        [(cx - 180, head_top_y + 8), (cx - 165, head_top_y - 5), (cx - 150, head_top_y + 12)],
        [(cx - 20, head_top_y + 10), (cx, head_top_y - 5), (cx + 20, head_top_y + 15)],
        [(cx + 140, head_top_y + 12), (cx + 155, head_top_y + 2), (cx + 170, head_top_y + 18)],
    ]
    
    for strand in highlight_strands:
        draw.polygon(strand, fill=hair_highlight)

    # === NOSE (TRIANGULAR) ===
    nose_y = head_top_y + int(head_h * 0.6)
    nose_shape = [
        (cx - 24, nose_y - 8),
        (cx, nose_y + 32),
        (cx + 24, nose_y - 8),
    ]
    draw.polygon(nose_shape, fill=skin_shadow)

    # === SUNGLASSES (THICK FRAME, PROFESSIONAL) ===
    glass_top_y = head_top_y + int(head_h * 0.42)
    glass_h = 92
    glass_w = 278
    frame_thick = 20

    # Outer frame (very thick)
    draw.rounded_rectangle(
        [cx - glass_w - frame_thick, glass_top_y - frame_thick,
         cx + glass_w + frame_thick, glass_top_y + glass_h + frame_thick],
        radius=24, fill=frame_black
    )

    # Left lens
    draw.rounded_rectangle(
        [cx - glass_w, glass_top_y, cx - 16, glass_top_y + glass_h],
        radius=16, fill=lens_dark
    )

    # Right lens
    draw.rounded_rectangle(
        [cx + 16, glass_top_y, cx + glass_w, glass_top_y + glass_h],
        radius=16, fill=lens_dark
    )

    # Bridge (thick)
    draw.rectangle([cx - 16, glass_top_y + 24, cx + 16, glass_top_y + 56],
                   fill=frame_black)

    # Lens reflections (white shine)
    # Left lens reflection
    draw.arc([cx - glass_w + 32, glass_top_y + 16,
             cx - 105, glass_top_y + 50],
             start=30, end=140, fill=(255, 255, 255, 65), width=10)
    
    # Right lens reflection
    draw.arc([cx + 105, glass_top_y + 16,
             cx + glass_w - 32, glass_top_y + 50],
             start=40, end=150, fill=(255, 255, 255, 65), width=10)

    # Temple arms (side extensions)
    temple_y = glass_top_y + glass_h // 2
    draw.line([(cx - glass_w - frame_thick, temple_y),
               (cx - glass_w - 100, temple_y + 20)],
              fill=frame_black, width=frame_thick)
    
    draw.line([(cx + glass_w + frame_thick, temple_y),
               (cx + glass_w + 100, temple_y + 20)],
              fill=frame_black, width=frame_thick)

    # Scale down to target size with maximum quality
    img = img.resize(size, Image.Resampling.LANCZOS)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_closed(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate closed mouth with professional styling."""
    scale = 4
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    lip_base = (142, 65, 56)
    lip_dark = (115, 48, 42)
    lip_highlight = (165, 82, 70)

    # Gentle smile curve
    draw.arc([cx - 132, cy - 28, cx + 132, cy + 28],
             start=0, end=180, fill=lip_dark, width=26)
    draw.arc([cx - 125, cy - 24, cx + 125, cy + 24],
             start=0, end=180, fill=lip_base, width=18)
    # Lip highlight (glossy top)
    draw.arc([cx - 115, cy - 30, cx + 115, cy - 5],
             start=0, end=180, fill=lip_highlight, width=8)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_a(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'A' mouth with professional teeth and shading."""
    scale = 4
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (28, 10, 10)
    lip_base = (142, 65, 56)
    lip_dark = (115, 48, 42)
    lip_highlight = (165, 82, 70)
    teeth = (255, 255, 252)
    teeth_shadow = (240, 240, 238)
    teeth_separator = (235, 235, 232)
    tongue = (188, 92, 92)

    mw, mh = 138, 95

    # Inner cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=inside)

    # Upper teeth (prominent)
    draw.rounded_rectangle([cx - 118, cy - 82, cx + 118, cy - 16],
                          radius=10, fill=teeth)
    
    # Teeth shadows (top and bottom)
    draw.rounded_rectangle([cx - 118, cy - 82, cx + 118, cy - 70],
                          radius=10, fill=teeth_shadow)
    
    # Individual tooth separators
    for i in range(-4, 5):
        tx = cx + i * 37
        draw.line([(tx, cy - 82), (tx, cy - 16)], fill=teeth_separator, width=4)

    # Tongue
    draw.ellipse([cx - 88, cy + 16, cx + 88, cy + 58], fill=tongue)

    # Outer lips (thick outline)
    draw.ellipse([cx - mw - 10, cy - mh - 10, cx + mw + 10, cy + mh + 10],
                 outline=lip_dark, width=24)
    draw.ellipse([cx - mw - 4, cy - mh - 4, cx + mw + 4, cy + mh + 4],
                 outline=lip_base, width=13)
    # Top lip highlight
    draw.arc([cx - mw, cy - mh - 8, cx + mw, cy],
             start=180, end=360, fill=lip_highlight, width=10)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_o(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'O' mouth - perfect circle with depth."""
    scale = 4
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (28, 10, 10)
    lip_base = (142, 65, 56)
    lip_dark = (115, 48, 42)
    lip_highlight = (165, 82, 70)
    teeth = (250, 250, 246)

    r = 88

    # Inner cavity
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=inside)

    # Upper teeth arc
    draw.arc([cx - 68, cy - 76, cx + 68, cy - 20],
             start=180, end=360, fill=teeth, width=24)

    # Outer lips
    draw.ellipse([cx - r - 10, cy - r - 10, cx + r + 10, cy + r + 10],
                 outline=lip_dark, width=24)
    draw.ellipse([cx - r - 4, cy - r - 4, cx + r + 4, cy + r + 4],
                 outline=lip_base, width=13)
    # Top highlight
    draw.arc([cx - r - 8, cy - r - 12, cx + r + 8, cy],
             start=180, end=360, fill=lip_highlight, width=10)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_e(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'E' mouth - wide smile with full teeth display."""
    scale = 4
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    inside = (28, 10, 10)
    lip_base = (142, 65, 56)
    lip_dark = (115, 48, 42)
    lip_highlight = (165, 82, 70)
    teeth = (255, 255, 252)
    teeth_shadow = (240, 240, 238)
    teeth_separator = (235, 235, 232)
    teeth_lower = (250, 250, 246)

    mw, mh = 218, 63

    # Inner cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=inside)

    # Upper teeth (very prominent)
    draw.rounded_rectangle([cx - 187, cy - 50, cx + 187, cy + 6],
                          radius=9, fill=teeth)
    
    # Teeth shadow (top edge)
    draw.rounded_rectangle([cx - 187, cy - 50, cx + 187, cy - 38],
                          radius=9, fill=teeth_shadow)
    
    # Individual teeth
    for i in range(-7, 8):
        tx = cx + i * 43
        draw.line([(tx, cy - 50), (tx, cy + 6)], fill=teeth_separator, width=4)
        # Tooth shine (top)
        draw.rectangle([tx - 16, cy - 48, tx - 8, cy - 32], fill=(255, 255, 255))

    # Lower teeth hint
    draw.ellipse([cx - 168, cy + 10, cx + 168, cy + 42], fill=teeth_lower)

    # Outer lips
    draw.ellipse([cx - mw - 10, cy - mh - 10, cx + mw + 10, cy + mh + 10],
                 outline=lip_dark, width=20)
    draw.ellipse([cx - mw - 4, cy - mh - 4, cx + mw + 4, cy + mh + 4],
                 outline=lip_base, width=12)
    # Top lip highlight
    draw.arc([cx - mw + 10, cy - mh - 8, cx + mw - 10, cy],
             start=180, end=360, fill=lip_highlight, width=8)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_all_assets(force: bool = False) -> None:
    """Generate all ultra-professional assets."""
    assets_dir = get_assets_dir()
    assets_dir.mkdir(exist_ok=True)

    assets = [
        ("base.png", generate_base_character, (512, 512)),
        ("mouth_closed.png", generate_mouth_closed, (256, 128)),
        ("mouth_A.png", generate_mouth_a, (256, 128)),
        ("mouth_O.png", generate_mouth_o, (256, 128)),
        ("mouth_E.png", generate_mouth_e, (256, 128)),
    ]

    print("=== Ultra-Professional Asset Generation ===")
    for filename, generator_func, size in assets:
        output_path = assets_dir / filename

        if force or not output_path.exists():
            print(f"  Rendering: {filename} (4x supersampling)...")
            generator_func(size=size, output_path=output_path)
            file_size = output_path.stat().st_size
            print(f"    -> Complete ({file_size:,} bytes)")
        else:
            print(f"  Cached: {filename}")

    print("=== All Assets Generated Successfully ===\n")


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
