"""make_textures.py [out_dir] — C va D uslublari teksturalarini qayta yasaydi (assets/textures ga tayyorlari bor).

guil.png  (1080x700)  — C: banknota uslubidagi gilosh to'lqin chiziqlari, lavanda #7C5EC8, shaffof fon.
micro.png (~3050x20)  — C: mikromatn qatori «XINA SIREN • HALOL • ORIGINAL •» (JetBrains Mono). Matn sifatida emas, RASM
                         sifatida — hyperframes check matn chetdan chiqqanini xato deb ko'radi.
grain.png (512x512)   — D: qog'oz donadorligi (multiply bilan).
"""
import math
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.ndimage import gaussian_filter

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "textures")
os.makedirs(out, exist_ok=True)
fonts = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "fonts")

# guilloche
W, H, S = 1080, 700, 2
im = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
d = ImageDraw.Draw(im)
for k in range(26):
    pts = []
    for x in range(0, W + 1, 3):
        u = x / W * math.pi * 2
        y = H * 0.5 + H * 0.36 * math.sin(u * 3 + k * 0.3) * math.cos(u * 0.5 + k * 0.17) + H * 0.05 * math.sin(x / 52 + k * 0.9)
        pts.append((x * S, y * S))
    d.line(pts, fill=(124, 94, 200, 110 if k % 3 == 0 else 62), width=2 * S // 2 + 1, joint="curve")
im.resize((W, H), Image.LANCZOS).save(os.path.join(out, "guil.png"))

# microtext
f = ImageFont.truetype(os.path.join(fonts, "JetBrainsMono-var.ttf"), 26)
try:
    f.set_variation_by_axes([500])
except Exception:
    pass
txt = "XINA SIREN  •  HALOL  •  ORIGINAL  •  " * 10
w = int(f.getlength(txt)) + 20
m = Image.new("RGBA", (w, 40), (0, 0, 0, 0))
ImageDraw.Draw(m).text((0, 4), txt, font=f, fill=(42, 29, 68, 150))
m.resize((w // 2, 20), Image.LANCZOS).save(os.path.join(out, "micro.png"))

# paper grain
rng = np.random.default_rng(7)
n = 0.7 * rng.normal(0, 1, (512, 512)) + 0.3 * gaussian_filter(rng.normal(0, 1, (512, 512)), 2) * 3
n = (n - n.min()) / (n.max() - n.min())
a = (np.abs(n - 0.5) * 2 * 70).astype(np.uint8)
rgba = np.zeros((512, 512, 4), np.uint8)
rgba[..., 0], rgba[..., 1], rgba[..., 2], rgba[..., 3] = 70, 55, 40, a
Image.fromarray(rgba).save(os.path.join(out, "grain.png"))
print("teksturalar ->", out)
