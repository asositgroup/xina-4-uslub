"""C — Original pasport: himoyalangan hujjat tili (gilosh, seriya, mikromatn, golografik muhr, UV-skaner)."""
from common import chunks, split_acc, icon, NAIL_DIAGRAM, subs_js, DUR

PAPER, INK, GL, RED = "#f6f3fb", "#231638", "#8c6fd0", "#c23b3b"
FACES = ["PlayfairSC", "PlayfairI", "JBMono", "Archivo"]
MICRO = "XINA SIREN • HALOL • ORIGINAL • " * 8

CSS = f"""
#cam {{ filter: contrast(1.05) brightness(1.02); }}
.ic {{ fill: none; stroke: {INK}; stroke-width: 5.5; stroke-linecap: round; stroke-linejoin: round; }}
.doc {{ position: absolute; left: 0; top: 0; width: 1080px; overflow: hidden; background-color: rgba(246,243,251,.95);
  background-image: url("assets/guil.png"); background-size: 1080px 700px; background-position: 0 50%; box-shadow: 0 16px 40px rgba(35,22,56,.22); }}
.doc .micro {{ position: absolute; left: 0; bottom: 10px; width: 2400px; height: 20px; background: url("assets/micro.png") repeat-x 0 0 / auto 20px; }}
.doc .edge {{ position: absolute; left: 0; bottom: 0; width: 1080px; height: 3px; background: repeating-linear-gradient(90deg, {GL} 0 14px, transparent 14px 22px); }}
.sc {{ font-family: "PlayfairSC"; font-weight: 700; color: #2a1d44; letter-spacing: .3em; white-space: nowrap; }}
.pi {{ font-family: "PlayfairI"; font-style: italic; font-weight: 700; color: {INK}; white-space: nowrap; line-height: 1.08; }}
.mo {{ font-family: "JBMono"; font-weight: 500; color: #45366a; white-space: nowrap; letter-spacing: .06em; }}
.mo b {{ color: {INK}; font-weight: 600; }}
.tag {{ position: absolute; font-family: "JBMono"; font-weight: 600; font-size: 22px; letter-spacing: .12em; color: {RED}; border: 3px solid {RED}; border-radius: 8px; padding: 6px 12px; white-space: nowrap; }}
.seal {{ position: absolute; width: 240px; height: 240px; }}
.seal .holo {{ position: absolute; inset: 0; border-radius: 50%; background: conic-gradient(#ffd1f3, #c9b6ff, #9fe8ff, #c8ffd8, #fff0b3, #ffd1f3);
  -webkit-mask: radial-gradient(circle, transparent 0 82px, #000 83px); mask: radial-gradient(circle, transparent 0 82px, #000 83px); box-shadow: 0 10px 26px rgba(35,22,56,.35); }}
.seal .core {{ position: absolute; inset: 79px; border-radius: 50%; background: {INK}; display: grid; place-items: center; }}
.seal .core span {{ font-family: "PlayfairSC"; font-weight: 700; font-size: 22px; letter-spacing: .14em; color: #e9ddff; }}
.seal svg {{ position: absolute; inset: 0; width: 240px; height: 240px; }}
.tile {{ position: absolute; width: 230px; height: 250px; border: 4px solid {INK}; border-radius: 14px; background: rgba(246,243,251,.97); }}
.tile .n {{ position: absolute; left: 16px; top: 10px; font-family: "JBMono"; font-size: 24px; color: {INK}; }}
.tile .m {{ position: absolute; right: 16px; top: 12px; font-family: "JBMono"; font-size: 18px; color: #45366a; }}
.tile .s {{ position: absolute; left: 0; width: 100%; top: 52px; text-align: center; font-family: "PlayfairSC"; font-weight: 700; font-size: 100px; color: {INK}; letter-spacing: 0; }}
.tile .l {{ position: absolute; left: 0; width: 100%; top: 196px; text-align: center; font-family: "JBMono"; font-size: 22px; letter-spacing: .14em; color: #45366a; }}
.sub .t {{ display: inline-block; font-family: "Archivo"; font-weight: 600; font-size: 44px; line-height: 1.25; color: {INK};
  background: rgba(246,243,251,.96); padding: 10px 26px 12px; border-radius: 8px; box-shadow: 0 10px 28px rgba(0,0,0,.22); }}
.sub .m {{ background-image: linear-gradient(rgba(140,111,208,.45), rgba(140,111,208,.45)); background-repeat: no-repeat; background-size: 0% 100%; padding: 0 6px; border-radius: 4px; }}
.uvbar {{ position: absolute; left: 0; top: 0; width: 1080px; height: 260px; z-index: 50; mix-blend-mode: screen;
  background: linear-gradient(180deg, rgba(120,60,255,0) 0%, rgba(140,90,255,.5) 70%, rgba(235,222,255,.95) 93%, rgba(140,90,255,0) 100%); }}
.uvtint {{ position: absolute; inset: 0; z-index: 49; background: rgba(84,40,210,.38); mix-blend-mode: multiply; }}
.nd .nd-ln {{ fill: none; stroke: {INK}; stroke-width: 5; stroke-linecap: round; stroke-linejoin: round; }}
.nd .nd-fill {{ fill: #3a1d10; }}
.idc {{ position: absolute; left: 90px; top: 190px; width: 900px; height: 300px; border-radius: 22px; overflow: hidden; background-color: rgba(246,243,251,.97);
  background-image: url("assets/guil.png"); background-size: 1080px 700px; background-position: -60px -180px; box-shadow: 0 22px 50px rgba(35,22,56,.28); }}
.idc img {{ position: absolute; left: 36px; top: 58px; width: 180px; height: 180px; border-radius: 16px; object-fit: cover; border: 3px solid {INK}; }}
.btn {{ position: absolute; left: 250px; top: 200px; width: 330px; height: 62px; border-radius: 10px; background: {INK}; color: #fff; font-family: "JBMono"; font-weight: 600; font-size: 24px; letter-spacing: .12em; display: grid; place-items: center; }}
.btn span {{ grid-area: 1/1; }}
.btn .b2 {{ opacity: 0; }}
#end {{ background-color: {PAPER}; background-image: url("assets/guil.png"); background-size: 1080px 700px; background-repeat: no-repeat; background-position: 0 560px; }}
.frame {{ position: absolute; left: 40px; top: 40px; width: 1000px; height: 1840px; border: 3px solid {INK}; border-radius: 10px; }}
.frame::after {{ content: ""; position: absolute; inset: 12px; border: 1.5px solid {GL}; border-radius: 6px; }}
"""

