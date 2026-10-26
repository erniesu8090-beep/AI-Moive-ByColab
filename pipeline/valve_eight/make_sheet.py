import json
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
REPO = (HERE / "../..").resolve()
sys.path.insert(0, str(REPO / "tools"))
from fonts import font

first_dir = HERE / "out" / "first"
masters_dir = HERE / "out" / "masters"

def generate_sheet():
    shots = [f"S{i:02d}.png" for i in range(1, 14)]
    files = [first_dir / s for s in shots if (first_dir / s).exists()]
    if not files:
        print("No shot files found yet.", flush=True)
        return

    cols = 3
    W, H = 672, 384  # 16:9
    rows = (len(files) + cols - 1) // cols
    im = Image.new("RGB", (W * cols, H * rows), color=(20, 20, 20))
    f = ImageFont.truetype(font("jhbd"), 28)

    for i, p in enumerate(files):
        try:
            t = Image.open(p).convert("RGB").resize((W, H))
            draw = ImageDraw.Draw(t)
            draw.text((12, 10), p.stem, font=f, fill=(255, 255, 0), stroke_width=3, stroke_fill=(0, 0, 0))
            im.paste(t, ((i % cols) * W, (i // cols) * H))
        except Exception as e:
            print(f"Error reading {p}: {e}", flush=True)

    dst = first_dir / "_sheet.jpg"
    im.save(dst, quality=88)
    print(f"Sheet generated at: {dst} ({len(files)} shots)", flush=True)

if __name__ == "__main__":
    generate_sheet()
