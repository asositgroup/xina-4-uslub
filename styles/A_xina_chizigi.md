# A · Xina chizig'i (henna line) — `scripts/style_a.py`

**G'oya.** Akkauntda eng ko'p ko'rishni «jonli chizilayotgan chiziq» olib keladi (qosh geometriyasi, konusdan chiqayotgan xina).
Shu uslubda ekrandagi HAR element xina konusidan siqilgandek paydo bo'ladi: chiziq avval **yangi pasta** rangida (zaytun-jigarrang),
keyin ko'z oldida **dog'** rangiga qorayadi — haqiqiy xina ham shunday qorayadi. Faqat xinaga xos imzo. Seriya uchun eng mos (doimiy brend tili).

## Palitra
| Token | Hex | Ishlatilishi |
|---|---|---|
| CREAM (krem teri) | `#F3E7DA` | scrim, subtitr plashkasi (`rgba(247,240,231,.93)`), yakun fon |
| PASTE (yangi pasta) | `#7D6A2E` | yozuv/chiziq boshlang'ich rangi |
| STAIN (xina dog'i) | `#2A150C` | yakuniy chiziq/matn, ikonkalar, tugma |
| LAV (brend lavanda) | `#C7AEF7` / urg'u chizig'i `#9A7BE0` | subtitr aksent ostiga chiziq, avatar halqasi, «obunadasiz» tugma `#8A6CD6` |
| xina to'ldirish | `#3A1D10` | tirnoq chizmasidagi xina |

## Shriftlar (assets/fonts)
- **Pinyon Script** 60–190 px — sarlavhalar («tashlash», «Halol manikyur», «Xina qo'ying», «Xina Siren»), `padding-right:30px` (kursiv dum kesilmasin).
- **Cormorant Garamond 600** — raqamlar («3», «10–15», «Ca/Zn», bo'lim raqami 110 px).
- **Manrope 700/800** — CAPS kicker (30 px, `letter-spacing:.3em`), yorliqlar 26–44 px, subtitr 52 px.

## Grade
Yo'q (tabiiy). Faqat `#cam` kamera «nafasi».

## Komponentlar (1080×1920 koordinata)
- **Scrim** (`.scrim`): tepa polosa, chiziqli gradient `rgba(246,238,228,.95)→.88 (62%)→.45 (82%)→0`; BALANDLIK kadrning tepa bo'sh zonasi:
  S1 420, S2 360–380, S3 340, keng kadrlar 560–690. Radial scrim ISHLATMA — hijob tepasini oqartiradi.
- **Konus uchi** (`.tip`): 26 px doira `radial-gradient(#7a5530, #2a150c)`, yozuv `clip-path inset` ochilishi bilan bir xil vaqtda x bo'yicha siljiydi
  (masofa = `textw.tw("Pinyon", px, matn) − 30`).
- **Yozuv ochilishi**: `clipPath inset(-20% 100% -20% 0%) → inset(-20% 0% -20% 0%)`, 0.8–1.6 s `power1.inOut` + `color PASTE→STAIN` 1.0–1.8 s `sine.inOut`.
- **Nuqtali halqa** (`ring(cx,cy,r,n)`): 22–28 nuqta (katta/kichik navbat), har nuqta `scale .4→1` 0.45 s, stagger 0.025–0.03.
- **Bo'lim** (`section(k, title, top, size)`): chapda halqa + Cormorant raqam, o'ngda Pinyon sarlavha, ixtiyoriy ikonka (sarlavha oxiridan +40 px).
- **Mehndi naqsh** (`vine()`): poyacha + 5 barg (yopiq tomchi) + nuqtalar, `strokeDashoffset` chizish (poya 1.6–2 s, barglar 0.7 s, stagger 0.18–0.22).
- **Ikonkalar** (`common.ICONS`): STAIN, `stroke-width 5.5`, `draw()` 0.8–1.0 s `power2.inOut`.
- **Info qatorlar**: Pinyon sarlavha («Nega original?») + mehndi-nuqtali bullet (aylanib kiradi) + Manrope 44 px.
- **Pill/chip** (`.pill`): 4 px STAIN chegarali krem pill, ikonka 66 px + Manrope 44 px.
- **Profil kartasi** (`.prof`): 860×250 krem karta, avatar 160 px (lavanda halqa), @handle Manrope 800 50 px, tugma «Obuna bo'lish» → bosilish
  (scale .92 0.22 s + 1.0 0.4 s `expo.out`) + matn almashuvi «✓ Obunadasiz» (crossfade + 1.2→1) + fon lavandaga.
- **Qog'oz samolyot**: nuqtali yo'l (`clipPath` ochilishi) + `plane` ikonkasi chizilib, sine bilan ko'tarilib siljiydi.
- **Subtitr**: krem plashka (radius 18, soya), STAIN Manrope 700 52 px; aksent so'z ostiga lavanda chiziq `background-size 0%→100%` 0.55 s
  (aksent so'z aytilgan paytda). `z-index:70`.
- **O'tish — xina chizig'i** (`SWEEPS`): 110 px qalin diagonal S-chiziq (gradient `#4a2a16→#2a150c→#5a3420`), 0.42 s chiziladi + 0.62 s «o'chib» ketadi
  (`strokeDashoffset L→0→−L`); SFX `sweep_small.wav` gain 0.35. Subtitr chiziq USTIDA qoladi.
- **Yakun kartasi** (`#end`): krem fon, ikki yonda mehndi naqsh (0.7 masshtab), «Xina Siren» Pinyon 170 px yoziladi (pasta→dog'),
  CAPS «HALOL XINA · MANIKYUR · TOSHKENT», @handle 54 px, telefon 40 px.

## Namunadagi bo'g'inlar (vaqt — sekund, so'zga bog'langan)
| Vaqt | Bo'g'in | Element |
|---|---|---|
| 0.1–5.45 | Hook | kicker «TIRNOQ TISHLASH ODATINI» + Pinyon «tashlash» (konus uchi bilan) + halqa «3 LAYFXAK» + chap mehndi naqsh |
| 5.72 | o'tish | xina chizig'i (kesim 6.13) |
| 6.3–14.25 | 1-bo'lim | halqa «1» + «Halol manikyur»; 10.6 tirnoq ikonkasi + ✓ |
| 15.0–19.75 | sabab | yopiq doira: tishlash → mo'rt (Pinyon, qorayadi) → oson tishlanadi + qaytish strelkasi |
| 19.86 | o'tish | xina chizig'i |
| 20.4–24.4 | 2-bo'lim | «Mustahkamlik» + qalqon |
| 24.75–28.9 | protokol | kosa «tuzli suv» + soat (strelka 300° aylanadi) + «10–15» (26.7, so'z bilan) «minut · bir kunda» |
| 28.5–32.4 | vitamin | Ca 20 «kalsiy» (29.75) + «+» + Zn 30 «sink» (30.45) plitkalari chiziladi |
| 32.06 | o'tish | xina chizig'i (kesim 32.47) |
| 32.5–35.75 | 3-bo'lim | katta halqa «3» + «Xina qo'ying» 150 px + konus |
| 35.35–44.25 | chizma | barmoq+tirnoq chiziladi, kesish chizig'i, «o'sgan qism»; 38.0 ko'z ✗ «ko'rinmaydi»; 42.5 xina tirnoqni to'ldiradi; 42.8 «xina bekitadi» |
| 44.4–49.7 | natija | pill «mustahkam» (46.75) + «o'sish» (48.35) + o'ng mehndi |
| 49.40 | o'tish | xina chizig'i (kesim 49.8) |
| 50.2–55.55 | CTA | profil kartasi; 53.8 tugma bosiladi («obuna» so'zi) |
| 55.2–59.0 | yuboring | «do'stingizga yuboring» Pinyon + nuqtali yo'l + samolyot (57.2) |
| 58.75–60.6 | yakun | krem yakun kartasi |

## Qilinmaydi
Radial scrim (bosh oqaradi) · oq subtitr och ko'ylak ustida (kontrast <3:1) · chiziq subtitrni yopishi · overshoot.
