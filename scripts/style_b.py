"""B — Binafsha ipak: lyuks go'zallik jurnali; Bodoni + Jost, muzli shisha, marvarid, lavanda ipak o'tishlari."""
from common import chunks, split_acc, icon, NAIL_DIAGRAM, subs_js
from textw import tw

PLUM, SILK, AME, PEARL = "#1d0f2a", "#cdb6ff", "#7e5acb", "#efe8f7"
FACES = ["Bodoni", "BodoniI", "Jost"]

CSS = f"""
#cam {{ filter: saturate(.92) contrast(1.04); }}
#tint {{ position: absolute; inset: 0; background: rgba(80,40,120,.10); mix-blend-mode: multiply; }}
#vig {{ position: absolute; inset: 0; background: radial-gradient(120% 80% at 50% 45%, rgba(29,15,42,0) 55%, rgba(29,15,42,.45) 100%); }}
.ic {{ fill: none; stroke: {PEARL}; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }}
.band {{ position: absolute; left: 0; top: 0; width: 1080px; background: linear-gradient(180deg, rgba(29,15,42,.9) 0%, rgba(29,15,42,.8) 58%, rgba(29,15,42,.35) 82%, rgba(29,15,42,0) 100%); }}
.bod {{ font-family: "Bodoni"; font-weight: 600; font-optical-sizing: none; font-variation-settings: "opsz" 14; color: #fff; white-space: nowrap; line-height: 1.12; }}
.it {{ font-family: "BodoniI"; font-style: italic; font-weight: 600; font-optical-sizing: none; font-variation-settings: "opsz" 14; color: {SILK}; white-space: nowrap; line-height: 1.12; }}
.jo {{ font-family: "Jost"; font-weight: 400; color: {PEARL}; white-space: nowrap; letter-spacing: .32em; text-transform: uppercase; }}
.rule {{ position: absolute; height: 2px; background: linear-gradient(90deg, rgba(239,232,247,0), {PEARL} 18%, {PEARL} 82%, rgba(239,232,247,0)); transform-origin: 0 50%; }}
.glass {{ position: absolute; border-radius: 36px; background: rgba(255,255,255,.13); border: 1.5px solid rgba(255,255,255,.36);
  -webkit-backdrop-filter: blur(22px) saturate(1.2); backdrop-filter: blur(22px) saturate(1.2); box-shadow: 0 24px 60px rgba(20,8,32,.32); }}
.pearl {{ width: 22px; height: 22px; border-radius: 50%; background: radial-gradient(circle at 35% 30%, #fff, #e7dcf5 45%, #a998c4 100%); box-shadow: 0 2px 6px rgba(0,0,0,.3); display: inline-block; }}
.sub .t {{ display: inline-block; font-family: "Jost"; font-weight: 500; font-size: 46px; line-height: 1.25; color: #fff; letter-spacing: .01em;
  padding: 10px 30px 12px; border-radius: 30px; background: rgba(29,15,42,.76); border: 1.5px solid rgba(255,255,255,.22);
  -webkit-backdrop-filter: blur(14px); backdrop-filter: blur(14px); }}
.sub .a {{ font-family: "BodoniI"; font-style: italic; font-weight: 700; font-optical-sizing: none; font-variation-settings: "opsz" 11; font-size: 60px; color: {SILK}; }}
.silk {{ position: absolute; left: -1360px; top: -940px; width: 3800px; height: 3800px; z-index: 50; pointer-events: none;
  background:
   repeating-linear-gradient(115deg, rgba(255,255,255,0) 0 90px, rgba(255,255,255,.07) 120px, rgba(80,40,140,.08) 170px, rgba(255,255,255,0) 210px),
   linear-gradient(115deg, rgba(205,182,255,0) 0%, rgba(205,182,255,0) 17%, #e9ddff 24%, #a585e6 34%, #d7c4fb 44%, #7e5acb 54%, #cdb6ff 64%, #efe6ff 76%, rgba(239,230,255,0) 83%, rgba(239,230,255,0) 100%); }}
.sheen {{ position: absolute; left: -1360px; top: -940px; width: 3800px; height: 3800px; z-index: 51; pointer-events: none; mix-blend-mode: screen;
  background: linear-gradient(115deg, transparent 40%, rgba(255,255,255,.55) 48%, transparent 56%); }}
.nd .nd-ln {{ fill: none; stroke: {PEARL}; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }}
.nd .nd-fill {{ fill: #3b1830; }}
.nd .nd-cut {{ stroke: {SILK}; }}
.prof {{ position: absolute; left: 100px; top: 200px; width: 880px; height: 270px; }}
.prof img {{ position: absolute; left: 40px; top: 50px; width: 170px; height: 170px; border-radius: 50%; object-fit: cover; outline: 3px solid {SILK}; outline-offset: 6px; }}
.prof .h {{ position: absolute; left: 250px; top: 46px; font-family: "BodoniI"; font-style: italic; font-weight: 600; font-optical-sizing: none; font-variation-settings: "opsz" 14; font-size: 64px; color: #fff; }}
.prof .d {{ position: absolute; left: 254px; top: 128px; font-family: "Jost"; font-size: 26px; letter-spacing: .26em; color: {PEARL}; text-transform: uppercase; }}
.btn {{ position: absolute; left: 252px; top: 182px; width: 320px; height: 62px; border-radius: 40px; background: {PEARL}; color: {PLUM}; font-family: "Jost"; font-weight: 500; font-size: 26px; letter-spacing: .14em; display: grid; place-items: center; text-transform: uppercase; }}
.btn span {{ grid-area: 1/1; }}
.btn .b2 {{ opacity: 0; }}
#end {{ background: radial-gradient(90% 60% at 50% 40%, #3a1f55 0%, {PLUM} 70%); }}
"""

