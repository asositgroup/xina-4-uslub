"""A — Xina chizig'i: hamma grafika xina konusidan chiqqandek chiziladi; chiziq yangi pasta rangidan dog' rangiga o'tadi."""
from common import chunks, split_acc, icon, NAIL_DIAGRAM, subs_js
from textw import tw

PASTE, STAIN, CREAM, LAV = "#7d6a2e", "#2a150c", "#f3e7da", "#c7aef7"
FACES = ["Pinyon", "Cormorant", "CormorantI", "Manrope"]

CSS = f"""
.ic {{ fill: none; stroke: {STAIN}; stroke-width: 5.5; stroke-linecap: round; stroke-linejoin: round; }}
.scrim {{ position: absolute; left: 0; top: 0; width: 1080px; background: linear-gradient(180deg, rgba(246,238,228,.95) 0%, rgba(246,238,228,.88) 62%, rgba(246,238,228,.45) 82%, rgba(246,238,228,0) 100%); }}
.kick {{ font-family: "Manrope"; font-weight: 800; font-size: 30px; letter-spacing: .3em; color: {STAIN}; white-space: nowrap; }}
.scr {{ font-family: "Pinyon"; color: {STAIN}; white-space: nowrap; line-height: 1.25; padding: 0 30px 0 8px; }}
.num {{ font-family: "Cormorant"; font-weight: 600; color: {STAIN}; line-height: 1; text-align: center; }}
.lab {{ font-family: "Manrope"; font-weight: 700; color: {STAIN}; white-space: nowrap; }}
.tip {{ position: absolute; width: 26px; height: 26px; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #7a5530, {STAIN} 70%); box-shadow: 0 4px 10px rgba(42,21,12,.45); }}
.ring circle {{ fill: {STAIN}; }}
.sweep path {{ fill: none; stroke-linecap: round; }}
.sub .t {{ display: inline-block; font-family: "Manrope"; font-weight: 700; font-size: 52px; line-height: 1.2; color: {STAIN};
  background: rgba(247,240,231,.93); padding: 10px 26px 12px; border-radius: 18px; box-shadow: 0 10px 30px rgba(42,21,12,.18); }}
.sub .u {{ background-image: linear-gradient(#9a7be0, #9a7be0); background-repeat: no-repeat; background-position: 0 96%; background-size: 0% 6px; padding-bottom: 2px; }}
.vine path {{ fill: none; stroke: {STAIN}; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }}
.vine circle {{ fill: {STAIN}; }}
.nd .nd-ln {{ fill: none; stroke: {STAIN}; stroke-width: 6; stroke-linecap: round; stroke-linejoin: round; }}
.nd .nd-fill {{ fill: #3a1d10; }}
.pill {{ position: absolute; display: flex; align-items: center; gap: 22px; padding: 18px 34px 18px 22px; border: 4px solid {STAIN}; border-radius: 80px; background: rgba(246,238,228,.9); }}
.pill .ic {{ width: 66px; height: 66px; }}
.prof {{ position: absolute; left: 110px; top: 210px; width: 860px; height: 250px; border-radius: 40px; background: rgba(246,238,228,.95); box-shadow: 0 20px 50px rgba(42,21,12,.22); }}
.prof img {{ position: absolute; left: 40px; top: 45px; width: 160px; height: 160px; border-radius: 50%; object-fit: cover; outline: 4px solid {LAV}; outline-offset: 5px; }}
.prof .h {{ position: absolute; left: 236px; top: 52px; font-family: "Manrope"; font-weight: 800; font-size: 50px; color: {STAIN}; }}
.prof .d {{ position: absolute; left: 238px; top: 120px; font-family: "Manrope"; font-weight: 600; font-size: 28px; color: #6b5444; }}
.btn {{ position: absolute; left: 236px; top: 170px; width: 300px; height: 62px; border-radius: 40px; background: {STAIN}; color: #fff; font-family: "Manrope"; font-weight: 800; font-size: 28px; display: grid; place-items: center; }}
.btn span {{ grid-area: 1/1; }}
.btn .b2 {{ opacity: 0; }}
#end {{ background: {CREAM}; }}
"""


def ring(cx, cy, r, n, cls):
    import math
    dots = "".join(f'<circle cx="{cx + r * math.cos(-math.pi / 2 + 2 * math.pi * k / n):.1f}" '
                   f'cy="{cy + r * math.sin(-math.pi / 2 + 2 * math.pi * k / n):.1f}" r="{6 if k % 2 == 0 else 4}"/>'
                   for k in range(n))
    return f'<svg class="layer ring {cls}" viewBox="0 0 1080 1920">{dots}</svg>'


