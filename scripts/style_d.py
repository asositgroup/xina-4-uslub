"""D — Kundalik: qog'oz qaydlar, lavanda skotch, chek-list, polaroid, yirtilgan qog'oz o'tishlari."""
import random

from common import chunks, split_acc, icon, NAIL_DIAGRAM, subs_js

NOTE, PAPER, INK, TAPE, RED = "#fbf7ef", "#efe7da", "#2c2433", "#b8a3e8", "#b23a48"
FACES = ["Caveat", "DMSerif", "Karla"]
TEAR = [6.13, 20.2, 32.47, 49.8]

CSS = f"""
#cam {{ filter: sepia(.12) saturate(.96) contrast(1.03); }}
#grain {{ position: absolute; inset: 0; background: url("assets/grain.png") repeat 0 0 / 512px 512px; opacity: .55; mix-blend-mode: multiply; }}
.ic {{ fill: none; stroke: {INK}; stroke-width: 5.5; stroke-linecap: round; stroke-linejoin: round; }}
.note {{ position: absolute; background-color: {NOTE}; background-image: url("assets/grain.png"); background-size: 512px 512px; box-shadow: 0 14px 34px rgba(40,28,20,.28); }}
.note.lav {{ background-color: #e8def9; }}
.tape {{ position: absolute; height: 54px; background: repeating-linear-gradient(135deg, rgba(184,163,232,.85) 0 16px, rgba(200,183,240,.85) 16px 32px); box-shadow: 0 2px 6px rgba(0,0,0,.12); }}
.hand {{ font-family: "Caveat"; font-weight: 700; color: {INK}; white-space: nowrap; line-height: 1.05; }}
.hand2 {{ font-family: "Caveat"; font-weight: 600; color: #5b4b78; white-space: nowrap; line-height: 1.05; }}
.kl {{ font-family: "Karla"; font-weight: 700; color: #5b4b78; letter-spacing: .14em; text-transform: uppercase; white-space: nowrap; }}
.box {{ position: absolute; width: 64px; height: 64px; border: 5px solid {INK}; border-radius: 10px; }}
.box svg {{ position: absolute; left: -8px; top: -14px; width: 84px; height: 84px; overflow: visible; }}
.box svg path {{ fill: none; stroke: {RED}; stroke-width: 9; stroke-linecap: round; stroke-linejoin: round; }}
.stamp {{ position: absolute; border-radius: 50%; border: 5px solid {RED}; color: {RED}; display: grid; place-items: center; text-align: center;
  font-family: "Karla"; font-weight: 700; letter-spacing: .1em; background: rgba(251,247,239,.4); }}
.stamp::before {{ content: ""; position: absolute; inset: 9px; border-radius: 50%; border: 2px dashed rgba(178,58,72,.7); }}
.strip {{ position: absolute; left: 0; top: 0; width: 1080px; background-color: {NOTE}; background-image: url("assets/grain.png"); background-size: 512px 512px;
  filter: drop-shadow(0 10px 18px rgba(40,28,20,.25)); }}
.sub .t {{ display: inline-block; font-family: "Karla"; font-weight: 700; font-size: 46px; line-height: 1.25; color: {INK};
  background-color: {NOTE}; background-image: url("assets/grain.png"); background-size: 512px 512px; padding: 8px 26px 12px; box-shadow: 0 8px 22px rgba(40,28,20,.28); }}
.sub .h {{ font-family: "Caveat"; font-weight: 700; font-size: 64px; color: #6a4fb0; line-height: .9; margin: 0 6px; }}
.tear {{ position: absolute; left: 0; top: 0; width: 1080px; height: 2400px; z-index: 55; background-color: {PAPER}; background-image: url("assets/grain.png"); background-size: 512px 512px;
  box-shadow: 0 -10px 30px rgba(0,0,0,.25); }}
.nd .nd-ln {{ fill: none; stroke: {INK}; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; }}
.nd .nd-fill {{ fill: #3a1d10; }}
.pol {{ position: absolute; background: #fff; box-shadow: 0 18px 40px rgba(40,28,20,.3); }}
.pol img {{ position: absolute; left: 18px; top: 18px; object-fit: cover; }}
.dots {{ background-image: radial-gradient(circle, rgba(60,40,80,.16) 2.2px, transparent 2.6px), url("assets/grain.png"); background-size: 48px 48px, 512px 512px; }}
#end {{ background-color: {PAPER}; }}
"""


