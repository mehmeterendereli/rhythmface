"""
Professional flat-design character asset generation.

Creates high-quality vector-style PNG assets matching modern design standards.
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
    Generate professional flat-design rapper character.
    
    Style: Modern flat design with clean shapes and bold colors.
    
    Args:
        size: Image dimensions (width, height)
        output_path: Optional path to save PNG

    Returns:
        PIL Image of base character (transparent background)
    """
    # 3x super-sampling for ultra-sharp edges
    scale = 3
    w, h = size[0] * scale, size[1] * scale
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, h // 2

    # === FLAT DESIGN COLOR PALETTE ===
    skin = (218, 160, 116)
    skin_shadow = (195, 140, 100)
    skin_highlight = (235, 175, 130)
    
    hair_dark = (52, 34, 26)
    hair_mid = (68, 45, 35)
    hair_light = (85, 58, 45)
    
    black_shirt = (22, 22, 26)
    black_shadow = (14, 14, 17)
    
    gold = (232, 182, 55)
    gold_shadow = (198, 155, 42)
    gold_highlight = (248, 208, 95)
    
    glass_frame = (18, 18, 22)
    glass_lens = (28, 28, 32)

    # === BODY/TORSO (HOODIE) ===
    body_top_y = cy + 210
    body_bottom_y = h - 30
    shoulder_width = 390
    body_width = 270

    # Main hoodie shape (trapezoid)
    hoodie = [
        (cx - body_width, body_bottom_y),
        (cx - shoulder_width, body_top_y),
        (cx + shoulder_width, body_top_y),
        (cx + body_width, body_bottom_y),
    ]
    draw.polygon(hoodie, fill=black_shirt)

    # Inner shadow for depth
    inner_shadow = [
        (cx - shoulder_width + 60, body_top_y + 30),
        (cx - body_width + 45, body_bottom_y - 15),
        (cx + body_width - 45, body_bottom_y - 15),
        (cx + shoulder_width - 60, body_top_y + 30),
    ]
    draw.polygon(inner_shadow, fill=black_shadow)

    # === NECK ===
    neck_top_y = body_top_y - 90
    neck_width = 80

    # Neck shadow
    draw.rectangle([cx - neck_width - 10, neck_top_y, cx + neck_width + 10, body_top_y + 20],
                   fill=skin_shadow)
    # Neck main
    draw.rectangle([cx - neck_width, neck_top_y, cx + neck_width, body_top_y + 20],
                   fill=skin)

    # === GOLD CHAIN NECKLACE ===
    import math
    chain_y = body_top_y + 65
    chain_bead_size = 32
    num_beads = 11

    for i in range(num_beads):
        # Calculate chain curve position
        t = i / (num_beads - 1)
        angle = math.pi * (0.15 + 0.7 * t)
        x = cx + math.cos(angle - math.pi / 2) * 195
        y = chain_y + math.sin(angle - math.pi / 2) * 75

        # Bead shadow
        draw.ellipse([x - chain_bead_size + 5, y - chain_bead_size + 5,
                     x + chain_bead_size + 5, y + chain_bead_size + 5],
                     fill=gold_shadow)
        
        # Gold bead
        draw.ellipse([x - chain_bead_size, y - chain_bead_size,
                     x + chain_bead_size, y + chain_bead_size],
                     fill=gold)
        
        # Highlight (glossy effect)
        draw.ellipse([x - chain_bead_size // 2, y - chain_bead_size // 2,
                     x + chain_bead_size // 3, y + chain_bead_size // 3],
                     fill=gold_highlight)

    # === HEAD ===
    head_bottom_y = neck_top_y + 25
    head_top_y = cy - 360
    head_width = 260
    head_height = head_bottom_y - head_top_y

    # Head main shape (oval)
    draw.ellipse([cx - head_width, head_top_y, cx + head_width, head_bottom_y],
                 fill=skin)

    # Left side shadow
    draw.ellipse([cx - head_width, head_top_y, cx - head_width + 70, head_bottom_y],
                 fill=skin_shadow)

    # Cheek highlights
    draw.ellipse([cx - 80, head_top_y + head_height * 0.55,
                 cx - 45, head_top_y + head_height * 0.7],
                 fill=skin_highlight)
    draw.ellipse([cx + 45, head_top_y + head_height * 0.55,
                 cx + 80, head_top_y + head_height * 0.7],
                 fill=skin_highlight)

    # === EARS ===
    ear_top_y = head_top_y + head_height * 0.4
    ear_width = 45
    ear_height = 85

    # Left ear
    draw.ellipse([cx - head_width - 18, ear_top_y,
                 cx - head_width + ear_width, ear_top_y + ear_height],
                 fill=skin)
    # Inner ear detail
    draw.ellipse([cx - head_width - 5, ear_top_y + 18,
                 cx - head_width + 25, ear_top_y + ear_height - 22],
                 fill=skin_shadow)

    # Right ear
    draw.ellipse([cx + head_width - ear_width, ear_top_y,
                 cx + head_width + 18, ear_top_y + ear_height],
                 fill=skin)
    # Inner ear detail
    draw.ellipse([cx + head_width - 25, ear_top_y + 18,
                 cx + head_width + 5, ear_top_y + ear_height - 22],
                 fill=skin_shadow)

    # === HAIR (WAVY/TEXTURED) ===
    hair_base_y = head_top_y + 90

    # Main hair silhouette
    hair_outline = [
        (cx - head_width - 25, hair_base_y),
        (cx - head_width + 5, head_top_y + 45),
        (cx - 210, head_top_y + 20),
        (cx - 150, head_top_y - 5),
        (cx - 90, head_top_y + 10),
        (cx - 30, head_top_y),
        (cx + 30, head_top_y + 15),
        (cx + 90, head_top_y + 12),
        (cx + 150, head_top_y + 8),
        (cx + 210, head_top_y + 35),
        (cx + head_width - 10, head_top_y + 55),
        (cx + head_width + 15, hair_base_y),
    ]
    draw.polygon(hair_outline, fill=hair_dark)

    # Hair texture/waves
    wave1 = [
        (cx - 150, head_top_y + 5),
        (cx - 130, head_top_y - 10),
        (cx - 110, head_top_y + 8),
    ]
    draw.polygon(wave1, fill=hair_mid)

    wave2 = [
        (cx - 50, head_top_y + 8),
        (cx - 30, head_top_y - 8),
        (cx - 10, head_top_y + 5),
    ]
    draw.polygon(wave2, fill=hair_mid)

    wave3 = [
        (cx + 50, head_top_y + 15),
        (cx + 70, head_top_y + 3),
        (cx + 90, head_top_y + 18),
    ]
    draw.polygon(wave3, fill=hair_light)

    # === NOSE ===
    nose_y = head_top_y + head_height * 0.58
    nose_shape = [
        (cx - 18, nose_y - 5),
        (cx, nose_y + 25),
        (cx + 18, nose_y - 5),
    ]
    draw.polygon(nose_shape, fill=skin_shadow)

    # === SUNGLASSES (THICK FRAME, FLAT DESIGN) ===
    glass_center_y = head_top_y + head_height * 0.42
    glass_height = 70
    glass_width = 210
    frame_thickness = 15

    # Outer frame (thick black border)
    draw.rounded_rectangle(
        [cx - glass_width - frame_thickness, glass_center_y - frame_thickness,
         cx + glass_width + frame_thickness, glass_center_y + glass_height + frame_thickness],
        radius=18, fill=glass_frame
    )

    # Left lens
    draw.rounded_rectangle(
        [cx - glass_width, glass_center_y, cx - 12, glass_center_y + glass_height],
        radius=12, fill=glass_lens
    )

    # Right lens
    draw.rounded_rectangle(
        [cx + 12, glass_center_y, cx + glass_width, glass_center_y + glass_height],
        radius=12, fill=glass_lens
    )

    # Bridge
    draw.rectangle([cx - 12, glass_center_y + 18, cx + 12, glass_center_y + 42],
                   fill=glass_frame)

    # Lens reflections (white arcs)
    draw.arc([cx - glass_width + 25, glass_center_y + 12,
             cx - 80, glass_center_y + 38],
             start=35, end=145, fill=(255, 255, 255, 50), width=8)
    
    draw.arc([cx + 80, glass_center_y + 12,
             cx + glass_width - 25, glass_center_y + 38],
             start=35, end=145, fill=(255, 255, 255, 50), width=8)

    # Temple arms (sides)
    temple_y = glass_center_y + glass_height // 2
    draw.line([(cx - glass_width - frame_thickness, temple_y),
               (cx - glass_width - 75, temple_y + 15)],
              fill=glass_frame, width=frame_thickness)
    
    draw.line([(cx + glass_width + frame_thickness, temple_y),
               (cx + glass_width + 75, temple_y + 15)],
              fill=glass_frame, width=frame_thickness)

    # Scale down with premium antialiasing
    img = img.resize(size, Image.Resampling.LANCZOS)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_closed(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate closed mouth - simple horizontal line with slight smile."""
    scale = 3
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    lip_color = (145, 68, 58)
    lip_dark = (118, 52, 45)

    # Slight smile curve
    draw.arc([cx - 100, cy - 22, cx + 100, cy + 22],
             start=0, end=180, fill=lip_dark, width=20)
    draw.arc([cx - 95, cy - 18, cx + 95, cy + 18],
             start=0, end=180, fill=lip_color, width=14)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_a(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'A' mouth - vertical oval with visible upper teeth."""
    scale = 3
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    mouth_inside = (32, 12, 12)
    lip_color = (145, 68, 58)
    lip_dark = (118, 52, 45)
    teeth = (255, 255, 250)
    teeth_line = (238, 238, 235)
    tongue = (185, 88, 88)

    mouth_w, mouth_h = 105, 72

    # Inner mouth cavity
    draw.ellipse([cx - mouth_w, cy - mouth_h, cx + mouth_w, cy + mouth_h],
                 fill=mouth_inside)

    # Upper teeth row
    draw.rounded_rectangle([cx - 90, cy - 62, cx + 90, cy - 12],
                          radius=8, fill=teeth)
    
    # Individual tooth lines
    for i in range(-3, 4):
        tooth_x = cx + i * 28
        draw.line([(tooth_x, cy - 62), (tooth_x, cy - 12)],
                 fill=teeth_line, width=3)

    # Tongue hint
    draw.ellipse([cx - 68, cy + 12, cx + 68, cy + 45],
                 fill=tongue)

    # Lip outlines (thick)
    draw.ellipse([cx - mouth_w - 8, cy - mouth_h - 8,
                 cx + mouth_w + 8, cy + mouth_h + 8],
                 outline=lip_dark, width=18)
    draw.ellipse([cx - mouth_w - 3, cy - mouth_h - 3,
                 cx + mouth_w + 3, cy + mouth_h + 3],
                 outline=lip_color, width=10)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_o(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'O' mouth - perfect circle shape."""
    scale = 3
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    mouth_inside = (32, 12, 12)
    lip_color = (145, 68, 58)
    lip_dark = (118, 52, 45)
    teeth = (248, 248, 243)

    radius = 68

    # Inner cavity
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                 fill=mouth_inside)

    # Upper teeth hint (arc)
    draw.arc([cx - 52, cy - 58, cx + 52, cy - 15],
             start=180, end=360, fill=teeth, width=18)

    # Lip outlines
    draw.ellipse([cx - radius - 8, cy - radius - 8,
                 cx + radius + 8, cy + radius + 8],
                 outline=lip_dark, width=18)
    draw.ellipse([cx - radius - 3, cy - radius - 3,
                 cx + radius + 3, cy + radius + 3],
                 outline=lip_color, width=10)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_e(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'E' mouth - wide horizontal smile with prominent teeth."""
    scale = 3
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    mouth_inside = (32, 12, 12)
    lip_color = (145, 68, 58)
    lip_dark = (118, 52, 45)
    teeth = (255, 255, 250)
    teeth_line = (238, 238, 235)
    teeth_lower = (248, 248, 243)

    mouth_w, mouth_h = 165, 48

    # Inner cavity
    draw.ellipse([cx - mouth_w, cy - mouth_h, cx + mouth_w, cy + mouth_h],
                 fill=mouth_inside)

    # Upper teeth (prominent)
    draw.rounded_rectangle([cx - 142, cy - 38, cx + 142, cy + 5],
                          radius=7, fill=teeth)
    
    # Individual teeth
    for i in range(-6, 7):
        tooth_x = cx + i * 33
        draw.line([(tooth_x, cy - 38), (tooth_x, cy + 5)],
                 fill=teeth_line, width=3)

    # Lower teeth hint
    draw.ellipse([cx - 128, cy + 8, cx + 128, cy + 32],
                 fill=teeth_lower)

    # Lip outlines
    draw.ellipse([cx - mouth_w - 8, cy - mouth_h - 8,
                 cx + mouth_w + 8, cy + mouth_h + 8],
                 outline=lip_dark, width=15)
    draw.ellipse([cx - mouth_w - 3, cy - mouth_h - 3,
                 cx + mouth_w + 3, cy + mouth_h + 3],
                 outline=lip_color, width=9)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_all_assets(force: bool = False) -> None:
    """Generate all professional flat-design assets."""
    assets_dir = get_assets_dir()
    assets_dir.mkdir(exist_ok=True)

    assets = [
        ("base.png", generate_base_character, (512, 512)),
        ("mouth_closed.png", generate_mouth_closed, (256, 128)),
        ("mouth_A.png", generate_mouth_a, (256, 128)),
        ("mouth_O.png", generate_mouth_o, (256, 128)),
        ("mouth_E.png", generate_mouth_e, (256, 128)),
    ]

    print("=== Generating Professional Assets ===")
    for filename, generator_func, size in assets:
        output_path = assets_dir / filename

        if force or not output_path.exists():
            print(f"  Creating: {filename}...")
            generator_func(size=size, output_path=output_path)
            file_size = output_path.stat().st_size
            print(f"    -> Done ({file_size:,} bytes)")
        else:
            print(f"  Exists: {filename}")

    print("=== Asset Generation Complete ===\n")


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