VINE_L = """<svg class="layer vine VID" viewBox="0 0 1080 1920"><g transform="translate(TX TY) scale(SC)">
<path d="M70 0 C150 80 20 160 95 240 S175 400 90 480 S20 630 105 710"/>
<path d="M118 130 C160 108 195 120 204 152 C172 162 140 157 118 130 Z"/>
<path d="M95 240 C140 210 185 225 196 262 C160 275 120 270 95 240 Z"/>
<path d="M70 365 C34 342 8 352 4 382 C30 394 56 388 70 365 Z"/>
<path d="M90 480 C130 450 168 462 176 496 C142 508 110 502 90 480 Z"/>
<path d="M100 605 C145 580 180 592 190 625 C155 636 122 630 100 605 Z"/>
<circle cx="138" cy="18" r="7"/><circle cx="154" cy="44" r="6"/><circle cx="40" cy="200" r="6"/><circle cx="146" cy="420" r="6"/><circle cx="56" cy="550" r="6"/>
</g></svg>"""


def vine(vid, tx, ty, sc=1.0, flip=False):
    s = VINE_L.replace("VID", vid).replace("TX", str(tx)).replace("TY", str(ty))
    s = s.replace("SC", f"{-sc} {sc}" if flip else str(sc))
    return s


def section(k, title, top, size=104, icon_name=None, scrim_top=0, scrim_h=360):
    w = tw("Pinyon", size, title)
    return f"""
<div class="scrim ov" id="s{k}scrim" style="top:{scrim_top}px;height:{scrim_h}px"></div>
{ring(150, top + 95, 82, 22, f"ov s{k}ring")}
<div class="abs num ov" id="s{k}num" style="left:100px;top:{top + 40}px;width:100px;font-size:110px">{k}</div>
<div class="abs scr ov" id="s{k}t" style="left:262px;top:{top + 18}px;font-size:{size}px">{title}</div>
""" + (f'<div class="abs ov" id="s{k}ic" style="left:{min(900, 262 + w + 40)}px;top:{top + 30}px;width:130px;height:130px">{icon(icon_name)}</div>' if icon_name else "")


def section_js(k, t0, t1, top, title, size=104, has_icon=False):
    w = tw("Pinyon", size, title)
    js = f"""
tl.fromTo("#s{k}scrim", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, {t0:.2f});
tl.fromTo(".s{k}ring circle", {{opacity:0, scale:0.4, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.45, ease:IN, stagger:0.025}}, {t0 + 0.05:.2f});
tl.set(".s{k}ring", {{opacity:1}}, {t0:.2f});
enter("#s{k}num", {t0 + 0.3:.2f}, {{y:16, b:10, s:0.9, d:0.7}});
tl.set("#s{k}t", {{opacity:1}}, {t0 + 0.45:.2f});
tl.fromTo("#s{k}t", {{clipPath:"inset(-20% 100% -20% 0%)", color:"{PASTE}"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:1.3, ease:"power1.inOut"}}, {t0 + 0.45:.2f});
tl.to("#s{k}t", {{color:"{STAIN}", duration:1.6, ease:"sine.inOut"}}, {t0 + 1.2:.2f});
"""
    if has_icon:
        js += f'tl.set("#s{k}ic", {{opacity:1}}, {t0 + 1.4:.2f}); draw("#s{k}ic path, #s{k}ic circle", {t0 + 1.4:.2f}, 0.9, 0.12);\n'
    js += f'exit([...document.querySelectorAll("#s{k}scrim, .s{k}ring, #s{k}num, #s{k}t{", #s" + str(k) + "ic" if has_icon else ""}")], {t1:.2f}, 0.55);\n'
    return js


def sweep_svg(i):
    return f"""<svg class="layer sweep" id="sw{i}" viewBox="0 0 1080 1920" style="z-index:40">
<defs><linearGradient id="hg{i}" x1="0" y1="1" x2="1" y2="0"><stop offset="0" stop-color="#4a2a16"/><stop offset=".5" stop-color="{STAIN}"/><stop offset="1" stop-color="#5a3420"/></linearGradient></defs>
<path d="M-140 1780 C 240 1560 200 1120 540 960 S 900 520 1240 180" stroke="url(#hg{i})" stroke-width="110"/></svg>"""