def jag(w, h, top=True, bottom=True, seed=3, step=36, amp=26):
    rnd = random.Random(seed)
    pts = []
    if top:
        pts += [f"{x}px {8 + rnd.random() * amp:.0f}px" for x in range(0, w + 1, step)]
    else:
        pts += ["0px 0px", f"{w}px 0px"]
    if bottom:
        pts += [f"{x}px {h - 8 - rnd.random() * amp:.0f}px" for x in range(w, -1, -step)]
    else:
        pts += [f"{w}px {h}px", f"0px {h}px"]
    return "polygon(" + ",".join(pts) + ")"


def checkbox(id_, x, y):
    return f'<div class="box" id="{id_}" style="left:{x}px;top:{y}px"><svg viewBox="0 0 84 84"><path d="M10 44 L32 66 L78 8"/></svg></div>'


def card(id_, x, y, w, h, rot, inner, tape_x=None, lav=False):
    tx = tape_x if tape_x is not None else w // 2 - 110
    return (f'<div class="note ov{" lav" if lav else ""}" id="{id_}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">'
            f'{inner}<div class="tape" style="left:{tx}px;top:-28px;width:220px;transform:rotate({-rot * 1.6 + 3:.1f}deg)"></div></div>')


def card_js(id_, t0, t1, rot, kids=()):
    js = f'tl.fromTo("#{id_}", {{opacity:0, y:46, rotation:{rot - 4}, filter:"blur(12px)"}}, {{opacity:1, y:0, rotation:{rot}, filter:"blur(0px)", duration:0.8, ease:IN}}, {t0:.2f});\n'
    for sel, dt, kind in kids:
        if kind == "write":
            js += f'tl.fromTo("{sel}", {{clipPath:"inset(-20% 100% -20% 0%)"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:0.9, ease:"power1.inOut"}}, {t0 + dt:.2f});\n'
        elif kind == "check":
            js += f'draw("{sel} path", {t0 + dt:.2f}, 0.55);\n'
        elif kind == "draw":
            js += f'draw("{sel} path, {sel} circle", {t0 + dt:.2f}, 0.9, 0.12);\n'
        else:
            js += f'enter("{sel}", {t0 + dt:.2f}, {kind});\n'
    js += f'tl.to("#{id_}", {{opacity:0, y:-24, filter:"blur(8px)", duration:0.55, ease:IO}}, {t1:.2f});\n'
    return js


