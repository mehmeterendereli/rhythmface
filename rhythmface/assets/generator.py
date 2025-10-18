"""
MODERN flat-design character generation - Professional quality implementation.

Generates sleek vector-style assets with contemporary aesthetics,
smooth gradients, and polished details.
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
    Generate modern flat-design character with improved aesthetics.
    
    Args:
        size: Image dimensions (width, height)
        output_path: Optional path to save PNG

    Returns:
        PIL Image of base character (transparent background)
    """
    # 6x super-sampling for premium quality
    scale = 6
    w, h = size[0] * scale, size[1] * scale
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = w // 2, h // 2

    # === MODERN COLOR PALETTE ===
    # Skin tones - warmer and more natural
    skin_base = (235, 195, 160)
    skin_shadow = (200, 160, 130)
    skin_highlight = (245, 215, 185)
    
    # Hair - rich brown with depth
    hair_dark = (60, 40, 30)
    hair_mid = (85, 60, 45)
    hair_light = (110, 80, 60)
    
    # Clothing - sleek dark with subtle variation
    shirt_dark = (25, 25, 30)
    shirt_base = (35, 35, 42)
    shirt_highlight = (50, 50, 58)
    
    # Gold chain - vibrant and eye-catching
    gold_shadow = (200, 150, 40)
    gold_base = (240, 190, 60)
    gold_shine = (255, 220, 100)
    
    # Sunglasses - deep black with style
    frame_color = (20, 20, 25)
    lens_color = (30, 35, 45)
    lens_reflection = (80, 90, 110)

    # === BODY (Modern trapezoid with style) ===
    body_top = cy + 280
    body_bottom = h - 40
    shoulder_width = 580
    waist_width = 420

    # Main shirt with gradient effect
    draw.polygon([
        (cx - waist_width, body_bottom),
        (cx - shoulder_width, body_top),
        (cx + shoulder_width, body_top),
        (cx + waist_width, body_bottom),
    ], fill=shirt_base)

    # Shadow layer for depth
    draw.polygon([
        (cx - shoulder_width + 80, body_top + 40),
        (cx - waist_width + 60, body_bottom - 20),
        (cx + waist_width - 60, body_bottom - 20),
        (cx + shoulder_width - 80, body_top + 40),
    ], fill=shirt_dark)

    # Highlight for dimension
    draw.polygon([
        (cx - 50, body_top + 30),
        (cx - 200, body_top + 80),
        (cx - 180, body_top + 200),
        (cx - 30, body_top + 150),
    ], fill=shirt_highlight)

    # === NECK (Smooth and proportional) ===
    neck_top = body_top - 120
    neck_width = 110

    # Neck shadow
    draw.ellipse([cx - neck_width - 15, neck_top - 20, 
                  cx + neck_width + 15, body_top + 30],
                 fill=skin_shadow)
    
    # Main neck
    draw.ellipse([cx - neck_width, neck_top - 10, 
                  cx + neck_width, body_top + 25],
                 fill=skin_base)

    # === GOLD CHAIN (Eye-catching centerpiece) ===
    import math
    chain_y = body_top + 80
    bead_size = 45
    bead_count = 14

    for i in range(bead_count):
        t = i / (bead_count - 1)
        angle = math.pi * (0.15 + 0.7 * t)
        x = cx + math.cos(angle - math.pi / 2) * 280
        y = chain_y + math.sin(angle - math.pi / 2) * 100

        # Shadow bead
        draw.ellipse([x - bead_size + 5, y - bead_size + 5, 
                     x + bead_size + 5, y + bead_size + 5],
                     fill=gold_shadow)
        
        # Main gold bead
        draw.ellipse([x - bead_size, y - bead_size, 
                     x + bead_size, y + bead_size], 
                     fill=gold_base)
        
        # Shine highlight
        draw.ellipse([x - bead_size // 3, y - bead_size // 3,
                     x + bead_size // 4, y + bead_size // 4], 
                     fill=gold_shine)

    # === HEAD (Perfect oval with smooth shading) ===
    head_bottom = neck_top + 35
    head_top = cy - 550
    head_width = 400
    head_height = head_bottom - head_top

    # Head shadow (left side)
    draw.ellipse([cx - head_width - 8, head_top - 5, 
                  cx + head_width + 8, head_bottom + 5],
                 fill=skin_shadow)
    
    # Main head
    draw.ellipse([cx - head_width, head_top, 
                  cx + head_width, head_bottom], 
                 fill=skin_base)

    # Subtle shading gradient
    draw.ellipse([cx - head_width + 20, head_top + 20, 
                  cx - head_width + 100, head_bottom - 20],
                 fill=skin_shadow)
    
    # Highlight (right side)
    draw.ellipse([cx + head_width - 80, head_top + 30, 
                  cx + head_width - 15, head_bottom - 30],
                 fill=skin_highlight)

    # === EARS (Subtle and proportional) ===
    ear_y = head_top + int(head_height * 0.38)
    ear_width = 65
    ear_height = 120

    # Left ear
    draw.ellipse([cx - head_width - 20, ear_y, 
                  cx - head_width + ear_width + 10, ear_y + ear_height],
                 fill=skin_base)
    draw.ellipse([cx - head_width, ear_y + 25, 
                  cx - head_width + 35, ear_y + ear_height - 30],
                 fill=skin_shadow)

    # Right ear
    draw.ellipse([cx + head_width - ear_width - 10, ear_y, 
                  cx + head_width + 20, ear_y + ear_height],
                 fill=skin_base)
    draw.ellipse([cx + head_width - 35, ear_y + 25, 
                  cx + head_width, ear_y + ear_height - 30],
                 fill=skin_shadow)

    # === HAIR (Modern, textured style) ===
    hair_base_y = head_top + 120

    # Main hair silhouette
    hair_points = [
        (cx - head_width - 35, hair_base_y),
        (cx - head_width + 15, head_top + 60),
        (cx - 320, head_top + 25),
        (cx - 200, head_top - 15),
        (cx - 100, head_top + 5),
        (cx, head_top - 8),
        (cx + 100, head_top + 8),
        (cx + 200, head_top + 2),
        (cx + 320, head_top + 35),
        (cx + head_width - 20, head_top + 75),
        (cx + head_width + 25, hair_base_y),
    ]
    draw.polygon(hair_points, fill=hair_dark)

    # Hair texture strands
    strands = [
        # Left side
        [(cx - 280, head_top + 15), (cx - 250, head_top - 10), (cx - 220, head_top + 20)],
        [(cx - 180, head_top + 10), (cx - 150, head_top - 5), (cx - 120, head_top + 15)],
        # Center
        [(cx - 60, head_top + 5), (cx - 30, head_top - 12), (cx, head_top + 8)],
        [(cx, head_top + 8), (cx + 30, head_top - 8), (cx + 60, head_top + 12)],
        # Right side
        [(cx + 120, head_top + 15), (cx + 150, head_top - 2), (cx + 180, head_top + 18)],
        [(cx + 220, head_top + 20), (cx + 250, head_top + 5), (cx + 280, head_top + 25)],
    ]
    
    for strand in strands:
        draw.polygon(strand, fill=hair_mid)

    # Hair highlights for depth
    highlights = [
        [(cx - 250, head_top + 5), (cx - 230, head_top - 8), (cx - 210, head_top + 12)],
        [(cx - 30, head_top + 8), (cx - 10, head_top - 6), (cx + 10, head_top + 15)],
        [(cx + 210, head_top + 12), (cx + 230, head_top + 2), (cx + 250, head_top + 20)],
    ]
    
    for hl in highlights:
        draw.polygon(hl, fill=hair_light)

    # === NOSE (Subtle triangle) ===
    nose_y = head_top + int(head_height * 0.58)
    draw.polygon([
        (cx - 22, nose_y),
        (cx, nose_y + 35),
        (cx + 22, nose_y),
    ], fill=skin_shadow)

    # === SUNGLASSES (Sleek and modern) ===
    glass_y = head_top + int(head_height * 0.38)
    glass_height = 105
    glass_width = 320
    frame_thickness = 22

    # Frame outline
    draw.rounded_rectangle(
        [cx - glass_width - frame_thickness, glass_y - frame_thickness,
         cx + glass_width + frame_thickness, glass_y + glass_height + frame_thickness],
        radius=28, fill=frame_color
    )

    # Left lens
    draw.rounded_rectangle(
        [cx - glass_width, glass_y, cx - 25, glass_y + glass_height],
        radius=18, fill=lens_color
    )
    
    # Right lens
    draw.rounded_rectangle(
        [cx + 25, glass_y, cx + glass_width, glass_y + glass_height],
        radius=18, fill=lens_color
    )

    # Nose bridge
    draw.rounded_rectangle(
        [cx - 25, glass_y + 25, cx + 25, glass_y + 60],
        radius=8, fill=frame_color
    )

    # Lens reflections (modern style)
    draw.ellipse([cx - glass_width + 35, glass_y + 15, 
                  cx - glass_width + 110, glass_y + 50],
                 fill=(255, 255, 255, 60))
    draw.ellipse([cx + glass_width - 110, glass_y + 15, 
                  cx + glass_width - 35, glass_y + 50],
                 fill=(255, 255, 255, 60))
    
    # Secondary reflections
    draw.arc([cx - glass_width + 50, glass_y + 25, cx - 120, glass_y + 65],
             start=30, end=140, fill=lens_reflection, width=10)
    draw.arc([cx + 120, glass_y + 25, cx + glass_width - 50, glass_y + 65],
             start=40, end=150, fill=lens_reflection, width=10)

    # Temples (arms)
    temple_y = glass_y + glass_height // 2
    draw.line([(cx - glass_width - frame_thickness, temple_y),
               (cx - glass_width - 110, temple_y + 22)],
              fill=frame_color, width=frame_thickness)
    draw.line([(cx + glass_width + frame_thickness, temple_y),
               (cx + glass_width + 110, temple_y + 22)],
              fill=frame_color, width=frame_thickness)

    # === MOUTH AREA (Subtle smile hint) ===
    mouth_y = head_top + int(head_height * 0.75)
    draw.arc([cx - 70, mouth_y - 12, cx + 70, mouth_y + 12],
             start=0, end=180, fill=skin_shadow, width=10)

    # Downscale with premium quality
    img = img.resize(size, Image.Resampling.LANCZOS)

    if output_path:
        img.save(output_path)

    return img


def generate_mouth_closed(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate closed mouth with subtle natural smile - matching base.png aesthetic."""
    scale = 6
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    # Colors matching base.png palette (skin_shadow for hint line)
    lip_outline = (180, 140, 125)  # Warm tone from skin palette
    lip_fill = (210, 160, 145)     # Lighter warm tone
    lip_highlight = (235, 185, 170)  # Brightest highlight

    # Subtle smile curve - matching the hint line in base.png
    draw.arc([cx - 140, cy - 25, cx + 140, cy + 25],
             start=0, end=180, fill=lip_outline, width=24)
    draw.arc([cx - 132, cy - 22, cx + 132, cy + 22],
             start=0, end=180, fill=lip_fill, width=18)
    draw.arc([cx - 128, cy - 28, cx + 128, cy - 6],
             start=0, end=180, fill=lip_highlight, width=8)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_a(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'A' mouth with visible teeth - matching base.png modern flat-design."""
    scale = 6
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    # Modern palette matching base.png
    mouth_cavity = (45, 20, 20)    # Dark interior
    lip_outline = (180, 140, 125)  # Warm outline
    lip_fill = (210, 160, 145)     # Medium lip
    lip_highlight = (235, 185, 170)  # Bright highlight
    teeth = (248, 248, 242)        # Natural white teeth
    teeth_line = (225, 220, 210)   # Tooth separator
    tongue = (205, 120, 110)       # Warm red-brown tongue

    mw, mh = 155, 105

    # Mouth cavity ellipse
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=mouth_cavity)

    # Upper teeth - rounded rectangle
    draw.rounded_rectangle([cx - 130, cy - 90, cx + 130, cy - 20],
                          radius=9, fill=teeth)
    
    # Individual teeth separators with shine
    for i in range(-5, 6):
        tooth_x = cx + i * 40
        # Separator line
        draw.line([(tooth_x, cy - 90), (tooth_x, cy - 20)], 
                 fill=teeth_line, width=3)
        # Tooth shine rectangle
        draw.rectangle([tooth_x - 15, cy - 87, tooth_x - 8, cy - 68], 
                      fill=(255, 255, 255, 180))

    # Tongue
    draw.ellipse([cx - 95, cy + 10, cx + 95, cy + 60], fill=tongue)
    # Tongue centerline
    draw.line([(cx, cy + 15), (cx, cy + 55)], fill=(185, 105, 95), width=2)

    # Lips with gradient effect
    draw.ellipse([cx - mw - 9, cy - mh - 9, cx + mw + 9, cy + mh + 9],
                 outline=lip_outline, width=22)
    draw.ellipse([cx - mw - 3, cy - mh - 3, cx + mw + 3, cy + mh + 3],
                 outline=lip_fill, width=12)
    draw.arc([cx - mw, cy - mh - 7, cx + mw, cy - 5],
             start=180, end=360, fill=lip_highlight, width=8)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_o(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'O' mouth with rounded shape - matching base.png modern aesthetic."""
    scale = 6
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    # Modern palette
    mouth_cavity = (45, 20, 20)
    lip_outline = (180, 140, 125)
    lip_fill = (210, 160, 145)
    lip_highlight = (235, 185, 170)
    teeth = (248, 248, 242)

    radius = 95

    # Mouth cavity - perfect circle
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius], 
                 fill=mouth_cavity)

    # Upper teeth arc
    draw.arc([cx - 72, cy - 82, cx + 72, cy - 22],
             start=180, end=360, fill=teeth, width=24)

    # Lips with depth
    draw.ellipse([cx - radius - 9, cy - radius - 9, cx + radius + 9, cy + radius + 9],
                 outline=lip_outline, width=22)
    draw.ellipse([cx - radius - 3, cy - radius - 3, cx + radius + 3, cy + radius + 3],
                 outline=lip_fill, width=12)
    draw.arc([cx - radius - 7, cy - radius - 10, cx + radius + 7, cy - 3],
             start=180, end=360, fill=lip_highlight, width=8)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_mouth_e(
    size: tuple[int, int] = (256, 128),
    output_path: Path | None = None,
) -> Image.Image:
    """Generate 'E' mouth with wide smile and full teeth - matching base.png professional style."""
    scale = 6
    img = Image.new("RGBA", (size[0] * scale, size[1] * scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    cx, cy = (size[0] * scale) // 2, (size[1] * scale) // 2

    # Modern palette matching base.png
    mouth_cavity = (45, 20, 20)
    lip_outline = (180, 140, 125)
    lip_fill = (210, 160, 145)
    lip_highlight = (235, 185, 170)
    teeth = (248, 248, 242)
    teeth_line = (225, 220, 210)
    teeth_lower = (242, 240, 235)

    mw, mh = 240, 70

    # Mouth cavity
    draw.ellipse([cx - mw, cy - mh, cx + mw, cy + mh], fill=mouth_cavity)

    # Upper teeth - large smile
    draw.rounded_rectangle([cx - 205, cy - 55, cx + 205, cy + 4],
                          radius=9, fill=teeth)
    
    # Individual teeth with shine
    for i in range(-8, 9):
        tooth_x = cx + i * 47
        if -8 <= i <= 8:
            # Separator line
            draw.line([(tooth_x, cy - 55), (tooth_x, cy + 4)], 
                     fill=teeth_line, width=3)
            # Tooth shine
            draw.rectangle([tooth_x - 17, cy - 53, tooth_x - 9, cy - 35], 
                          fill=(255, 255, 255, 200))

    # Lower teeth
    draw.ellipse([cx - 185, cy + 8, cx + 185, cy + 45], fill=teeth_lower)

    # Modern lips with gradient
    draw.ellipse([cx - mw - 9, cy - mh - 9, cx + mw + 9, cy + mh + 9],
                 outline=lip_outline, width=20)
    draw.ellipse([cx - mw - 3, cy - mh - 3, cx + mw + 3, cy + mh + 3],
                 outline=lip_fill, width=11)
    draw.arc([cx - mw + 10, cy - mh - 7, cx + mw - 10, cy - 2],
             start=180, end=360, fill=lip_highlight, width=7)

    img = img.resize(size, Image.Resampling.LANCZOS)
    if output_path:
        img.save(output_path)
    return img


def generate_all_assets(force: bool = False) -> None:
    """Generate all modern high-quality assets."""
    assets_dir = get_assets_dir()
    assets_dir.mkdir(exist_ok=True)

    assets = [
        ("base.png", generate_base_character, (512, 512)),
        ("mouth_closed.png", generate_mouth_closed, (256, 128)),
        ("mouth_A.png", generate_mouth_a, (256, 128)),
        ("mouth_O.png", generate_mouth_o, (256, 128)),
        ("mouth_E.png", generate_mouth_e, (256, 128)),
    ]

    print("=== Modern Asset Generation (6x Supersampling) ===")
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
    missing = [asset for asset in required_assets 
               if not (assets_dir / asset).exists()]

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