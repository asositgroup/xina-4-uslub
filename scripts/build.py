"""build.py [--project DIR] A B C D — har uslub uchun <DIR>/hf_<X>/ HyperFrames loyihasini yig'adi.

Loyiha papkasi (DIR) da bo'lishi kerak: project.json, words json (MMS alignment), media (project.json → media):
  base  — 1080x1920 asosiy video (retush qilingan), voice — toza ovoz (Auphonic), avatar — Instagram avatar.
Skill'dan olinadi: shriftlar, GSAP, teksturalar, SFX.
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser()
ap.add_argument("--project", default=os.environ.get("XS_PROJECT", str(SKILL / "example" / "xina-tirnoq")))
ap.add_argument("letters", nargs="*", default=["A", "B", "C", "D"])
args = ap.parse_args()
PROJECT = Path(args.project).expanduser().resolve()
os.environ["XS_PROJECT"] = str(PROJECT)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import common  # noqa: E402  (XS_PROJECT o'rnatilgandan keyin)

SFXDIR = SKILL / "assets" / "sfx"
HFV = "0.8.171"
CFG = common.CFG


def link(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    try:
        os.link(src, dst)
    except OSError:  # boshqa disk bo'lsa — nusxa
        import shutil
        shutil.copy2(src, dst)


def sfx_track(out, cues):
    """cues: [(t, file, gain)] -> bitta wav (DUR uzunlikda)."""
    a = ["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "lavfi", "-t", str(common.DUR), "-i", "anullsrc=r=48000:cl=stereo"]
    filt, labels = [], ["[0:a]"]
    for k, (t, f, g) in enumerate(cues, start=1):
        a += ["-i", str(SFXDIR / f)]
        ms = max(0, int(round(t * 1000)))
        filt.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,volume={g},adelay={ms}|{ms}[s{k}]")
        labels.append(f"[s{k}]")
    filt.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=first[out]")
    a += ["-filter_complex", ";".join(filt), "-map", "[out]", "-c:a", "pcm_s16le", str(out)]
    subprocess.run(a, check=True)


def build(letter):
    mod = __import__(f"style_{letter.lower()}")
    st = mod.build()
    hf = PROJECT / f"hf_{letter}"
    (hf / "assets").mkdir(parents=True, exist_ok=True)
    m = CFG["media"]
    link(PROJECT / m["base"], hf / "assets/base.mp4")
    link(PROJECT / m["voice"], hf / "assets/voice.wav")
    link(PROJECT / m["avatar"], hf / "assets/avatar.jpg")
    link(SKILL / "assets/gsap.min.js", hf / "assets/gsap.min.js")
    for f in (SKILL / "assets/fonts").glob("*.ttf"):
        link(f, hf / "assets/fonts" / f.name)
    for extra in st.get("assets", []):
        link(SKILL / "assets/textures" / extra, hf / "assets" / extra)
    cues = [(t - st.get("sfx_lead", 0.0), st["sfx"], st["sfx_gain"]) for t in st["sweeps"]]
    cues += st.get("sfx_extra", [])
    sfx_track(hf / "assets/sfx.wav", cues)
    html = common.page(f"{CFG.get('name', 'video')} — {letter}", st["faces"], st["css"], st["body"], st["js"], st.get("bg", "#000"))
    (hf / "index.html").write_text(html, encoding="utf-8")
    (hf / "hyperframes.json").write_text(json.dumps({
        "$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
        "paths": {"blocks": "compositions", "components": "compositions/components", "assets": "assets"},
        "authoringSkill": "general-video"}, indent=2))
    (hf / "package.json").write_text(json.dumps({"name": f"xs-{letter.lower()}", "private": True, "type": "module",
        "scripts": {k: f"npx --yes hyperframes@{HFV} {k}" for k in ("preview", "check", "render")}}, indent=2))
    print(f"{letter}: {hf}/index.html ({len(html) // 1024} KB)")


if __name__ == "__main__":
    for L in args.letters:
        build(L)