UV = [6.13, 20.2, 32.47, 49.8]


def seal(id_, x, y, word="HALOL"):
    return f"""<div class="seal ov" id="{id_}" style="left:{x}px;top:{y}px">
<div class="holo"></div><div class="core"><span>{word}</span></div>
<svg viewBox="0 0 240 240"><defs><path id="{id_}p" d="M120 120 m-101 0 a101 101 0 1 1 202 0 a101 101 0 1 1 -202 0"/></defs>
<g class="ring"><text font-family="JBMono" font-size="17" font-weight="600" letter-spacing="2.6" fill="{INK}"><textPath href="#{id_}p">ORIGINAL • XINA SIREN • HALOL • TOSHKENT •</textPath></text></g></svg></div>"""


def doc(id_, h, inner):
    return f'<div class="doc ov" id="{id_}" style="height:{h}px">{inner}<div class="micro"></div><div class="edge"></div></div>'


def doc_js(id_, t0, t1, h, kids=()):
    js = f'tl.fromTo("#{id_}", {{y:{-h - 20}, opacity:1, filter:"blur(10px)"}}, {{y:0, filter:"blur(0px)", duration:0.9, ease:IN}}, {t0:.2f});\n'
    js += f'tl.fromTo("#{id_} .micro", {{x:0}}, {{x:-260, duration:{t1 - t0 + 0.5:.2f}, ease:"none"}}, {t0:.2f});\n'
    for k, (sel, dt, o) in enumerate(kids):
        js += f'enter("{sel}", {t0 + dt:.2f}, {o});\n'
    js += f'tl.to("#{id_}", {{y:-50, opacity:0, filter:"blur(10px)", duration:0.55, ease:IO}}, {t1:.2f});\n'
    return js