SILKS = [6.13, 20.2, 32.47, 49.8]


def band(i, h):
    return f'<div class="band ov" id="{i}" style="height:{h}px"></div>'


def section(k, label, icon_name=None):
    return f"""
{band(f"s{k}band", 380)}
<div class="abs it ov" id="s{k}num" style="left:70px;top:22px;font-size:200px;line-height:1">{k}</div>
<div class="abs jo ov" id="s{k}lab" style="left:220px;top:120px;font-size:34px">{label}</div>
<div class="rule ov" id="s{k}rule" style="left:220px;top:180px;width:{tw("Jost", 34, label) + 34 * 0.32 * len(label)}px"></div>
""" + (f'<div class="abs ov" id="s{k}ic" style="left:880px;top:70px;width:130px;height:130px">{icon(icon_name)}</div>' if icon_name else "")


def section_js(k, t0, t1, has_icon=False):
    js = f"""
tl.fromTo("#s{k}band", {{opacity:0}}, {{opacity:1, duration:0.7, ease:IO}}, {t0:.2f});
enter("#s{k}num", {t0 + 0.15:.2f}, {{y:30, b:22, s:1.08, d:1.0}});
enter("#s{k}lab", {t0 + 0.45:.2f}, {{y:14, b:8, d:0.7}});
tl.fromTo("#s{k}rule", {{scaleX:0, opacity:1}}, {{scaleX:1, duration:0.9, ease:IO}}, {t0 + 0.6:.2f});
"""
    sel = f"#s{k}band, #s{k}num, #s{k}lab, #s{k}rule"
    if has_icon:
        js += f'tl.set("#s{k}ic", {{opacity:1}}, {t0 + 0.9:.2f}); draw("#s{k}ic path", {t0 + 0.9:.2f}, 0.9, 0.12);\n'
        sel += f", #s{k}ic"
    js += f'exit([...document.querySelectorAll("{sel}")], {t1:.2f}, 0.55);\n'
    return js