def build():
    subs = []
    rnd = random.Random(11)
    for c in chunks():
        a, acc, b = split_acc(c["text"], c["acc"])
        mid = f'<span class="h">{acc}</span>' if acc else ""
        r = (rnd.random() - 0.5) * 2.0
        subs.append(f'<div class="sub ov" id="sb{c["i"]}" style="top:{c["y"] - 36}px"><span class="t" style="transform:rotate({r:.2f}deg)">{a}{mid}{b}</span></div>')
    # subtitr chiziqlari uchun clip-path kengligi matnga emas, 1200 px ga — inline-block'dan chetga chiqmaydi (o'ng chet tekis qoladi)

    body = f"""
<div id="grain" class="layer"></div>

<!-- HOOK -->
{card("hc", 56, 70, 680, 270, -2.5, '''
<div class="abs hand" id="h1" style="left:40px;top:40px;font-size:70px">Tirnoq tishlash odatimni</div>
<div class="abs hand2" id="h2" style="left:40px;top:136px;font-size:66px">17 yoshimda tashlaganman</div>''')}
<div class="stamp ov" id="hs" style="left:790px;top:70px;width:220px;height:220px;font-size:30px;line-height:1.25">3<br>LAYFXAK<br><span style="font-size:20px">XINA SIREN</span></div>

<!-- 1 -->
{card("c1", 56, 64, 660, 210, -2, f'''
{checkbox("c1b", 38, 70)}
<div class="abs hand" id="c1t" style="left:130px;top:56px;font-size:80px">1. Halol manikyur</div>''')}
{card("c1n", 770, 70, 250, 250, 3, f'<div class="abs" id="c1i" style="left:60px;top:46px;width:130px;height:130px">{icon("nail")}</div><div class="abs hand2" id="c1il" style="left:0;width:250px;text-align:center;top:176px;font-size:46px">toza = ✓</div>', lav=True)}

<!-- sabab -->
<div class="strip ov" id="cy" style="height:320px;clip-path:{jag(1080, 320, top=False, seed=5)}">
<div class="abs" id="cy1" style="left:110px;top:34px;width:130px;height:130px">{icon("nail_bitten")}</div>
<div class="abs hand" id="cy1l" style="left:60px;width:230px;text-align:center;top:166px;font-size:54px">tishlash</div>
<div class="abs" id="cy2" style="left:475px;top:34px;width:130px;height:130px">{icon("nail_crack")}</div>
<div class="abs hand" id="cy2l" style="left:415px;width:250px;text-align:center;top:160px;font-size:64px;color:{RED}">mo'rt</div>
<div class="abs" id="cy3" style="left:840px;top:34px;width:130px;height:130px">{icon("loop")}</div>
<div class="abs hand" id="cy3l" style="left:770px;width:270px;text-align:center;top:166px;font-size:50px">yana tishlash</div>
<svg class="layer" id="cyar" viewBox="0 0 1080 1920"><g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
<path d="M285 104 C 330 84 390 120 432 96"/><path d="M416 84 L434 96 L416 110"/><path d="M650 104 C 695 84 755 120 797 96"/><path d="M781 84 L799 96 L781 110"/></g></svg>
</div>

<!-- 2 -->
{card("c2", 56, 50, 680, 200, -1.5, f'''
{checkbox("c2b", 38, 66)}
<div class="abs hand" id="c2t" style="left:130px;top:52px;font-size:80px">2. Mustahkamlik</div>''')}
{card("c2n", 790, 56, 230, 230, 4, f'<div class="abs" id="c2i" style="left:50px;top:40px;width:130px;height:130px">{icon("shield")}</div>', lav=True)}
{card("bwc", 56, 46, 960, 250, -1, f'''
<div class="abs" id="bw" style="left:40px;top:40px;width:150px;height:150px">{icon("bowl")}</div>
<div class="abs hand" id="bwl" style="left:200px;top:70px;font-size:66px">tuzli suv</div>
<div class="abs" id="ck" style="left:470px;top:50px;width:130px;height:130px">{icon("clock")}</div>
<div class="abs" id="ckn" style="left:620px;top:46px;font-family:DMSerif;font-size:110px;line-height:1;color:{INK}">10–15</div>
<div class="abs hand2" id="ckl" style="left:640px;top:166px;font-size:52px">minut, bir kunda</div>
<svg class="layer" id="ckc" viewBox="0 0 960 250" style="width:960px;height:250px"><path d="M600 60 C 620 20 900 16 905 92 C 910 160 640 168 606 120 C 592 98 600 70 640 50" fill="none" stroke="{RED}" stroke-width="5" stroke-linecap="round"/></svg>''')}
{card("e1", 160, 50, 300, 250, -3, f'''<div class="abs kl" style="left:22px;top:22px;font-size:22px">20</div>
<div class="abs" style="left:0;width:300px;text-align:center;top:46px;font-family:DMSerif;font-size:110px;color:{INK};line-height:1">Ca</div>
<div class="abs hand2" style="left:0;width:300px;text-align:center;top:166px;font-size:54px">kalsiy</div>''')}
{card("e2", 620, 56, 300, 250, 3, f'''<div class="abs kl" style="left:22px;top:22px;font-size:22px">30</div>
<div class="abs" style="left:0;width:300px;text-align:center;top:46px;font-family:DMSerif;font-size:110px;color:{INK};line-height:1">Zn</div>
<div class="abs hand2" style="left:0;width:300px;text-align:center;top:166px;font-size:54px">sink</div>''', lav=True)}
<div class="abs hand ov" id="elp" style="left:490px;width:100px;text-align:center;top:120px;font-size:110px">+</div>

<!-- 3: chek-list -->
{card("c3", 150, 70, 780, 560, -1.5, f'''
<div class="abs kl" style="left:52px;top:44px;font-size:24px">Kundalik · 3 layfxak</div>
{checkbox("l1b", 52, 120)}<div class="abs hand" style="left:150px;top:106px;font-size:76px">Halol manikyur</div>
{checkbox("l2b", 52, 260)}<div class="abs hand" style="left:150px;top:246px;font-size:76px">Mustahkamlik</div>
{checkbox("l3b", 52, 400)}<div class="abs hand" id="l3t" style="left:150px;top:386px;font-size:76px">Xina qo'ying</div>
<div class="abs" id="l3i" style="left:600px;top:360px;width:110px;height:150px">{icon("cone")}</div>''', tape_x=280)}
{card("ndc", 190, 44, 720, 600, 1.5, f'''
<div class="abs" id="nd" style="left:110px;top:56px;width:400px;height:510px">{NAIL_DIAGRAM}</div>
<div class="abs hand2" id="ndl1" style="left:480px;top:66px;font-size:50px">o'sgan qism</div>''', tape_x=250)}
{card("ndn", 40, 100, 220, 230, -4, f'<div class="abs" id="ndeye" style="left:45px;top:36px;width:130px;height:130px">{icon("eye_off")}</div><div class="abs hand2" style="left:0;width:220px;text-align:center;top:164px;font-size:46px">ko&#39;rinmaydi</div>', lav=True)}
<div class="abs hand ov" id="ndl3" style="left:740px;top:430px;font-size:70px;color:{RED};transform:rotate(-6deg)">bekitadi!</div>
{card("ch1", 120, 210, 380, 160, -3, f'<div class="abs" style="left:28px;top:30px;width:100px;height:100px">{icon("shield")}</div><div class="abs hand" style="left:140px;top:40px;font-size:66px">mustahkam</div>')}
{card("ch2", 580, 220, 380, 160, 2.5, f'<div class="abs" style="left:28px;top:30px;width:100px;height:100px">{icon("arrow_up")}</div><div class="abs hand" style="left:140px;top:40px;font-size:66px">o&#39;sadi</div>', lav=True)}

<!-- CTA -->
<div class="pol ov" id="pol" style="left:110px;top:150px;width:260px;height:320px;transform:rotate(-4deg)"><img src="assets/avatar.jpg" alt="" style="width:224px;height:224px"><div class="abs hand2" style="left:0;width:260px;text-align:center;top:250px;font-size:44px">@xina_siren</div>
<div class="tape" style="left:40px;top:-26px;width:180px;transform:rotate(6deg)"></div></div>
{card("ctc", 420, 190, 560, 250, 2, f'''
<div class="abs hand" style="left:40px;top:34px;font-size:72px">Sahifamga</div>
{checkbox("ctb", 44, 140)}<div class="abs hand" style="left:140px;top:126px;font-size:72px">obuna bo'ling</div>''', tape_x=170)}
{card("plc", 80, 150, 920, 320, -1.5, f'''
<div class="abs hand" style="left:56px;top:44px;font-size:76px">do'stingizga yuboring</div>
<svg class="layer" id="plpath" viewBox="0 0 920 320" style="width:920px;height:320px"><path d="M80 250 C 280 160 480 300 700 190" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 16"/></svg>
<div class="abs" id="pl" style="left:690px;top:120px;width:130px;height:130px">{icon("plane")}</div>''', tape_x=350)}

<!-- SUBTITRLAR -->
{chr(10).join(subs)}

<!-- YIRTIQ QOG'OZ -->
{''.join(f'<div class="tear" id="tr{i}" style="clip-path:{jag(1080, 2400, seed=20 + i)}"></div>' for i in range(len(TEAR)))}

<!-- YAKUN -->
<div class="layer ov dots" id="end" style="z-index:60">
  <div class="pol" id="epol" style="left:380px;top:420px;width:320px;height:390px;transform:rotate(-3deg)"><img src="assets/avatar.jpg" alt="" style="width:284px;height:284px">
  <div class="abs hand2" style="left:0;width:320px;text-align:center;top:310px;font-size:50px">@xina_siren</div>
  <div class="tape" style="left:70px;top:-26px;width:180px;transform:rotate(5deg)"></div></div>
  <div class="abs hand" id="ent" style="left:0;width:1080px;text-align:center;top:860px;font-size:130px">Xina Siren</div>
  <div class="abs kl" id="enk" style="left:0;width:1080px;text-align:center;top:1020px;font-size:28px">halol xina · manikyur · toshkent</div>
  <div class="abs kl" id="enp" style="left:0;width:1080px;text-align:center;top:1074px;font-size:32px;color:{INK}">+998 33 712 26 07</div>
  <div class="stamp" id="ens" style="left:760px;top:360px;width:200px;height:200px;font-size:26px;line-height:1.25;transform:rotate(12deg)">HALOL<br><span style="font-size:20px">XINA SIREN</span></div>
</div>
"""

    tear_js = "\n".join(
        f'tl.fromTo("#tr{i}", {{y:1960}}, {{y:-220, duration:0.7, ease:"power2.in"}}, {t - 0.7:.2f});\n'
        f'tl.to("#tr{i}", {{y:-2500, duration:0.85, ease:"power2.out"}}, {t + 0.01:.2f});'
        for i, t in enumerate(TEAR))

    js = f"""
// ---------- HOOK ----------
{card_js("hc", 0.2, 5.35, -2.5, [("#h1", 0.55, "write"), ("#h2", 1.35, "write")])}
tl.fromTo("#hs", {{opacity:0, scale:1.15, rotation:20, filter:"blur(8px)"}}, {{opacity:0.92, scale:1, rotation:12, filter:"blur(0px)", duration:0.5, ease:"power3.out"}}, 2.3);
exit("#hs", 5.35, 0.55);

// ---------- 1 ----------
{card_js("c1", 6.5, 14.2, -2, [("#c1t", 0.45, "write"), ("#c1b", 2.6, "check")])}
{card_js("c1n", 10.4, 14.2, 3, [("#c1i", 0.3, "draw"), ("#c1il", 0.9, "write")])}

// ---------- sabab ----------
tl.fromTo("#cy", {{opacity:1, y:-340}}, {{y:0, duration:0.85, ease:IN}}, 14.95);
tl.fromTo("#cy1, #cy2, #cy3, #cyar", {{opacity:0}}, {{opacity:1, duration:0.01}}, 15.0);
draw("#cy1 path", 15.2, 0.8, 0.15);
tl.fromTo("#cy1l", {{clipPath:"inset(-20% 100% -20% 0%)"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:0.7, ease:"power1.inOut"}}, 15.5);
draw("#cyar path:nth-child(1), #cyar path:nth-child(2)", 15.9, 0.45, 0.2);
draw("#cy2 path", 16.35, 0.8, 0.15);
tl.fromTo("#cy2l", {{clipPath:"inset(-20% 100% -20% 0%)"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:0.7, ease:"power1.inOut"}}, 16.8);
draw("#cyar path:nth-child(3), #cyar path:nth-child(4)", 17.7, 0.45, 0.2);
draw("#cy3 path", 18.1, 0.8, 0.2);
tl.fromTo("#cy3l", {{clipPath:"inset(-20% 100% -20% 0%)"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:0.8, ease:"power1.inOut"}}, 18.5);
tl.to("#cy", {{y:-60, opacity:0, filter:"blur(8px)", duration:0.55, ease:IO}}, 19.4);

// ---------- 2 ----------
{card_js("c2", 20.55, 24.35, -1.5, [("#c2t", 0.45, "write"), ("#c2b", 3.0, "check")])}
{card_js("c2n", 21.2, 24.35, 4, [("#c2i", 0.3, "draw")])}
{card_js("bwc", 24.7, 28.4, -1, [("#bw", 0.25, "draw"), ("#bwl", 0.6, "write"), ("#ck", 1.2, "draw"), ("#ckn", 2.0, "{y:16, b:10, s:1.05, d:0.8}"), ("#ckl", 2.3, "write"), ("#ckc", 2.6, "draw")])}
{card_js("e1", 29.7, 31.6, -3)}
tl.fromTo("#elp", {{opacity:0, scale:0.8, filter:"blur(8px)"}}, {{opacity:1, scale:1, filter:"blur(0px)", duration:0.6, ease:IN}}, 30.2);
exit("#elp", 31.6, 0.5);
{card_js("e2", 30.4, 31.6, 3)}

// ---------- 3 ----------
{card_js("c3", 32.85, 35.35, -1.5, [("#l1b", 0.5, "check"), ("#l2b", 0.85, "check"), ("#l3t", 1.1, "write"), ("#l3b", 1.9, "check"), ("#l3i", 1.5, "draw")])}
{card_js("ndc", 35.55, 44.25, 1.5, [("#ndl1", 1.7, "write")])}
draw("#nd .nd-finger", 35.85, 1.1); draw("#nd .nd-nail", 36.35, 1.0);
tl.fromTo("#nd .nd-cut", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 37.0);
draw("#nd .nd-dim", 37.1, 0.6);
{card_js("ndn", 38.0, 40.6, -4, [("#ndeye", 0.3, "draw")])}
tl.fromTo("#nd .nd-fill", {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:1.3, ease:"power2.inOut"}}, 42.5);
tl.fromTo("#ndl3", {{opacity:0, clipPath:"inset(-20% 100% -20% 0%)"}}, {{opacity:1, clipPath:"inset(-20% 0% -20% 0%)", duration:0.8, ease:"power1.inOut"}}, 42.8);
exit("#ndl3", 44.25, 0.5);
{card_js("ch1", 46.75, 49.25, -3)}
{card_js("ch2", 48.35, 49.25, 2.5)}

// ---------- CTA ----------
tl.fromTo("#pol", {{opacity:0, y:60, rotation:-9, filter:"blur(12px)"}}, {{opacity:1, y:0, rotation:-4, filter:"blur(0px)", duration:0.9, ease:IN}}, 50.4);
exit("#pol", 55.05, 0.5);
{card_js("ctc", 50.9, 55.05, 2, [("#ctb", 2.9, "check")])}
{card_js("plc", 55.25, 58.45, -1.5)}
tl.fromTo("#plpath", {{clipPath:"inset(0% 100% 0% 0%)"}}, {{clipPath:"inset(0% 0% 0% 0%)", duration:1.2, ease:IO}}, 56.0);
tl.fromTo("#pl", {{opacity:0}}, {{opacity:1, duration:0.01}}, 57.2); draw("#pl path", 57.2, 0.8, 0.2);
tl.fromTo("#pl", {{x:-50, y:30}}, {{x:20, y:-10, duration:1.3, ease:"sine.inOut"}}, 57.2);

// ---------- YIRTIQ QOG'OZ ----------
{tear_js}

// ---------- SUBTITR ----------
{subs_js()}

// ---------- YAKUN ----------
tl.fromTo("#end", {{opacity:0}}, {{opacity:1, duration:0.6, ease:"sine.inOut"}}, 58.75);
tl.fromTo("#epol", {{opacity:0, y:60, rotation:-8, filter:"blur(12px)"}}, {{opacity:1, y:0, rotation:-3, filter:"blur(0px)", duration:0.9, ease:IN}}, 58.95);
tl.fromTo("#ent", {{clipPath:"inset(-20% 100% -20% 0%)"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:1.0, ease:"power1.inOut"}}, 59.3);
enter("#enk", 59.6, {{y:12, b:6, d:0.6}});
enter("#enp", 59.75, {{y:12, b:6, d:0.6}});
tl.fromTo("#ens", {{opacity:0, scale:1.15, rotation:20, filter:"blur(8px)"}}, {{opacity:0.9, scale:1, rotation:12, filter:"blur(0px)", duration:0.5, ease:"power3.out"}}, 59.9);
"""
    sfx_extra = [(t - 0.05, "select_click.wav", 0.45) for t in (2.3, 59.9)]
    return dict(faces=FACES, css=CSS, body=body, js=js, bg=PAPER, sweeps=TEAR, sfx="air_woosh.wav", sfx_gain=0.4,
                sfx_lead=1.0, sfx_extra=sfx_extra, assets=["grain.png"])
