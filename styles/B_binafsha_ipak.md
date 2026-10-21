# B · Binafsha ipak (lavender silk luxe) — `scripts/style_b.py`

**G'oya.** Brendning lavanda formasi/qo'lqopi/qadog'i lyuks go'zallik jurnali tiliga ko'tariladi: yuqori kontrastli Bodoni serif,
ingichka marvarid chiziqlar, muzli shisha kartalar, kadrlar ustidan sirpanib o'tadigan lavanda ipak. Soyalarga yengil olxo'ri tusi, teri tabiiy.
Eng «qimmat» ko'rinish.

## Palitra
| Token | Hex | Ishlatilishi |
|---|---|---|
| PLUM (tun binafsha) | `#1D0F2A` | band gradienti `rgba(29,15,42,.9→.8→.35→0)`, yakun fon (radial `#3a1f55→#1d0f2a`), subtitr pill `rgba(29,15,42,.76)` |
| SILK (ipak lavanda) | `#CDB6FF` | Bodoni kursiv aksent, strelkalar, «obunadasiz» tugma |
| AME (ametist) | `#7E5ACB` | ipak gradienti o'rtasi |
| PEARL (marvarid) | `#EFE8F7` | Jost CAPS, ikonka chiziqlari, marvarid chiziq (`.rule` gradient), tugma fon |
| xina to'ldirish | `#3B1830` | tirnoq chizmasi |

## Shriftlar
- **Bodoni Moda** (var, `opsz` o'qi): upright 600 `font-variation-settings:"opsz" 14; font-optical-sizing:none` — MAJBURIY
  (aks holda katta o'lchamda soch chiziqlari yo'qoladi, «N» ko'rinmaydi). Masthead/plitka 98–140 px.
- **Bodoni Moda Italic** 600–700 (`opsz` 11–14) — aksent, raqamlar 200–330 px, subtitr aksenti 60 px.
- **Jost** 400–500 — CAPS `letter-spacing:.32em` 22–40 px, subtitr 46 px.

## Grade
`#cam { filter: saturate(.92) contrast(1.04) }` + `#tint` `rgba(80,40,120,.10)` multiply + `#vig` radial vinyetka `rgba(29,15,42,.45)` chetlarda.

## Komponentlar
- **Band** (`.band`): tepa PLUM gradient polosa; balandlik kadr tepa bo'sh zonasi (S1 430, S2 380, S3 340, keng 560–700).
- **Masthead hook**: Jost CAPS «XINA SIREN · MASLAHAT» 26 px + marvarid chiziq (scaleX 0→1 0.9 s) + Bodoni 98 px «Tirnoq tishlash» +
  Bodoni Italic 98 px SILK «odatini tashlash» + shisha pill «● 3 LAYFXAK».
- **Bo'lim** (`section(k,label)`): Bodoni Italic 200 px raqam + Jost CAPS 34 px yorliq + marvarid chiziq; ixtiyoriy ikonka.
- **Muzli shisha** (`.glass`): `rgba(255,255,255,.13)`, 1.5 px oq .36 chegara, `backdrop-filter: blur(22px) saturate(1.2)`, radius 36, soya.
- **Marvarid nuqta** (`.pearl`): 22 px `radial-gradient(#fff, #e7dcf5, #a998c4)`.
- **Subtitr**: Jost 500 46 px oq, PLUM .76 shisha pill (radius 30, blur 14); aksent so'z Bodoni Italic 700 60 px SILK. `z-index:70`.
- **O'tish — ipak** (`SILKS` = kesim vaqtlari, cho'qqi aynan kesimda): 3800×3800 element (`left:-1360; top:-940`), 115° gradient
  (shaffof 17% → `#e9ddff 24%, #a585e6 34%, #d7c4fb 44%, #7e5acb 54%, #cdb6ff 64%, #efe6ff 76%` → shaffof 83%) + mato burmalari
  (repeating 115°), ustidan oq `sheen` (screen). Harakat yo'nalish vektori (0.906, 0.423) bo'yicha −2600 → +2600, 1.5 s `power2.inOut`,
  boshlanish = kesim − 0.75 (o'rtada ekran 100% yopiq). SFX `air_woosh.wav` gain 0.42, 1.0 s oldin.
- **Profil**: shisha karta 880×270, avatar 170 px SILK halqa, @handle Bodoni Italic 64 px, Jost CAPS tavsif, PEARL tugma → bosilib SILK.
- **Yakun**: PLUM radial fon, Jost CAPS «HALOL XINA STUDIYASI · TOSHKENT», «XINA SIREN» Bodoni 140 px `letter-spacing:.06em`,
  marvarid chiziq, @handle Bodoni Italic 72 px SILK, telefon Jost 32 px.

## Namunadagi bo'g'inlar
| Vaqt | Bo'g'in | Element |
|---|---|---|
| 0.05–5.85 | Hook | band + masthead + 2 qator sarlavha + «3 LAYFXAK» pill |
| 6.13 | ipak | (kesim) |
| 6.45–14.75 | 1-bo'lim | «1 HALOL MANIKYUR»; 10.4 shisha kvadrat ichida tirnoq + ✓ |
| 14.95–19.9 | sabab | 3 shisha karta: tishlash → mo'rt (Bodoni Italic) → yana tishlanadi, SILK strelkalar |
| 20.2 | ipak | (bo'lim 2) |
| 20.55–24.9 | 2-bo'lim | «2 MUSTAHKAMLIK» + qalqon |
| 24.7–28.9 | protokol | keng shisha karta: kosa «tuzli suv» + soat + «10–15» Bodoni Italic 132 px + «minut · bir kunda» |
| 28.5–32.1 | vitamin | ikki shisha plitka Ca/Zn + «+» |
| 32.47 | ipak | (kesim) |
| 32.75–35.75 | 3-bo'lim | ulkan «3» Bodoni Italic 330 px + «XINA QO'YING» + konus |
| 35.35–44.75 | chizma | PEARL chiziqli tirnoq, ko'z ✗, xina to'ladi (42.5), «xina bekitadi» (42.8) |
| 44.4–49.75 | natija | shisha pill'lar «mustahkam» / «o'sish» |
| 49.8 | ipak | (kesim) |
| 50.5–55.55 | CTA | shisha profil kartasi, tugma 53.8 |
| 55.2–58.95 | yuboring | samolyot + «do'stingizga yuboring» Bodoni Italic 92 px |
| 58.75–60.6 | yakun | PLUM yakun |

## Qilinmaydi
Bodoni `opsz` avtomatik (ingichka chiziqlar yo'qoladi) · subtitr pill shaffof (<.7 — kontrast tushadi) · ipak cho'qqisi kesimdan farqli vaqtda.