def seal_js(id_, t0, t1):
    return (f'tl.fromTo("#{id_}", {{opacity:0, scale:1.14, filter:"blur(10px)"}}, {{opacity:1, scale:1, filter:"blur(0px)", duration:0.6, ease:"power3.out"}}, {t0:.2f});\n'
            f'tl.fromTo("#{id_} .holo", {{rotation:0}}, {{rotation:{(t1 - t0) * 40:.0f}, duration:{t1 - t0 + 0.5:.2f}, ease:"none"}}, {t0:.2f});\n'
            f'tl.fromTo("#{id_} .ring", {{rotation:0, svgOrigin:"120 120"}}, {{rotation:-{(t1 - t0) * 15:.0f}, svgOrigin:"120 120", duration:{t1 - t0 + 0.5:.2f}, ease:"none"}}, {t0:.2f});\n'
            f'exit("#{id_}", {t1:.2f}, 0.5);\n')


def build():
    subs = []
    for c in chunks():
        a, acc, b = split_acc(c["text"], c["acc"])
        mid = f'<span class="m">{acc}</span>' if acc else ""
        subs.append(f'<div class="sub ov" id="sb{c["i"]}" style="top:{c["y"] - 36}px"><span class="t">{a}{mid}{b}</span></div>')

    body = f"""
<!-- HOOK -->
{doc("hd", 400, '''
<div class="abs sc" id="hk" style="left:64px;top:58px;font-size:28px">TAVSIYANOMA</div>
<div class="abs mo" id="hn" style="left:392px;top:62px;font-size:24px"><b>№ XS-0001</b> · 3 USUL</div>
<div class="abs pi" id="h1" style="left:58px;top:106px;font-size:90px">Tirnoq tishlash</div>
<div class="abs pi" id="h2" style="left:58px;top:210px;font-size:90px">odatini tashlash</div>''')}
{seal("hs", 826, 118)}

<!-- 1 -->
{doc("d1", 360, f'''
<div class="abs mo" id="d1a" style="left:64px;top:58px;font-size:30px"><b>§ 1</b> · USUL</div>
<div class="abs pi" id="d1t" style="left:58px;top:100px;font-size:104px">Halol manikyur</div>
<div class="abs mo" id="d1b" style="left:64px;top:240px;font-size:24px">toza · kap-katta · tishlashga ko'z qiymaydi</div>
<div class="abs" id="d1c" style="left:860px;top:70px;width:150px;height:150px">{icon("nail")}</div>
<div class="abs" id="d1k" style="left:930px;top:150px;width:80px;height:80px">{icon("check")}</div>''')}

<!-- sabab -->
{doc("cy", 330, f'''
<div class="abs" id="cy1" style="left:110px;top:34px;width:130px;height:130px">{icon("nail_bitten")}</div>
<div class="abs mo" id="cy1l" style="left:60px;width:230px;text-align:center;top:176px;font-size:24px"><b>TISHLASH</b></div>
<div class="abs" id="cy2" style="left:475px;top:34px;width:130px;height:130px">{icon("nail_crack")}</div>
<div class="abs pi" id="cy2l" style="left:415px;width:250px;text-align:center;top:160px;font-size:60px">mo'rt</div>
<div class="abs" id="cy3" style="left:840px;top:34px;width:130px;height:130px">{icon("loop")}</div>
<div class="abs mo" id="cy3l" style="left:770px;width:270px;text-align:center;top:176px;font-size:22px"><b>YANA TISHLASH</b></div>
<svg class="layer" id="cyar" viewBox="0 0 1080 1920"><g fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
<path d="M285 100 H435"/><path d="M420 86 L436 100 L420 114"/><path d="M650 100 H800"/><path d="M785 86 L801 100 L785 114"/></g></svg>
<div class="tag" id="cytag" style="left:390px;top:236px">XAVF · YOPIQ DOIRA</div>''')}

<!-- 2 -->
{doc("d2", 330, f'''
<div class="abs mo" id="d2a" style="left:64px;top:50px;font-size:30px"><b>§ 2</b> · USUL</div>
<div class="abs pi" id="d2t" style="left:58px;top:92px;font-size:104px">Mustahkamlik</div>
<div class="abs mo" id="d2b" style="left:64px;top:230px;font-size:24px">mustahkam tirnoqni tishlashga qiynalasiz</div>
<div class="abs" id="d2c" style="left:860px;top:60px;width:150px;height:150px">{icon("shield")}</div>''')}
{doc("bwd", 330, f'''
<div class="abs mo" id="bwa" style="left:64px;top:40px;font-size:24px"><b>PROTOKOL</b> · HAR KUNI</div>
<div class="abs" id="bw" style="left:80px;top:80px;width:150px;height:150px">{icon("bowl")}</div>
<div class="abs mo" id="bwl" style="left:50px;width:210px;text-align:center;top:236px;font-size:22px"><b>TUZLI SUV</b></div>
<div class="abs" id="ck" style="left:330px;top:84px;width:140px;height:140px">{icon("clock")}</div>
<div class="abs" id="ckn" style="left:500px;top:70px;font-family:JBMono;font-weight:600;font-size:150px;line-height:1;color:{INK};letter-spacing:-.04em">10–15</div>
<div class="abs mo" id="ckl" style="left:508px;top:236px;font-size:24px"><b>MINUT</b> · bir kunda</div>''')}
{doc("eld", 330, '''
<div class="tile" id="t1" style="left:190px;top:36px"><div class="n">20</div><div class="m">40.078</div><div class="s">Ca</div><div class="l">KALSIY</div></div>
<div class="abs pi" id="elp" style="left:470px;width:140px;text-align:center;top:100px;font-size:110px">+</div>
<div class="tile" id="t2" style="left:660px;top:36px"><div class="n">30</div><div class="m">65.38</div><div class="s">Zn</div><div class="l">SINK</div></div>''')}

<!-- 3 -->
{doc("d3", 690, f'''
<div class="abs mo" id="d3a" style="left:0;width:1080px;text-align:center;top:90px;font-size:34px"><b>§ 3</b> · USUL</div>
<div class="abs pi" id="d3t" style="left:0;width:1080px;text-align:center;top:160px;font-size:160px">Xina qo'ying</div>
<div class="abs mo" id="d3b" style="left:0;width:1080px;text-align:center;top:380px;font-size:26px">o'sgan tirnoqni yashiradi · mustahkamlaydi</div>
<div class="abs" id="d3c" style="left:470px;top:440px;width:140px;height:180px">{icon("cone")}</div>''')}
{doc("ndd", 690, f'''
<div class="abs" id="nd" style="left:320px;top:80px;width:440px;height:560px">{NAIL_DIAGRAM}</div>
<div class="abs mo" id="ndl1" style="left:722px;top:162px;font-size:24px"><b>O'SGAN QISM</b></div>
<div class="abs" id="ndeye" style="left:96px;top:140px;width:140px;height:140px">{icon("eye_off")}</div>
<div class="abs mo" id="ndl2" style="left:56px;width:230px;text-align:center;top:300px;font-size:22px"><b>KO'RINMAYDI</b></div>
<div class="abs mo" id="ndl3" style="left:722px;top:330px;font-size:24px;line-height:1.5"><b>XINA BILAN</b><br><b>YOPILADI</b></div>''')}
{doc("chd", 560, f'''
<div class="abs mo" id="cha" style="left:0;width:1080px;text-align:center;top:90px;font-size:26px"><b>NATIJA</b></div>
<div class="tag" id="ch1" style="left:150px;top:200px;font-size:40px;color:{INK};border-color:{INK};padding:16px 26px">✓ MUSTAHKAM</div>
<div class="tag" id="ch2" style="left:610px;top:200px;font-size:40px;color:{INK};border-color:{INK};padding:16px 26px">↑ O'SISH</div>''')}
{seal("ns", 820, 380)}

<!-- CTA -->
<div class="idc ov" id="idc"><img src="assets/avatar.jpg" alt="">
<div class="abs sc" style="left:250px;top:40px;font-size:22px">GUVOHNOMA · XS</div>
<div class="abs pi" style="left:246px;top:74px;font-size:64px">@xina_siren</div>
<div class="abs mo" style="left:250px;top:156px;font-size:22px"><b>155K</b> OBUNACHI · HALOL XINA</div>
<div class="btn" id="btn"><span class="b1">OBUNA BO'LISH</span><span class="b2">✓ OBUNADASIZ</span></div></div>
{doc("pld", 600, f'''
<div class="abs mo" id="pla" style="left:120px;top:400px;font-size:26px"><b>SIZ</b></div>
<div class="abs mo" id="plb" style="left:800px;top:240px;font-size:26px"><b>DO'STINGIZ</b></div>
<svg class="layer" id="plpath" viewBox="0 0 1080 1920"><path d="M150 380 C 380 260 600 420 820 300" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 18"/></svg>
<div class="abs" id="pl" style="left:830px;top:250px;width:120px;height:120px">{icon("plane")}</div>
<div class="abs pi" id="pll" style="left:0;width:1080px;text-align:center;top:80px;font-size:84px">Do'stingizga yuboring</div>''')}

<!-- SUBTITRLAR -->
{chr(10).join(subs)}

<!-- UV-SKANER -->
<div class="uvtint ov" id="uvt"></div>
<div class="uvbar ov" id="uvb"></div>

<!-- YAKUN -->
<div class="layer ov" id="end" style="z-index:60">
  <div class="frame"></div>
  <div class="abs sc" style="left:0;width:1080px;text-align:center;top:420px;font-size:34px">SERTIFIKAT</div>
  <div class="abs mo" style="left:0;width:1080px;text-align:center;top:480px;font-size:24px"><b>№ XS-0001</b> · TOSHKENT</div>
  <div class="abs pi" id="ent1" style="left:0;width:1080px;text-align:center;top:560px;font-size:100px">Tirnoq tishlash</div>
  <div class="abs pi" id="ent2" style="left:0;width:1080px;text-align:center;top:672px;font-size:100px">odati</div>
  <div class="tag" id="stamp" style="left:676px;top:706px;font-size:56px;padding:10px 22px;border-width:5px;transform:rotate(-8deg)">YOPILDI</div>
  {seal("es", 420, 840)}
  <div class="abs sc" style="left:0;width:1080px;text-align:center;top:1120px;font-size:58px;letter-spacing:.16em;color:{INK}">XINA SIREN</div>
  <div class="abs mo" style="left:0;width:1080px;text-align:center;top:1210px;font-size:30px"><b>@xina_siren</b> · +998 33 712 26 07</div>
</div>
"""

    uv_js = "\n".join(
        f'tl.fromTo("#uvb", {{y:-260, opacity:1}}, {{y:1920, duration:1.1, ease:"power1.inOut", immediateRender:{"true" if i == 0 else "false"}}}, {t - 0.55:.2f});\n'
        f'tl.fromTo("#uvt", {{opacity:0}}, {{opacity:1, duration:0.45, ease:IO, immediateRender:{"true" if i == 0 else "false"}}}, {t - 0.55:.2f});\n'
        f'tl.to("#uvt", {{opacity:0, duration:0.7, ease:IO}}, {t + 0.35:.2f});'
        for i, t in enumerate(UV))

    js = f"""
// ---------- HOOK ----------
{doc_js("hd", 0.15, 5.35, 400, [("#hk", 0.4, "{y:10, b:6, d:0.6}"), ("#hn", 0.55, "{y:10, b:6, d:0.6}"), ("#h1", 0.65, "{y:24, b:14, d:0.8}"), ("#h2", 0.95, "{y:24, b:14, d:0.8}")])}
{seal_js("hs", 1.6, 5.35)}

// ---------- 1 ----------
{doc_js("d1", 6.4, 14.2, 360, [("#d1a", 0.4, "{y:10, b:6, d:0.6}"), ("#d1t", 0.55, "{y:24, b:14, d:0.8}"), ("#d1b", 0.95, "{y:10, b:6, d:0.6}")])}
tl.fromTo("#d1c", {{opacity:0}}, {{opacity:1, duration:0.3}}, 10.6); draw("#d1c path", 10.6, 1.0, 0.2);
tl.fromTo("#d1k", {{opacity:0}}, {{opacity:1, duration:0.3}}, 11.7); draw("#d1k path", 11.7, 0.6);

// ---------- sabab ----------
{doc_js("cy", 14.95, 19.4, 330)}
tl.fromTo("#cy1, #cy2, #cy3, #cyar", {{opacity:0}}, {{opacity:1, duration:0.01}}, 15.0);
draw("#cy1 path", 15.2, 0.8, 0.15); enter("#cy1l", 15.5, {{y:10, b:6, d:0.6}});
draw("#cyar path:nth-child(1), #cyar path:nth-child(2)", 15.9, 0.45, 0.2);
draw("#cy2 path", 16.35, 0.8, 0.15); enter("#cy2l", 16.8, {{y:14, b:10, d:0.7}});
draw("#cyar path:nth-child(3), #cyar path:nth-child(4)", 17.7, 0.45, 0.2);
draw("#cy3 path", 18.1, 0.8, 0.2); enter("#cy3l", 18.5, {{y:10, b:6, d:0.6}});
enter("#cytag", 18.8, {{y:0, b:8, s:0.86, d:0.6}});

// ---------- 2 ----------
{doc_js("d2", 20.55, 24.35, 330, [("#d2a", 0.4, "{y:10, b:6, d:0.6}"), ("#d2t", 0.55, "{y:24, b:14, d:0.8}"), ("#d2b", 0.95, "{y:10, b:6, d:0.6}")])}
tl.fromTo("#d2c", {{opacity:0}}, {{opacity:1, duration:0.3}}, 21.4); draw("#d2c path", 21.4, 0.9, 0.15);
{doc_js("bwd", 24.7, 28.4, 330, [("#bwa", 0.3, "{y:10, b:6, d:0.6}"), ("#bwl", 0.7, "{y:10, b:6, d:0.6}"), ("#ckn", 2.0, "{y:18, b:12, s:1.05, d:0.8}"), ("#ckl", 2.3, "{y:10, b:6, d:0.6}")])}
tl.fromTo("#bw, #ck", {{opacity:0}}, {{opacity:1, duration:0.01}}, 24.8);
draw("#bw path", 24.95, 0.9, 0.12); draw("#ck path, #ck circle", 25.9, 0.9, 0.1);
tl.fromTo("#ck path:nth-child(3)", {{rotation:0, svgOrigin:"60 62"}}, {{rotation:300, svgOrigin:"60 62", duration:2.2, ease:"sine.inOut"}}, 26.2);
{doc_js("eld", 28.55, 31.6, 330, [("#t1", 1.2, "{y:24, b:12, d:0.8}"), ("#elp", 1.65, "{y:0, b:10, s:0.86, d:0.6}"), ("#t2", 1.9, "{y:24, b:12, d:0.8}")])}

// ---------- 3 ----------
{doc_js("d3", 32.75, 35.3, 690, [("#d3a", 0.4, "{y:10, b:6, d:0.6}"), ("#d3t", 0.55, "{y:30, b:16, s:1.04, d:0.9}"), ("#d3b", 1.0, "{y:10, b:6, d:0.6}")])}
tl.fromTo("#d3c", {{opacity:0}}, {{opacity:1, duration:0.3}}, 33.9); draw("#d3c path", 33.9, 0.9, 0.12);
{doc_js("ndd", 35.55, 44.25, 690, [("#ndl1", 1.65, "{y:10, b:6, d:0.6}"), ("#ndl2", 2.75, "{y:10, b:6, d:0.6}"), ("#ndl3", 7.25, "{y:10, b:6, d:0.6}")])}
tl.fromTo("#nd, #ndeye", {{opacity:0}}, {{opacity:1, duration:0.01}}, 35.7);
draw("#nd .nd-finger", 35.8, 1.1); draw("#nd .nd-nail", 36.3, 1.0);
tl.fromTo("#nd .nd-cut", {{opacity:0}}, {{opacity:1, duration:0.6, ease:IO}}, 36.9);
draw("#nd .nd-dim", 37.0, 0.6);
draw("#ndeye path, #ndeye circle", 38.0, 0.8, 0.15);
tl.to("#ndeye, #ndl2", {{opacity:0, filter:"blur(8px)", duration:0.5, ease:IO}}, 40.6);
tl.fromTo("#nd .nd-fill", {{scaleY:0, transformOrigin:"50% 100%"}}, {{scaleY:1, duration:1.3, ease:"power2.inOut"}}, 42.5);
{doc_js("chd", 44.45, 49.25, 560, [("#cha", 0.4, "{y:10, b:6, d:0.6}"), ("#ch1", 2.3, "{y:0, b:10, s:0.86, d:0.7}"), ("#ch2", 3.9, "{y:0, b:10, s:0.86, d:0.7}")])}
{seal_js("ns", 46.9, 49.25)}

// ---------- CTA ----------
enter("#idc", 50.5, {{y:60, b:14, d:0.9}});
tl.to("#btn", {{scale:0.92, duration:0.22, ease:IO}}, 53.8);
tl.to("#btn", {{scale:1, duration:0.4, ease:IN}}, 54.02);
tl.fromTo("#btn .b1", {{opacity:1}}, {{opacity:0, duration:0.35, ease:IO}}, 53.9);
tl.fromTo("#btn .b2", {{opacity:0, scale:1.2}}, {{opacity:1, scale:1, duration:0.45, ease:IN}}, 53.95);
tl.to("#btn", {{backgroundColor:"{GL}", duration:0.4, ease:IO}}, 53.3);
exit("#idc", 55.05, 0.5);
{doc_js("pld", 55.2, 58.45, 600, [("#pll", 0.45, "{y:24, b:14, d:0.85}"), ("#pla", 1.2, "{y:10, b:6, d:0.6}"), ("#plb", 2.3, "{y:10, b:6, d:0.6}")])}
tl.fromTo("#plpath", {{clipPath:"inset(0% 100% 0% 0%)"}}, {{clipPath:"inset(0% 0% 0% 0%)", duration:1.2, ease:IO}}, 56.4);
tl.fromTo("#pl", {{opacity:0}}, {{opacity:1, duration:0.01}}, 57.2); draw("#pl path", 57.2, 0.8, 0.2);
tl.fromTo("#pl", {{x:-50, y:30}}, {{x:20, y:-10, duration:1.2, ease:"sine.inOut"}}, 57.2);

// ---------- UV ----------
{uv_js}

// ---------- SUBTITR ----------
{subs_js(extra=lambda c: f'tl.fromTo("#sb{c["i"]} .m", {{backgroundSize:"0% 100%"}}, {{backgroundSize:"100% 100%", duration:0.5, ease:IO}}, {c["acc_t"]:.2f});')}

// ---------- YAKUN ----------
tl.fromTo("#end", {{opacity:0}}, {{opacity:1, duration:0.6, ease:"sine.inOut"}}, 58.75);
enter("#ent1", 59.0, {{y:20, b:12, d:0.8}});
enter("#ent2", 59.15, {{y:20, b:12, d:0.8}});
tl.fromTo("#stamp", {{opacity:0, scale:1.25, filter:"blur(8px)", rotation:-14}}, {{opacity:0.92, scale:1, filter:"blur(0px)", rotation:-8, duration:0.5, ease:"power3.out"}}, 59.55);
{seal_js("es", 59.3, 60.6).replace('exit("#es", 60.60, 0.5);', '')}
"""
    sfx_extra = [(t - 0.05, "select_click.wav", 0.5) for t in (1.6, 46.9, 59.55)]
    return dict(faces=FACES, css=CSS, body=body, js=js, bg=PAPER, sweeps=UV, sfx="sweep_small.wav", sfx_gain=0.32,
                sfx_lead=0.55, sfx_extra=sfx_extra, assets=["guil.png", "micro.png"])
