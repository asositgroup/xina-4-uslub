# D · Kundalik (founder's diary) — `scripts/style_d.py`

**G'oya.** Video mutaxassisning shaxsiy yo'li sifatida, uning kundaligi sahifalarida ko'rsatiladi: lavanda skotch bilan yopishtirilgan
qo'lyozma qaydlar («Tirnoq tishlash odatimni / 17 yoshimda tashlaganman» — birinchi shaxsda, uning o'z so'zlari), qizil sana/«3 LAYFXAK» muhri,
har maslahat **chek-list**da belgilanadi (☐ → qizil ✓), polaroid, qog'oz yirtilib sahifa almashadi. Iliq, samimiy — lekin bolalarcha emas
(emoji, multfilm effektlari yo'q). Subtitr ham qog'oz yorliqda.

## Palitra
| Token | Hex | Ishlatilishi |
|---|---|---|
| NOTE | `#FBF7EF` | qayd kartalari (+ `grain.png`), subtitr yorlig'i |
| PAPER | `#EFE7DA` | yirtiq qog'oz, yakun fon (nuqtali to'r 48 px) |
| INK | `#2C2433` | qo'lyozma, ikonka, katakcha |
| ikkinchi siyoh | `#5B4B78` | Caveat 600 izohlar, Karla CAPS |
| TAPE (skotch) | `#B8A3E8` | 135° chiziqli lavanda skotch `rgba(184,163,232,.85)/(200,183,240,.85)` |
| lavanda karta | `#E8DEF9` | `.note.lav` |
| RED (muhr) | `#B23A48` | muhr, katakcha ✓, «mo'rt», «bekitadi!», doira belgisi |
| aksent siyoh | `#6A4FB0` | subtitrdagi Caveat aksent |

## Shriftlar
- **Caveat** 600/700 — qo'lyozma 46–80 px (sarlavhalar, izohlar, chek-list, polaroid imzosi, «Xina Siren» 130 px).
- **DM Serif Display** — katta raqam/belgi («10–15» 110 px, «Ca/Zn» 110 px).
- **Karla 700** — subtitr 46 px, CAPS yorliqlar (`letter-spacing .14em`).

## Grade
`#cam { filter: sepia(.12) saturate(.96) contrast(1.03) }` + `#grain` (512 px qog'oz donasi, opacity .55, multiply) butun kadrda.

## Komponentlar
- **Qayd kartasi** (`card(id,x,y,w,h,rot,inner,tape_x,lav)`): NOTE + grain, soya, qiyalik −4…+4°; tepasida skotch (220×54, karta qiyaligiga qarshi).
  Kirish: `y +46, rotation rot−4 → rot`, blur 12→0, 0.8 s `expo.out`; chiqish `y −24` + blur 0.55 s.
- **Qo'lyozma yozilishi**: `clipPath inset(-20% 100% -20% 0%) → 0%` 0.8–1.0 s `power1.inOut` (harf-harf span EMAS).
- **Katakcha** (`checkbox()`): 64 px INK ramka, ichida qizil ✓ yo'l (9 px) aytilgan paytda chiziladi.
- **Muhr** (`.stamp`): qizil doira 5 px + ichki punktir, `rotation 18→12`, scale 1.15→1, blur 8→0, 0.45 s `power3.out` + yumshoq click.
- **Yirtiq qog'oz chizig'i** (`.strip`): tepadan tushadigan to'liq kenglikdagi qog'oz, pastki cheti `jag()` poligon (tasodifiy tishli, seed bilan determinatsiyalangan).
- **Polaroid** (`.pol`): oq ramka, rasm (avatar), skotch, Caveat imzo.
- **Chek-list sahifasi** (3-bo'lim): «KUNDALIK · 3 LAYFXAK» + 3 qator: 1 va 2 avtomatik ✓, «Xina qo'ying» yoziladi va ✓ + konus.
- **Subtitr**: NOTE+grain yorliq, ±1° tasodifiy qiyalik (seed 11), INK Karla 700 46 px; aksent Caveat 700 64 px `#6A4FB0` (`margin 0 6px`). `z-index:70`.
- **O'tish — yirtiq qog'oz** (`TEAR` = kesim vaqtlari): 1080×2400 PAPER varaq, ikki cheti `jag()` tishli; y 1960 → −220 (0.7 s `power2.in`,
  kesimda ekran to'liq yopiq) → −2500 (0.85 s `power2.out`). SFX `air_woosh.wav` gain 0.4. Subtitr qog'oz USTIDA.
- **Yakun**: PAPER nuqtali to'r, polaroid (avatar, −3°), «Xina Siren» Caveat 130 px yoziladi, CAPS «halol xina · manikyur · toshkent»,
  telefon, qizil muhr «HALOL · XINA SIREN» (12°).

## Namunadagi bo'g'inlar
| Vaqt | Bo'g'in | Element |
|---|---|---|
| 0.2–5.9 | Hook | skotchli qayd: «Tirnoq tishlash odatimni» / «17 yoshimda tashlaganman» (uning so'zlari) + muhr «3 LAYFXAK» (2.3) |
| 5.43 | yirtiq | (kesim 6.13) |
| 6.5–14.75 | 1 | qayd «☐ 1. Halol manikyur» → ✓ (9.1, «qildiringlar»); 10.4 lavanda karta tirnoq «toza = ✓» |
| 14.95–19.95 | sabab | yirtiq qog'oz chizig'i: tishlash → mo'rt (qizil) → yana tishlash, qo'lda chizilgan strelkalar |
| 19.5 | yirtiq | |
| 20.55–24.9 | 2 | «☐ 2. Mustahkamlik» → ✓ (23.55) + lavanda karta qalqon |
| 24.7–28.95 | protokol | keng karta: kosa «tuzli suv» + soat + «10–15» + «minut, bir kunda» + qizil qo'lda doira |
| 29.7–32.15 | vitamin | qayd «20 Ca kalsiy» + «+» + lavanda «30 Zn sink» |
| 31.77 | yirtiq | (kesim 32.47) |
| 32.85–35.9 | 3 | chek-list sahifasi: ✓ Halol manikyur, ✓ Mustahkamlik, «Xina qo'ying» yoziladi → ✓ + konus |
| 35.55–44.8 | chizma | eskiz kartasi: tirnoq, «o'sgan qism»; 38.0 lavanda karta ko'z ✗ «ko'rinmaydi»; 42.5 xina; 42.8 qizil «bekitadi!» |
| 46.75–49.8 | natija | qayd «mustahkam» (qalqon) + lavanda «o'sadi» (↑) |
| 49.1 | yirtiq | (kesim 49.8) |
| 50.4–55.6 | CTA | polaroid @xina_siren + qayd «Sahifamga ☐ obuna bo'ling» → ✓ (53.8) |
| 55.25–59.0 | yuboring | qayd «do'stingizga yuboring» + nuqtali yo'l + samolyot |
| 58.75–60.6 | yakun | kundalik oxirgi sahifasi |

## Qilinmaydi
Harf-harf span yozuv (Caveat kerningi buziladi) · subtitrga `clip-path` tishli chet (yuqori harflarni kesadi) ·
`card` ichida `f-string` da `\'` (Python 3.9 — `&#39;` ishlat) · skotch/karta yuzga tushishi.
