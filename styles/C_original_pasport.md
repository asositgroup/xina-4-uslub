# C · Original pasport (authenticity document) — `scripts/style_c.py`

**G'oya.** Brendning «original vs soxta» va «halol» tushunchasi himoyalangan hujjat tiliga o'giriladi: banknotdagi gilosh naqshlar,
seriya raqami «№ XS-0001», mikromatn, kamalak-folga golografik «HALOL» muhri, UV-skaner o'tishi, oxirida «Tirnoq tishlash odati — YOPILDI»
sertifikati. Maslahatlar «§ 1 · USUL» kabi hujjat bandlari. Mahsulot/haqiqiylik mavzusiga eng kuchli (dizayn taxtasida tavsiya).

## Palitra
| Token | Hex | Ishlatilishi |
|---|---|---|
| PAPER | `#F6F3FB` | hujjat paneli `rgba(246,243,251,.95)`, subtitr yorlig'i, yakun fon |
| INK (siyoh) | `#231638` | sarlavha, ikonka, tugma, muhr yadrosi |
| mono matn | `#45366A` | JetBrains Mono (kontrast ≥4.5:1 uchun — `#5b4a80` yetmadi) |
| GL (gilosh lavanda) | `#8C6FD0` | gilosh chiziqlari (`assets/textures/guil.png`), panel cheti, marker `rgba(140,111,208,.45)`, «obunadasiz» |
| RED (o'chirish) | `#C23B3B` | «XAVF» yorlig'i, «YOPILDI» muhri |
| Gologramma | `conic-gradient(#ffd1f3,#c9b6ff,#9fe8ff,#c8ffd8,#fff0b3,#ffd1f3)` | muhr halqasi (mask: 82–83 px ichi shaffof) |

## Shriftlar
- **Playfair Display SC 700** — «TAVSIYANOMA», «SERTIFIKAT», muhr yadrosi, Ca/Zn plitka belgisi (`letter-spacing .14–.32em`).
- **Playfair Display Italic 700** — sarlavhalar 84–160 px («Tirnoq tishlash», «Halol manikyur», «Xina qo'ying», «@xina_siren»).
- **JetBrains Mono 500/600** — seriya, protokol, yorliqlar 22–34 px, «10–15» 150 px (`letter-spacing:-.04em`), muhr halqa matni 17 px.
- **Archivo 600** — subtitr 44 px.

## Grade
`#cam { filter: contrast(1.05) brightness(1.02) }`.

## Komponentlar
- **Hujjat paneli** (`doc(id, h, inner)`): to'liq kenglik, tepadan tushadi (`y −h−20 → 0`, blur 10→0, 0.9 s `expo.out`), fon PAPER + `guil.png`
  (1080×700, markazlangan), pastida `micro.png` marquee (x 0→−260 butun turish davomida, `ease:none` — doimiy tezlik) + 3 px nuqtali GL chet.
  Chiqish: `y −50`, blur, 0.55 s. Balandlik = kadr tepa bo'sh zonasi (S1 400, S2 360, S3 330, keng 560–690).
  Mikromatn MATN emas — PNG (hyperframes check matn chetdan chiqishini xato deydi).
- **Golografik muhr** (`seal(id,x,y,word)`): 240 px; halqa conic gradient doimiy aylanadi (40°/s), ichki SVG halqa matni
  «ORIGINAL • XINA SIREN • HALOL • TOSHKENT •» teskari aylanadi (15°/s, `svgOrigin 120 120`); kirish «bosilish» scale 1.14→1 + blur 10→0,
  0.6 s `power3.out` (overshootsiz) + yumshoq `select_click.wav`.
- **Element plitkasi** (`.tile` 230×250): 4 px INK ramka, atom raqami (20/30), massa (40.078 / 65.38), belgi PlayfairSC 100 px, nom CAPS.
- **Yorliq/teg** (`.tag`): JBMono 600 CAPS, 3 px ramka (RED yoki INK) — «XAVF · YOPIQ DOIRA», «✓ MUSTAHKAM», «↑ O'SISH».
- **Subtitr**: PAPER yorliq (radius 8, soya), INK Archivo 600 44 px; aksent so'z lavanda marker `background-size 0→100%` 0.5 s (aksent so'zida).
- **O'tish — UV-skaner** (`UV` = kesim vaqtlari): 1080×260 nur (`linear-gradient` binafsha→oq chiziq, `mix-blend: screen`) y −260 → 1920,
  1.1 s `power1.inOut`, boshlanish = kesim − 0.55; butun kadr binafsha tus (`rgba(84,40,210,.38)` multiply) 0.45 s yonib 0.7 s so'nadi.
  SFX `sweep_small.wav` gain 0.32. Subtitr nur USTIDA.
- **Guvohnoma kartasi** (`.idc` 900×300): gilosh fon, kvadrat avatar 180 px INK ramka, «GUVOHNOMA · XS», @handle italic 64 px,
  «155K OBUNACHI · HALOL XINA» (haqiqiy son), tugma «OBUNA BO'LISH» → «✓ OBUNADASIZ» (GL).
- **Yakun — sertifikat**: PAPER + pastdagi gilosh, ikki qatlamli INK/GL ramka, «SERTIFIKAT», «№ XS-0001 · TOSHKENT»,
  «Tirnoq tishlash / odati» italic 100 px, qizil «YOPILDI» muhri (−8°, 1.25→1 bosilish + click), golografik muhr, «XINA SIREN» SC 58 px, @handle · telefon.

## Namunadagi bo'g'inlar
| Vaqt | Bo'g'in | Element |
|---|---|---|
| 0.15–5.9 | Hook | panel «TAVSIYANOMA · № XS-0001 · 3 USUL» + «Tirnoq tishlash / odatini tashlash» + muhr (1.6) |
| 5.58 | UV | (kesim 6.13) |
| 6.4–14.75 | § 1 | «Halol manikyur» + «toza · kap-katta · tishlashga ko'z qiymaydi»; tirnoq + ✓ |
| 14.95–19.95 | sabab | TISHLASH → mo'rt → YANA TISHLASH + qizil teg «XAVF · YOPIQ DOIRA» |
| 19.65 | UV | |
| 20.55–24.9 | § 2 | «Mustahkamlik» + «mustahkam tirnoqni tishlashga qiynalasiz» + qalqon |
| 24.7–28.95 | protokol | «PROTOKOL · HAR KUNI»: kosa «TUZLI SUV» + soat + «10–15» mono + «MINUT · bir kunda» |
| 28.55–32.15 | vitamin | Ca (40.078) + Zn (65.38) element plitkalari |
| 31.92 | UV | (kesim 32.47) |
| 32.75–35.85 | § 3 | markazda «§ 3 · USUL», «Xina qo'ying» 160 px, konus |
| 35.55–44.8 | chizma | texnik chizma: «O'SGAN QISM», ko'z ✗ «KO'RINMAYDI», xina to'ladi 42.5, «XINA BILAN YOPILADI» |
| 44.45–49.8 | natija | «NATIJA» + tegler ✓ MUSTAHKAM / ↑ O'SISH + golografik muhr (46.9) |
| 49.25 | UV | (kesim 49.8) |
| 50.5–55.55 | CTA | guvohnoma kartasi, tugma 53.8 |
| 55.2–59.0 | yuboring | «Do'stingizga yuboring», SIZ → DO'STINGIZ nuqtali yo'l + samolyot (57.2) |
| 58.75–60.6 | yakun | sertifikat «YOPILDI» |

## Qilinmaydi
Mikromatnni HTML matn qilish · mono matn `#5b4a80` (kontrast past) · muhr «sakrab» bosilishi (back.out) · sarlavha muhr ostiga kirishi (`textw` bilan o'lcha).
