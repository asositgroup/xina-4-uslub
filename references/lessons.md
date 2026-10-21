# Saboqlar va tuzoqlar (Xina Siren loyihasidan, 2026-10-16 … 21)

## Auphonic
- Bepul tarif jingli ~6.4 s: 20 s faylda OXIRIDA, 59 s faylda BOSHIDA bo'ldi. Boshidan uzunlikka kesish = jingl qoladi + oxirgi 6.4 s nutq yo'qoladi.
  Yechim `auphonic_align.py`: 300–3400 Hz konvert o'zaro korrelyatsiyasi (10 ms dag'al, 1 ms aniq) → asl ovoz natija ichida topiladi →
  aynan asl uzunlikda kesiladi → boshi/o'rtasi/oxiri ±20 ms tekshiriladi (r≈0.8). Natijani qayta yuklash kredit sarflamaydi:
  `GET /api/production/{uuid}.json` → `download_url` (bearer header, `-L`).
- Har production ≥~3 daqiqa hisoblanadi (20 s sinov 0.05 soat oldi) — keraksiz sinov qilma, qisqa kliplarni birlashtir.
- Juda past manba (−36.6 LUFS, salon shovqini): speech_isolation natijasi −15.5 LUFS, toza nutq. RMS trough metrikasi bunday manbada aldaydi.

## Transkript va subtitr
- Whisper uz rejimi o'zbekchani qozoq/turkcha aralash yozadi; kk va tr rejimlari birinchi gapni ochib berdi («onetke ushinda taj aganman» →
  tr «17 yaşında taşıyacağım» → «17 yoshimda tashlaganman»). MMS `score` buni 68 vs 161–175 ball bilan tasdiqladi.
- MMS CTC NLL qisqaroq variantni yoqtiradi («obuna bo'lishni» < «obuna bo'lib qo'yishni»). 3 whisper rejimi uzun shaklni eshitsa — uzunini ol.
- Whisper so'z vaqtlari ±0.3 s siljiydi («Birinchisi» whisper 5.88, aslida 6.20) — subtitr uchun faqat MMS forced alignment.
- `align.py`: raqamlar `uz_num()` bilan so'zga ("10–15" → "o'n o'n besh"), defis bo'shliq, apostrof saqlanadi (MMS lug'atida `'` bor).
- `torchaudio.functional.forced_align` 2.8 da deprecated ogohlantirish beradi, ishlaydi; 2.9+ da yo'q — `torchaudio<=2.8` yoki `ctc-forced-aligner`.
- Bo'laklarni ma'no bo'yicha QO'LDA (`phrases`) — avtomatik bo'lish «halol | manikyur» ni ajratib yuboradi; `common.chunks()` so'zlarni assert qiladi.
- Subtitr chiqishi oxirgi so'z ichida boshlansa «oldinga qochgan» ko'rinadi → chiqish `t1−0.06` dan, `t1 = min(keyingi−0.03, oxirgi_so'z+0.35)`.

## HyperFrames
- Versiya `hyperframes@0.8.171`; `check` = 0 xato; `snapshot --at a,b,c --no-end --describe false` — bitta chaqiruv.
- Shriftlar lokal `@font-face` (render oflayn), GSAP lokal (`assets/gsap.min.js`). Brauzer shriftni kutmaydi → matn eni Python'da `textw.tw()`.
- `check`: `clipped_text`/`text_box_overflow` — marquee mikromatnni PNG qil. `content_overlap` subtitr almashuvida (info) — normal.
  Kontrast: oq subtitr och ko'k ko'ylakda 2.4:1 → plashkali subtitr. Mono `#5b4a80` qog'ozda 3.47:1 → `#45366a`.
- `overlapping_gsap_tweens`: kirish tugamay chiqish boshlansa — vaqtlarni ajrat.
- Bir nechta `fromTo` bitta elementda → keyingilariga `immediateRender:false` (kamera); takrorlanadigan vaqtli `tl.set` o'rniga `fromTo`.
- Python 3.9 f-string `{}` ichida `\'` mumkin emas → `&#39;`.
- Bodoni Moda katta o'lchamda `opsz` avtomatik = soch chiziqlari yo'qoladi («XI A SIREN») → `font-optical-sizing:none; font-variation-settings:"opsz" 14`, 600.
- Scrim radial bo'lsa hijob tepasini oqartiradi → chiziqli, bosh tepasidan oldin tugaydigan polosa.
- Subtitrga `clip-path` tishli chet — yuqori harflarni kesadi; ishlatma.

## Render
- 16 GB RAM, 4 ta ketma-ket render `-w 2`: A, B ~4 daq; C capture 0.5 fps ga tushdi, «Target closed», ffmpegEncodeTimeout; D video extraction ffmpeg_timeout.
  Yechim: `-w 1` + `PRODUCER_ENABLE_CHUNKED_ENCODE=true FFMPEG_ENCODE_TIMEOUT_MS=5400000`, ketma-ket — hammasi o'tdi (~5–7 daq har biri).
- Render oldidan eski preview/snapshot brauzerlarini to'xtat (RAM). Log faylga yoz (`> render.log 2>&1`), `| tail` exit kodini yashiradi.
- D (grain teksturasi) fayli kattaroq (~215 MB) — telefon nusxasi `-crf 25 -maxrate 3.6M` bilan <30 MB.

## Retush
- opencv 5 da Haar yo'q → YuNet (`assets/models/face_detection_yunet_2023mar.onnx`). Keng kadrda yuz kichik (~180 px) → silliqlash radiusi `w/300` ga masshtab.
- RGB↔YUV aylanishda `in/out_color_matrix=bt709 … accurate_rnd+full_chroma_int+bitexact` + `setparams` — aks holda kadr 2 daraja qorayadi.
- Yuzdan tashqari farq ~1.0 (faqat kodlash shovqini) — tekshiruv shu.

## Tahlil (Instagram)
- IG brauzer panelida logout bo'lishi mumkin: reels tab 36 ta reelni ko'rish soni bilan baribir beradi; `yt-dlp` login'siz ishlaydi,
  DNS uzilib qolsa ketma-ket va qayta urin. Avatar 150 px (imzoli URL).
- Kesim topish: ffmpeg `scene` filtri IG/VP9 da ishonchsiz → `cuts.py` kadr farqi.