def build():
    subs = []
    for c in chunks():
        a, acc, b = split_acc(c["text"], c["acc"])
        mid = f'<span class="a">{acc}</span>' if acc else ""
        subs.append(f'<div class="sub ov" id="sb{c["i"]}" style="top:{c["y"] - 40}px"><span class="t">{a}{mid}{b}</span></div>')

    body = f"""
<div id="tint" class="layer"></div>
<div id="vig" class="layer"></div>

<!-- HOOK -->
{band("hband", 430)}
<div class="abs jo ov" id="hm" style="left:72px;top:58px;font-size:26px">XINA SIREN · MASLAHAT</div>
<div class="rule ov" id="hr" style="left:72px;top:102px;width:430px"></div>
<div class="abs bod ov" id="h1" style="left:66px;top:118px;font-size:98px">Tirnoq tishlash</div>
<div class="abs it ov" id="h2" style="left:66px;top:226px;font-size:98px">odatini tashlash</div>
<div class="glass ov" id="h3" style="left:740px;top:44px;width:270px;height:64px;border-radius:40px;display:flex;align-items:center;justify-content:center;gap:14px">
  <span class="pearl"></span><span class="jo" style="font-size:24px;letter-spacing:.28em">3 LAYFXAK</span></div>

<!-- 1 -->
{section(1, "Halol manikyur")}
<div class="glass ov" id="s1g" style="left:820px;top:60px;width:190px;height:190px"></div>
<div class="abs ov" id="s1nail" style="left:850px;top:80px;width:130px;height:130px">{icon("nail")}</div>
<div class="abs ov" id="s1chk" style="left:930px;top:160px;width:70px;height:70px">{icon("check")}</div>

<!-- sabab -->
{band("cyband", 340)}
<div class="glass ov cyg" id="cyg1" style="left:60px;top:36px;width:270px;height:230px"></div>
<div class="glass ov cyg" id="cyg2" style="left:405px;top:36px;width:270px;height:230px"></div>
<div class="glass ov cyg" id="cyg3" style="left:750px;top:36px;width:270px;height:230px"></div>
<div class="abs ov" id="cy1" style="left:135px;top:52px;width:120px;height:120px">{icon("nail_bitten")}</div>
<div class="abs ov" id="cy2" style="left:480px;top:52px;width:120px;height:120px">{icon("nail_crack")}</div>
<div class="abs ov" id="cy3" style="left:825px;top:52px;width:120px;height:120px">{icon("loop")}</div>
<div class="abs jo ov" id="cy1l" style="left:60px;width:270px;text-align:center;top:196px;font-size:24px;letter-spacing:.2em">tishlash</div>
<div class="abs it ov" id="cy2l" style="left:405px;width:270px;text-align:center;top:180px;font-size:58px">mo'rt</div>
<div class="abs jo ov" id="cy3l" style="left:750px;width:270px;text-align:center;top:196px;font-size:22px;letter-spacing:.14em">yana tishlanadi</div>
<svg class="layer ov" id="cyar" viewBox="0 0 1080 1920"><g fill="none" stroke="{SILK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
<path d="M342 150 H392"/><path d="M380 138 L394 150 L380 162"/><path d="M687 150 H737"/><path d="M725 138 L739 150 L725 162"/></g></svg>

<!-- 2 -->
{section(2, "Mustahkamlik", "shield")}
{band("bwband", 340)}
<div class="glass ov" id="bwg" style="left:60px;top:36px;width:960px;height:250px"></div>
<div class="abs ov" id="bw" style="left:110px;top:60px;width:150px;height:150px">{icon("bowl")}</div>
<div class="abs jo ov" id="bwl" style="left:70px;width:230px;text-align:center;top:216px;font-size:24px;letter-spacing:.2em">tuzli suv</div>
<div class="abs ov" id="ck" style="left:350px;top:70px;width:130px;height:130px">{icon("clock")}</div>
<div class="abs it ov" id="ckn" style="left:510px;top:58px;font-size:132px;line-height:1">10–15</div>
<div class="abs jo ov" id="ckl" style="left:516px;top:212px;font-size:24px">minut · bir kunda</div>
{band("elband", 340)}
<div class="glass ov" id="elg1" style="left:230px;top:36px;width:230px;height:230px"></div>
<div class="glass ov" id="elg2" style="left:620px;top:36px;width:230px;height:230px"></div>
<div class="abs jo ov" id="el1n" style="left:254px;top:56px;font-size:24px;letter-spacing:.1em">20</div>
<div class="abs bod ov" id="el1" style="left:230px;width:230px;text-align:center;top:80px;font-size:110px">Ca</div>
<div class="abs jo ov" id="el1l" style="left:230px;width:230px;text-align:center;top:212px;font-size:22px">kalsiy</div>
<div class="abs jo ov" id="el2n" style="left:644px;top:56px;font-size:24px;letter-spacing:.1em">30</div>
<div class="abs bod ov" id="el2" style="left:620px;width:230px;text-align:center;top:80px;font-size:110px">Zn</div>
<div class="abs jo ov" id="el2l" style="left:620px;width:230px;text-align:center;top:212px;font-size:22px">sink</div>
<div class="abs it ov" id="elp" style="left:470px;width:140px;text-align:center;top:90px;font-size:110px">+</div>

<!-- 3 -->
{band("s3band", 700)}
<div class="abs it ov" id="s3num" style="left:0;width:1080px;text-align:center;top:40px;font-size:330px;line-height:1">3</div>
<div class="abs jo ov" id="s3lab" style="left:0;width:1080px;text-align:center;top:420px;font-size:40px">Xina qo'ying</div>
<div class="rule ov" id="s3rule" style="left:330px;top:490px;width:420px"></div>
<div class="abs ov" id="s3ic" style="left:845px;top:110px;width:150px;height:200px">{icon("cone")}</div>
{band("ndband", 700)}
<div class="abs ov" id="nd" style="left:320px;top:90px;width:440px;height:560px">{NAIL_DIAGRAM}</div>
<div class="abs it ov" id="ndl1" style="left:740px;top:150px;font-size:50px">o'sgan qism</div>
<div class="abs ov" id="ndeye" style="left:96px;top:150px;width:150px;height:150px">{icon("eye_off")}</div>
<div class="abs jo ov" id="ndl2" style="left:50px;width:250px;text-align:center;top:316px;font-size:24px;letter-spacing:.2em">ko'rinmaydi</div>
<div class="abs it ov" id="ndl3" style="left:770px;top:330px;font-size:58px;line-height:1.1">xina<br>bekitadi</div>
{band("chband", 560)}
<div class="glass ov" id="ch1" style="left:100px;top:210px;width:400px;height:120px;border-radius:60px;display:flex;align-items:center;gap:22px;padding-left:36px">
  <span style="width:70px;height:70px;display:block">{icon("shield")}</span><span class="it" style="font-size:52px;color:#fff">mustahkam</span></div>
<div class="glass ov" id="ch2" style="left:580px;top:210px;width:400px;height:120px;border-radius:60px;display:flex;align-items:center;gap:22px;padding-left:36px">
  <span style="width:70px;height:70px;display:block">{icon("arrow_up")}</span><span class="it" style="font-size:52px;color:#fff">o'sish</span></div>

<!-- CTA -->
<div class="glass prof ov" id="prof"><img src="assets/avatar.jpg" alt=""><div class="h">@xina_siren</div><div class="d">Halol xina · manikyur</div>
<div class="btn" id="btn"><span class="b1">Obuna bo'lish</span><span class="b2">✓ Obunadasiz</span></div></div>
{band("plband", 600)}
<div class="abs it ov" id="pll" style="left:0;width:1080px;text-align:center;top:300px;font-size:92px">do'stingizga yuboring</div>
<div class="abs ov" id="pl" style="left:470px;top:100px;width:150px;height:150px">{icon("plane")}</div>

<!-- SUBTITRLAR -->
{chr(10).join(subs)}

<!-- IPAK O'TISHLARI -->
{''.join(f'<div class="silk" id="sk{i}"></div><div class="sheen" id="sh{i}"></div>' for i in range(len(SILKS)))}

<!-- YAKUN -->
<div class="layer ov" id="end" style="z-index:60">
  <div class="abs jo" id="enm" style="left:0;width:1080px;text-align:center;top:600px;font-size:26px">HALOL XINA STUDIYASI · TOSHKENT</div>
  <div class="abs bod" id="ent" style="left:0;width:1080px;text-align:center;top:660px;font-size:140px;letter-spacing:.06em">XINA SIREN</div>
  <div class="rule" id="enr" style="left:300px;top:850px;width:480px"></div>
  <div class="abs it" id="enh" style="left:0;width:1080px;text-align:center;top:890px;font-size:72px">@xina_siren</div>
  <div class="abs jo" id="enp" style="left:0;width:1080px;text-align:center;top:1010px;font-size:32px;letter-spacing:.2em">+998 33 712 26 07</div>
</div>
"""

    D = 2600
    silk_js = "\n".join(
        f'tl.fromTo("#sk{i}", {{x:{-D * .906:.0f}, y:{-D * .423:.0f}}}, {{x:{D * .906:.0f}, y:{D * .423:.0f}, duration:1.5, ease:"power2.inOut"}}, {t - 0.75:.2f});\n'
        f'tl.fromTo("#sh{i}", {{x:{-D * 1.2 * .906:.0f}, y:{-D * 1.2 * .423:.0f}}}, {{x:{D * 1.2 * .906:.0f}, y:{D * 1.2 * .423:.0f}, duration:1.5, ease:"power2.inOut"}}, {t - 0.75:.2f});'
        for i, t in enumerate(SILKS))

    js = f"""
// ---------- HOOK ----------
tl.fromTo("#hband", {{opacity:0}}, {{opacity:1, duration:0.8, ease:IO}}, 0.05);
enter("#hm", 0.25, {{y:12, b:8, d:0.7}});
tl.fromTo("#hr", {{scaleX:0, opacity:1}}, {{scaleX:1, duration:0.9, ease:IO}}, 0.45);
enter("#h1", 0.55, {{y:30, b:18, d:0.9}});
enter("#h2", 0.9, {{y:30, b:18, d:0.9}});
enter("#h3", 1.6, {{y:14, b:10, s:0.94, d:0.75}});
exit([...document.querySelectorAll("#hband, #hm, #hr, #h1, #h2, #h3")], 5.3, 0.55);

// ---------- 1 ----------
{section_js(1, 6.45, 14.2)}
enter("#s1g", 10.4, {{y:20, b:12, d:0.8}});
tl.set("#s1nail", {{opacity:1}}, 10.6); draw("#s1nail path", 10.6, 1.0, 0.2);
tl.set("#s1chk", {{opacity:1}}, 11.7); draw("#s1chk path", 11.7, 0.6);
exit([...document.querySelectorAll("#s1g, #s1nail, #s1chk")], 14.2, 0.55);

// ---------- sabab ----------
tl.fromTo("#cyband", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 14.95);
enter("#cyg1", 15.05, {{y:24, b:12, d:0.8}});
tl.set("#cy1", {{opacity:1}}, 15.2); draw("#cy1 path", 15.2, 0.8, 0.15);
enter("#cy1l", 15.5, {{y:10, b:6, d:0.6}});
tl.set("#cyar", {{opacity:1}}, 15.9); draw("#cyar path:nth-child(1), #cyar path:nth-child(2)", 15.9, 0.45, 0.2);
enter("#cyg2", 16.2, {{y:24, b:12, d:0.8}});
tl.set("#cy2", {{opacity:1}}, 16.35); draw("#cy2 path", 16.35, 0.8, 0.15);
enter("#cy2l", 16.8, {{y:16, b:12, s:1.06, d:0.75}});
draw("#cyar path:nth-child(3), #cyar path:nth-child(4)", 17.7, 0.45, 0.2);
enter("#cyg3", 18.0, {{y:24, b:12, d:0.8}});
tl.set("#cy3", {{opacity:1}}, 18.15); draw("#cy3 path", 18.15, 0.8, 0.2);
enter("#cy3l", 18.6, {{y:10, b:6, d:0.6}});
exit([...document.querySelectorAll("#cyband, .cyg, #cy1, #cy2, #cy3, #cy1l, #cy2l, #cy3l, #cyar")], 19.4, 0.5);

// ---------- 2 ----------
{section_js(2, 20.55, 24.4, True)}
tl.fromTo("#bwband", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 24.7);
enter("#bwg", 24.75, {{y:30, b:14, d:0.85}});
tl.set("#bw", {{opacity:1}}, 24.95); draw("#bw path", 24.95, 0.9, 0.12);
enter("#bwl", 25.4, {{y:10, b:6, d:0.6}});
tl.set("#ck", {{opacity:1}}, 25.9); draw("#ck path, #ck circle", 25.9, 0.9, 0.1);
tl.fromTo("#ck path:nth-child(3)", {{rotation:0, svgOrigin:"60 62"}}, {{rotation:300, svgOrigin:"60 62", duration:2.4, ease:"sine.inOut"}}, 26.3);
enter("#ckn", 26.7, {{y:20, b:16, s:1.06, d:0.85}});
enter("#ckl", 27.0, {{y:10, b:6, d:0.6}});
exit([...document.querySelectorAll("#bwg, #bw, #bwl, #ck, #ckn, #ckl")], 28.4, 0.5);
tl.to("#bwband", {{opacity:0, duration:0.5, ease:IO}}, 28.75);
tl.fromTo("#elband", {{opacity:0}}, {{opacity:1, duration:0.4, ease:IO}}, 28.5);
enter("#elg1", 28.8, {{y:24, b:12, d:0.8}});
enter("#el1, #el1n", 29.75, {{y:14, b:10, d:0.75}}); enter("#el1l", 30.0, {{y:10, b:6, d:0.6}});
enter("#elp", 30.2, {{y:0, b:10, s:0.86, d:0.65}});
enter("#elg2", 30.35, {{y:24, b:12, d:0.8}});
enter("#el2, #el2n", 30.5, {{y:14, b:10, d:0.75}}); enter("#el2l", 30.75, {{y:10, b:6, d:0.6}});
exit([...document.querySelectorAll("#elband, #elg1, #elg2, #el1, #el1n, #el1l, #elp, #el2, #el2n, #el2l")], 31.6, 0.5);

// ---------- 3 ----------
tl.fromTo("#s3band", {{opacity:0}}, {{opacity:1, duration:0.7, ease:IO}}, 32.75);
enter("#s3num", 32.9, {{y:40, b:26, s:1.1, d:1.1}});
enter("#s3lab", 33.4, {{y:14, b:8, d:0.75}});
tl.fromTo("#s3rule", {{scaleX:0, opacity:1}}, {{scaleX:1, duration:0.9, ease:IO}}, 33.6);
tl.set("#s3ic", {{opacity:1}}, 33.8); draw("#s3ic path", 33.8, 0.9, 0.12);
exit([...document.querySelectorAll("#s3num, #s3lab, #s3rule, #s3ic")], 35.25, 0.5);
tl.to("#s3band", {{opacity:0, duration:0.5, ease:IO}}, 35.7);
tl.fromTo("#ndband", {{opacity:0}}, {{opacity:1, duration:0.5, ease:IO}}, 35.35);
tl.set("#nd", {{opacity:1}}, 35.7);
draw("#nd .nd-finger", 35.7, 1.1); draw("#nd .nd-nail", 36.2, 1.0);
tl.fromTo("#nd .nd-cut", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 36.9);
draw("#nd .nd-dim", 37.0, 0.6);
enter("#ndl1", 37.2, {{y:14, b:10, d:0.75}});
tl.set("#ndeye", {{opacity:1}}, 38.0); draw("#ndeye path, #ndeye circle", 38.0, 0.8, 0.15);
enter("#ndl2", 38.3, {{y:10, b:6, d:0.6}});
exit([...document.querySelectorAll("#ndeye, #ndl2")], 40.6, 0.5);
tl.fromTo("#nd .nd-fill", {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:1.3, ease:"power2.inOut"}}, 42.5);
enter("#ndl3", 42.8, {{y:16, b:12, d:0.8}});
exit([...document.querySelectorAll("#nd, #ndl1, #ndl3, #ndband")], 44.25, 0.5);
tl.fromTo("#chband", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 44.4);
enter("#ch1", 46.75, {{y:30, b:14, d:0.85}}); draw("#ch1 path", 46.95, 0.8, 0.15);
enter("#ch2", 48.35, {{y:30, b:14, d:0.85}}); draw("#ch2 path", 48.55, 0.7, 0.15);
exit([...document.querySelectorAll("#chband, #ch1, #ch2")], 49.25, 0.5);

// ---------- CTA ----------
enter("#prof", 50.5, {{y:60, b:14, d:0.9}});
tl.to("#btn", {{scale:0.92, duration:0.22, ease:IO}}, 53.8);
tl.to("#btn", {{scale:1, duration:0.4, ease:IN}}, 54.02);
tl.fromTo("#btn .b1", {{opacity:1}}, {{opacity:0, duration:0.35, ease:IO}}, 53.9);
tl.fromTo("#btn .b2", {{opacity:0, scale:1.2}}, {{opacity:1, scale:1, duration:0.45, ease:IN}}, 53.95);
tl.to("#btn", {{backgroundColor:"{SILK}", duration:0.4, ease:IO}}, 53.3);
exit("#prof", 55.05, 0.5);
tl.fromTo("#plband", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 55.2);
tl.set("#pl", {{opacity:1}}, 55.4); draw("#pl path", 55.4, 0.8, 0.2);
tl.fromTo("#pl", {{x:-60, y:30}}, {{x:40, y:-20, duration:3.0, ease:"sine.inOut"}}, 55.4);
enter("#pll", 55.8, {{y:24, b:16, d:0.9}});
exit([...document.querySelectorAll("#plband, #pll, #pl")], 58.45, 0.5);

// ---------- IPAK ----------
{silk_js}

// ---------- SUBTITR ----------
{subs_js()}

// ---------- YAKUN ----------
tl.fromTo("#end", {{opacity:0}}, {{opacity:1, duration:0.6, ease:"sine.inOut"}}, 58.75);
enter("#enm", 59.05, {{y:12, b:8, d:0.7}});
enter("#ent", 59.2, {{y:30, b:20, s:1.04, d:1.0}});
tl.fromTo("#enr", {{scaleX:0, opacity:1}}, {{scaleX:1, duration:0.9, ease:IO}}, 59.5);
enter("#enh", 59.6, {{y:18, b:12, d:0.8}});
enter("#enp", 59.8, {{y:12, b:8, d:0.7}});
"""
    return dict(faces=FACES, css=CSS, body=body, js=js, bg=PLUM, sweeps=SILKS, sfx="air_woosh.wav", sfx_gain=0.42, sfx_lead=1.0)