SWEEPS = [5.72, 19.86, 32.06, 49.40]


def build():
    ch = chunks()
    subs = []
    for c in ch:
        a, acc, b = split_acc(c["text"], c["acc"])
        mid = f'<span class="u">{acc}</span>' if acc else ""
        subs.append(f'<div class="sub ov" id="sb{c["i"]}" style="top:{c["y"] - 34}px"><span class="t">{a}{mid}{b}</span></div>')

    hook_w = tw("Pinyon", 150, "tashlash")
    body = f"""
<!-- HOOK -->
<div class="scrim ov" id="hscrim" style="height:420px"></div>
<div class="abs kick ov" id="hk" style="left:96px;top:78px">TIRNOQ TISHLASH ODATINI</div>
<div class="abs scr ov" id="ht" style="left:80px;top:105px;font-size:150px">tashlash</div>
<div class="tip ov" id="htip" style="left:92px;top:232px"></div>
{ring(870, 215, 98, 26, "ov hring")}
<div class="abs num ov" id="hn" style="left:820px;top:140px;width:100px;font-size:120px">3</div>
<div class="abs lab ov" id="hl" style="left:790px;top:256px;width:160px;text-align:center;font-size:26px;letter-spacing:.12em">LAYFXAK</div>
{vine("ov hv", 4, 440, 0.8)}

<!-- 1 -->
{section(1, "Halol manikyur", 92, 92)}
<div class="abs ov" id="s1nail" style="left:870px;top:110px;width:150px;height:150px">{icon("nail")}</div>
<div class="abs ov" id="s1chk" style="left:940px;top:190px;width:90px;height:90px">{icon("check")}</div>

<!-- sabab: yopiq doira -->
<div class="scrim ov" id="cyscrim" style="height:340px"></div>
<div class="abs ov" id="cy1" style="left:110px;top:40px;width:150px;height:150px">{icon("nail_bitten")}</div>
<div class="abs lab ov" id="cy1l" style="left:85px;top:196px;width:200px;text-align:center;font-size:34px">tishlash</div>
<div class="abs ov" id="cy2" style="left:465px;top:40px;width:150px;height:150px">{icon("nail_crack")}</div>
<div class="abs scr ov" id="cy2l" style="left:455px;top:178px;font-size:78px;padding:0 10px">mo'rt</div>
<div class="abs ov" id="cy3" style="left:820px;top:40px;width:150px;height:150px">{icon("loop")}</div>
<div class="abs lab ov" id="cy3l" style="left:760px;top:196px;width:270px;text-align:center;font-size:34px">oson tishlanadi</div>
<svg class="layer ov" id="cyar" viewBox="0 0 1080 1920"><g fill="none" stroke="{STAIN}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
<path d="M290 115 Q365 80 440 115"/><path d="M424 98 L442 116 L420 126"/>
<path d="M645 115 Q720 80 795 115"/><path d="M779 98 L797 116 L775 126"/>
<path d="M895 252 Q540 330 185 252"/><path d="M205 238 L183 253 L206 268"/></g></svg>

<!-- 2 -->
{section(2, "Mustahkamlik", 92, 104, "shield")}
<div class="scrim ov" id="bwscrim" style="height:340px"></div>
<div class="abs ov" id="bw" style="left:130px;top:30px;width:180px;height:180px">{icon("bowl")}</div>
<div class="abs lab ov" id="bwl" style="left:95px;top:214px;width:250px;text-align:center;font-size:36px">tuzli suv</div>
<div class="abs ov" id="ck" style="left:470px;top:40px;width:160px;height:160px">{icon("clock")}</div>
<div class="abs num ov" id="ckn" style="left:650px;top:50px;width:380px;font-size:140px;text-align:left">10–15</div>
<div class="abs lab ov" id="ckl" style="left:660px;top:206px;font-size:36px">minut · bir kunda</div>
<div class="scrim ov" id="elscrim" style="height:340px"></div>
<svg class="layer ov" id="eltiles" viewBox="0 0 1080 1920"><g fill="none" stroke="{STAIN}" stroke-width="5" stroke-linejoin="round">
<rect x="230" y="36" width="220" height="220" rx="22"/><rect x="630" y="36" width="220" height="220" rx="22"/></g></svg>
<div class="abs lab ov" id="el1n" style="left:250px;top:50px;font-size:30px">20</div>
<div class="abs num ov" id="el1" style="left:230px;top:78px;width:220px;font-size:108px">Ca</div>
<div class="abs lab ov" id="el1l" style="left:230px;top:200px;width:220px;text-align:center;font-size:32px">kalsiy</div>
<div class="abs lab ov" id="el2n" style="left:650px;top:50px;font-size:30px">30</div>
<div class="abs num ov" id="el2" style="left:630px;top:78px;width:220px;font-size:108px">Zn</div>
<div class="abs lab ov" id="el2l" style="left:630px;top:200px;width:220px;text-align:center;font-size:32px">sink</div>
<div class="abs num ov" id="elp" style="left:470px;top:84px;width:140px;font-size:100px">+</div>

<!-- 3 -->
<div class="scrim ov" id="s3scrim" style="height:690px"></div>
{ring(540, 230, 110, 28, "ov s3ring")}
<div class="abs num ov" id="s3num" style="left:470px;top:150px;width:140px;font-size:150px">3</div>
<div class="abs scr ov" id="s3t" style="left:0;width:1080px;text-align:center;top:360px;font-size:150px;padding:0"><span style="display:inline-block;padding:0 30px">Xina qo'ying</span></div>
<div class="abs ov" id="s3ic" style="left:880px;top:120px;width:150px;height:200px">{icon("cone")}</div>
<div class="scrim ov" id="ndscrim" style="height:690px"></div>
<div class="abs ov" id="nd" style="left:320px;top:90px;width:440px;height:560px">{NAIL_DIAGRAM}</div>
<div class="abs scr ov" id="ndl1" style="left:740px;top:160px;font-size:60px;padding:0 8px">o'sgan qism</div>
<div class="abs ov" id="ndeye" style="left:96px;top:150px;width:150px;height:150px">{icon("eye_off")}</div>
<div class="abs lab ov" id="ndl2" style="left:60px;top:310px;width:230px;text-align:center;font-size:34px">ko'rinmaydi</div>
<div class="abs scr ov" id="ndl3" style="left:770px;top:330px;font-size:70px;padding:0 8px">xina<br>bekitadi</div>

<div class="scrim ov" id="chscrim" style="height:560px"></div>
<div class="pill ov" id="ch1" style="left:120px;top:200px">{icon("shield")}<span class="lab" style="font-size:44px">mustahkam</span></div>
<div class="pill ov" id="ch2" style="left:600px;top:200px">{icon("arrow_up")}<span class="lab" style="font-size:44px">o'sish</span></div>
{vine("ov chv", 1074, 420, 0.8, flip=True)}

<!-- CTA -->
<div class="prof ov" id="prof"><img src="assets/avatar.jpg" alt=""><div class="h">@xina_siren</div><div class="d">Halol xina · manikyur · qosh</div>
<div class="btn" id="btn"><span class="b1">Obuna bo'lish</span><span class="b2">✓ Obunadasiz</span></div></div>
<div class="scrim ov" id="plscrim" style="height:600px"></div>
<svg class="layer ov" id="plpath" viewBox="0 0 1080 1920"><path d="M150 430 C 380 300 600 470 860 250" fill="none" stroke="{STAIN}" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 18"/></svg>
<div class="abs ov" id="pl" style="left:820px;top:170px;width:150px;height:150px">{icon("plane")}</div>
<div class="abs scr ov" id="pll" style="left:110px;top:120px;font-size:96px">do'stingizga yuboring</div>

{''.join(sweep_svg(i) for i in range(len(SWEEPS)))}

<!-- SUBTITRLAR -->
{chr(10).join(subs)}

<!-- YAKUN -->
<div class="layer ov" id="end" style="z-index:60">
  {vine("en1", 8, 560, 0.7)}
  {vine("en2", 1072, 560, 0.7, flip=True)}
  <div class="abs scr" id="ent" style="left:0;width:1080px;text-align:center;top:640px;font-size:170px;padding:0">Xina Siren</div>
  <div class="abs kick" id="enk" style="left:0;width:1080px;text-align:center;top:930px;font-size:30px">HALOL XINA · MANIKYUR · TOSHKENT</div>
  <div class="abs lab" id="enh" style="left:0;width:1080px;text-align:center;top:1010px;font-size:54px">@xina_siren</div>
  <div class="abs lab" id="enp" style="left:0;width:1080px;text-align:center;top:1090px;font-size:40px;font-weight:600;color:#6b5444">+998 33 712 26 07</div>
</div>
"""

    js = f"""
// ---------- HOOK ----------
tl.fromTo("#hscrim", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 0.1);
enter("#hk", 0.25, {{y:14, b:8, d:0.7}});
tl.set("#ht", {{opacity:1}}, 0.45);
tl.fromTo("#ht", {{clipPath:"inset(-20% 100% -20% 0%)", color:"{PASTE}"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:1.5, ease:"power1.inOut"}}, 0.45);
tl.to("#ht", {{color:"{STAIN}", duration:1.8, ease:"sine.inOut"}}, 1.4);
tl.fromTo("#htip", {{x:0, opacity:0}}, {{x:{hook_w - 30}, duration:1.5, ease:"power1.inOut"}}, 0.45);
tl.to("#htip", {{opacity:1, duration:0.3, ease:IO}}, 0.45);
tl.to("#htip", {{opacity:0, duration:0.5, ease:IO}}, 1.95);
tl.set(".hring", {{opacity:1}}, 1.2);
tl.fromTo(".hring circle", {{opacity:0, scale:0.4, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.45, ease:IN, stagger:0.03}}, 1.2);
enter("#hn", 1.55, {{y:18, b:10, s:0.9, d:0.8}});
enter("#hl", 1.8, {{y:10, b:6, d:0.6}});
tl.set(".hv", {{opacity:1}}, 0.6);
draw(".hv path", 0.6, 1.6, 0.18);
tl.fromTo(".hv circle", {{opacity:0, scale:0.4, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.45, ease:IN, stagger:0.1}}, 1.4);
exit([...document.querySelectorAll("#hscrim, #hk, #ht, .hring, #hn, #hl, .hv")], 5.45, 0.55);

// ---------- 1 ----------
{section_js(1, 6.3, 14.25, 92, "Halol manikyur", 92)}
tl.set("#s1nail", {{opacity:1}}, 10.6); draw("#s1nail path", 10.6, 1.0, 0.2);
tl.set("#s1chk", {{opacity:1}}, 11.7); draw("#s1chk path", 11.7, 0.6);
exit(["#s1nail", "#s1chk"].map(s=>document.querySelector(s)), 14.25, 0.55);

// ---------- sabab ----------
tl.fromTo("#cyscrim", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 15.0);
tl.set("#cy1", {{opacity:1}}, 15.1); draw("#cy1 path", 15.1, 0.9, 0.15);
enter("#cy1l", 15.5, {{y:12, b:6, d:0.6}});
tl.set("#cyar", {{opacity:1}}, 15.9);
draw("#cyar path:nth-child(1), #cyar path:nth-child(2)", 15.9, 0.5, 0.25);
tl.set("#cy2", {{opacity:1}}, 16.3); draw("#cy2 path", 16.3, 0.9, 0.15);
tl.set("#cy2l", {{opacity:1}}, 16.8);
tl.fromTo("#cy2l", {{clipPath:"inset(-20% 100% -20% 0%)", color:"{PASTE}"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:0.8, ease:"power1.inOut"}}, 16.8);
tl.to("#cy2l", {{color:"{STAIN}", duration:1.2, ease:"sine.inOut"}}, 17.3);
draw("#cyar path:nth-child(3), #cyar path:nth-child(4)", 17.7, 0.5, 0.25);
tl.set("#cy3", {{opacity:1}}, 18.1); draw("#cy3 path", 18.1, 0.8, 0.2);
enter("#cy3l", 18.6, {{y:12, b:6, d:0.6}});
draw("#cyar path:nth-child(5), #cyar path:nth-child(6)", 18.9, 0.8, 0.4);
exit([...document.querySelectorAll("#cyscrim, #cy1, #cy1l, #cy2, #cy2l, #cy3, #cy3l, #cyar")], 19.75, 0.5);

// ---------- 2 ----------
{section_js(2, 20.4, 24.4, 92, "Mustahkamlik", has_icon=True)}
tl.fromTo("#bwscrim", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 24.75);
tl.set("#bw", {{opacity:1}}, 24.8); draw("#bw path", 24.8, 0.9, 0.12);
enter("#bwl", 25.3, {{y:12, b:6, d:0.6}});
tl.set("#ck", {{opacity:1}}, 25.8); draw("#ck path, #ck circle", 25.8, 0.9, 0.1);
tl.fromTo("#ck path:nth-child(3)", {{rotation:0, svgOrigin:"60 62"}}, {{rotation:300, svgOrigin:"60 62", duration:2.6, ease:"sine.inOut"}}, 26.2);
enter("#ckn", 26.7, {{y:20, b:12, s:1.06, d:0.8}});
enter("#ckl", 27.0, {{y:12, b:6, d:0.6}});
exit([...document.querySelectorAll("#bw, #bwl, #ck, #ckn, #ckl")], 28.4, 0.5);
tl.to("#bwscrim", {{opacity:0, duration:0.5, ease:IO}}, 28.75);
tl.fromTo("#elscrim", {{opacity:0}}, {{opacity:1, duration:0.4, ease:IO}}, 28.5);
tl.set("#eltiles", {{opacity:1}}, 28.75);
draw("#eltiles rect", 28.75, 0.9, 1.4);
enter("#el1, #el1n", 29.75, {{y:14, b:8, d:0.7}}); enter("#el1l", 30.0, {{y:10, b:6, d:0.6}});
enter("#elp", 30.2, {{y:0, b:8, s:0.85, d:0.6}});
enter("#el2, #el2n", 30.45, {{y:14, b:8, d:0.7}}); enter("#el2l", 30.65, {{y:10, b:6, d:0.6}});
exit([...document.querySelectorAll("#elscrim, #eltiles, #el1, #el1n, #el1l, #elp, #el2, #el2n, #el2l")], 31.85, 0.55);

// ---------- 3 ----------
tl.fromTo("#s3scrim", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 32.5);
tl.set(".s3ring", {{opacity:1}}, 32.55);
tl.fromTo(".s3ring circle", {{opacity:0, scale:0.4, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.45, ease:IN, stagger:0.025}}, 32.55);
enter("#s3num", 32.8, {{y:18, b:10, s:0.9, d:0.8}});
tl.set("#s3t", {{opacity:1}}, 33.3);
tl.fromTo("#s3t span", {{clipPath:"inset(-20% 100% -20% 0%)", color:"{PASTE}"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:1.5, ease:"power1.inOut"}}, 33.3);
tl.to("#s3t span", {{color:"{STAIN}", duration:1.6, ease:"sine.inOut"}}, 34.1);
tl.set("#s3ic", {{opacity:1}}, 33.6); draw("#s3ic path", 33.6, 0.9, 0.12);
exit([...document.querySelectorAll(".s3ring, #s3num, #s3t, #s3ic")], 35.25, 0.5);
tl.to("#s3scrim", {{opacity:0, duration:0.5, ease:IO}}, 35.6);
tl.fromTo("#ndscrim", {{opacity:0}}, {{opacity:1, duration:0.5, ease:IO}}, 35.35);
tl.set("#nd", {{opacity:1}}, 35.7);
draw("#nd .nd-finger", 35.7, 1.1); draw("#nd .nd-nail", 36.2, 1.0);
tl.fromTo("#nd .nd-cut", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 36.9);
draw("#nd .nd-dim", 37.0, 0.6);
tl.set("#ndl1", {{opacity:1}}, 37.2);
tl.fromTo("#ndl1", {{clipPath:"inset(-20% 100% -20% 0%)"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:1.0, ease:"power1.inOut"}}, 37.2);
tl.set("#ndeye", {{opacity:1}}, 38.0); draw("#ndeye path, #ndeye circle", 38.0, 0.8, 0.15);
enter("#ndl2", 38.3, {{y:12, b:6, d:0.6}});
exit([...document.querySelectorAll("#ndeye, #ndl2")], 40.6, 0.5);
tl.fromTo("#nd .nd-fill", {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:1.3, ease:"power2.inOut"}}, 42.5);
tl.set("#ndl3", {{opacity:1}}, 42.8);
tl.fromTo("#ndl3", {{clipPath:"inset(-20% 100% -20% 0%)", color:"{PASTE}"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:0.8, ease:"power1.inOut"}}, 42.8);
tl.to("#ndl3", {{color:"{STAIN}", duration:0.8, ease:"sine.inOut"}}, 43.2);
exit([...document.querySelectorAll("#nd, #ndl1, #ndl3, #ndscrim")], 44.25, 0.5);
tl.fromTo("#chscrim", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 44.4);
enter("#ch1", 46.75, {{y:30, b:12, d:0.8}}); draw("#ch1 path", 46.95, 0.8, 0.15);
enter("#ch2", 48.35, {{y:30, b:12, d:0.8}}); draw("#ch2 path", 48.55, 0.7, 0.15);
tl.set(".chv", {{opacity:1}}, 45.0); draw(".chv path", 45.0, 2.0, 0.2);
tl.fromTo(".chv circle", {{opacity:0, scale:0.4, transformOrigin:"50% 50%"}}, {{opacity:1, scale:1, duration:0.45, ease:IN, stagger:0.12}}, 46.0);
exit([...document.querySelectorAll("#chscrim, #ch1, #ch2, .chv")], 49.2, 0.5);

// ---------- CTA ----------
enter("#prof", 50.2, {{y:60, b:12, d:0.9}});
tl.to("#btn", {{scale:0.92, duration:0.22, ease:IO}}, 53.8);
tl.to("#btn", {{scale:1, duration:0.4, ease:IN}}, 54.02);
tl.fromTo("#btn .b1", {{opacity:1}}, {{opacity:0, duration:0.35, ease:IO}}, 53.9);
tl.fromTo("#btn .b2", {{opacity:0, scale:1.2}}, {{opacity:1, scale:1, duration:0.45, ease:IN}}, 53.95);
tl.to("#btn", {{backgroundColor:"#8a6cd6", duration:0.4, ease:IO}}, 53.3);
exit("#prof", 55.05, 0.5);
tl.fromTo("#plscrim", {{opacity:0}}, {{opacity:1, duration:0.5, ease:IO}}, 55.2);
tl.set("#pll", {{opacity:1}}, 55.35);
tl.fromTo("#pll", {{clipPath:"inset(-20% 100% -20% 0%)", color:"{PASTE}"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:1.6, ease:"power1.inOut"}}, 55.35);
tl.to("#pll", {{color:"{STAIN}", duration:1.4, ease:"sine.inOut"}}, 56.2);
tl.set("#plpath", {{opacity:1}}, 56.6);
tl.fromTo("#plpath", {{clipPath:"inset(0% 100% 0% 0%)"}}, {{clipPath:"inset(0% 0% 0% 0%)", duration:1.2, ease:IO}}, 56.6);
tl.set("#pl", {{opacity:1}}, 57.2); draw("#pl path", 57.2, 0.8, 0.2);
tl.fromTo("#pl", {{x:-40, y:30}}, {{x:30, y:-20, duration:1.3, ease:"sine.inOut"}}, 57.2);
exit([...document.querySelectorAll("#plscrim, #pll, #plpath, #pl")], 58.5, 0.5);

// ---------- SWEEP o'tishlari ----------
{chr(10).join(f'tl.set("#sw{i} path", {{opacity:1}}, {t:.2f}); draw("#sw{i} path", {t:.2f}, 0.42); undraw("#sw{i} path", {t + 0.44:.2f}, 0.62);' for i, t in enumerate(SWEEPS))}

// ---------- SUBTITR ----------
{subs_js(extra=lambda c: f'tl.fromTo("#sb{c["i"]} .u", {{backgroundSize:"0% 6px"}}, {{backgroundSize:"100% 6px", duration:0.55, ease:IO}}, {c["acc_t"]:.2f});')}

// ---------- YAKUN ----------
tl.fromTo("#end", {{opacity:0}}, {{opacity:1, duration:0.6, ease:"sine.inOut"}}, 58.75);
draw("#end .vine path", 59.0, 0.95, 0.04);
tl.fromTo("#end .vine circle", {{opacity:0}}, {{opacity:1, duration:0.5, ease:IO, stagger:0.05}}, 59.4);
tl.fromTo("#ent", {{clipPath:"inset(-20% 100% -20% 0%)", color:"{PASTE}"}}, {{clipPath:"inset(-20% 0% -20% 0%)", duration:1.2, ease:"power1.inOut"}}, 59.0);
tl.to("#ent", {{color:"{STAIN}", duration:1.0, ease:"sine.inOut"}}, 59.6);
enter("#enk", 59.5, {{y:12, b:6, d:0.6}});
enter("#enh", 59.7, {{y:16, b:8, d:0.6}});
enter("#enp", 59.85, {{y:14, b:6, d:0.6}});
"""
    return dict(faces=FACES, css=CSS, body=body, js=js, bg="#f3e7da", sweeps=SWEEPS, sfx="sweep_small.wav", sfx_gain=0.35, sfx_lead=0.05)
