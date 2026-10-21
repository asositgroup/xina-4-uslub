---
name: xina-4-uslub
description: Talking-head (ekspert/go'zallik/xina-manikyur) reelni 4 xil premium uslubda montaj qiladigan to'liq skill — A «Xina chizig'i» (xina konusidan chizilgan naqsh va yozuv, pasta→dog' rangi), B «Binafsha ipak» (jurnal muqovasi, muzli shisha, lavanda ipak o'tishi), C «Original pasport» (gilosh hujjat, golografik HALOL muhri, UV-skaner, sertifikat), D «Kundalik» (qog'oz qaydlar, skotch, chek-list, yirtiq qog'oz). Quvur — Auphonic shovqin tozalash (jingl joyini o'zi topadi) → uz/kk/tr whisper + MMS forced alignment bilan mutaxassisning AYNAN so'zlari va so'zma-so'z vaqtli subtitr → asl 4K'dan sifat yo'qotmasdan yuz retushi → kesim va yuz zonalari → HyperFrames 4 kompozitsiya (GSAP, overshootsiz silliq) → 60 fps render → −14 LUFS + telefon nusxasi. "/xina-4-uslub", "4 uslubda montaj qil", "xina uslublarida", "Xina Siren uslubida", "A B C D uslublarda", "xina chizig'i / binafsha ipak / original pasport / kundalik uslubida" so'rovlarida, shuningdek go'zallik saloni / xina / manikyur ekspert videosini shu 4 uslubda qilish kerak bo'lsa ishlat.
---

# xina-4-uslub — bitta talking-head video → 4 ta premium uslub

Ish tili: **o'zbekcha**. Natija: bitta manba videodan 4 ta 9:16 reel (1080×1920, 60 fps, −14 LUFS), har biri o'z dizayn tilida,
bir xil aniq subtitr va bir xil tozalangan ovoz bilan. Birinchi marta @xina_siren (Toshkent, halol xina studiyasi) uchun
«Tirnoq tishlash odatini tashlash — 3 layfxak» videosida qurilgan; to'liq namuna `example/xina-tirnoq/`.

| Uslub | G'oya | Imzo o'tishi | Hujjat |
|---|---|---|---|
| **A · Xina chizig'i** | hamma grafika xina konusidan siqilgandek jonli chiziladi; chiziq yangi pasta (#7D6A2E) → dog' (#2A150C) rangiga «qurib» o'tadi | qalin xina chizig'i ekranni diagonal kesib o'tadi | `styles/A_xina_chizigi.md` |
| **B · Binafsha ipak** | lyuks jurnal: Bodoni + Jost, olxo'ri tus, muzli shisha kartalar, marvarid | lavanda ipak to'liq ekranni yopib o'tadi | `styles/B_binafsha_ipak.md` |
| **C · Original pasport** | himoyalangan hujjat: gilosh, seriya №, mikromatn, golografik «HALOL» muhri, «YOPILDI» sertifikat | UV-skaner nuri tepadan pastga | `styles/C_original_pasport.md` |
| **D · Kundalik** | qog'oz qaydlar, lavanda skotch, chek-list belgilanadi, polaroid, qizil muhr | qog'oz yirtilib almashadi | `styles/D_kundalik.md` |

Namunaviy natija kadrlari: `example/xina-tirnoq/previews/` (har uslubning snapshot va QC kadr qatorlari),
dizayn taxtasi (4 yo'nalishning jonli taqdimoti): `references/design-board/index.html`.

## Qat'iy qoidalar (foydalanuvchi o'rnatgan — `references/rules.md` to'liq)
1. **Avval Auphonic** — har yuborilgan video ovozi montajdan OLDIN auphonic.com API orqali tozalanadi (`scripts/auphonic_clean.sh`).
2. **Subtitr = mutaxassisning AYNAN so'zlari** (adabiy imlo, uning fe'l shakllari, qisqartirilmaydi, "kuniga…daqiqa" emas — u "bir kunda…minut" desa shunday).
   Har so'z vaqti MMS forced alignment bilan; bo'lak o'z birinchi so'zida chiqadi, oxirgi so'zi tugaguncha turadi. **Subtitr hamma narsa ustida**
   (z-index 70 — o'tishlar, ipak, UV, yirtiq qog'oz ham uni yopmaydi). Kartalardagi matn ham uning so'zlari bilan.
3. **Hamma narsa silliq** — kirish ≥0.38–0.9 s `expo.out`+blur, chiqish ≥0.26–0.55 s `power2.inOut`; overshoot/elastic/bounce YO'Q;
   `smooth_check.py` kod va video = 0 (asoslangan istisnolar: doimiy aylanish/marquee `ease:none`, 0.01 s konteyner yoqilishi).
4. **Yuz va bosh ochiq** — hech bir yozuv yuzga tushmaydi; tepadagi scrim/band/panel bosh tepasidan oldin tugaydi (kadrga qarab 330–690 px).
   IG xavfsiz zona: hech narsa y>1450 da emas, 1000–1700 polosada x>930 da emas.
5. **Retush sifatni buzmasin** — asl 4K'dan bir marta (CRF 13), faqat teri silliqlanadi, qosh/kiprik/lab keskin qoladi.
6. **Ovozsiz ham tushunarli** — har maslahat piktogramma/sabab→natija bilan (`feedback`: yopiq doira, kosa+soat, Ca/Zn, tirnoq chizmasi).
7. **Musiqa so'ramasdan qo'shilmaydi**; SFX faqat yumshoq whoosh/click — «trling» sparkle/chime HECH QACHON. Premium, bachkana emas, emoji yo'q.
8. Eski versiyani o'chirmaslik — `out/v1/` ga ko'chirish, yangisi `_v2`.

## Talablar
- macOS/Linux, `ffmpeg` ≥5.1, `node` + `npx hyperframes@0.8.171` (birinchi ishga tushishda o'zi o'rnatadi; Chrome headless shell bilan render).
- Python 3.9+ venv: `numpy scipy pillow opencv-python(-headless) faster-whisper torch torchaudio` (torchaudio ≤2.8 — `forced_align` bor).
  Shu Mac'da: `~/Desktop/AI-Videos/.venv/bin/python`. Boshqa joyda `XS_PY=/path/to/python` bering.
- Auphonic API kaliti: `~/.auphonic.env` → `AUPHONIC_API_KEY=...` (auphonic.com → Account Settings → API Key). Bepul tarif 2 soat/oy, har production ≥~3 daq hisoblanadi.
- MMS_FA modeli birinchi chaqiruvda yuklanadi (~1.2 GB, torchaudio pipelines). YuNet modeli `assets/models/` da bor.

## Ish tartibi (har qadamda natijani KO'Z bilan tekshir)
```bash
SK=~/.claude/skills/xina-4-uslub/scripts ; PY=~/Desktop/AI-Videos/.venv/bin/python ; PRJ=~/Desktop/AI-Videos/<Mijoz>/<NN_nom>
# 0. Loyiha: src/manba.mp4 (klon), assets/base.mp4 (1080x1920 60fps), project.json shabloni
$PY $SK/new_project.py /yo'l/video.mp4 $PRJ 01_Mavzu
# 1. Shovqinni tozalash (Auphonic) -> audio/manba_auphonic.wav (jingl boshida/oxirida bo'lsa o'zi kesadi, sinxron tekshiradi)
$SK/auphonic_clean.sh $PRJ/src/manba.mp4 $PRJ/audio
# 2. Transkript (3 rejim — shubhali joylarni uchburchak qilib aniqlash uchun)
ffmpeg -i $PRJ/audio/manba_auphonic.wav -ac 1 -ar 16000 $PRJ/audio/clean16k.wav
for L in uz kk tr; do HF_DEV=cpu HF_CT=int8 $PY $SK/tr.py $PRJ/audio/clean16k.wav $PRJ/audio/tr_$L.json $L; done
# 3. Adabiy matnni yoz: audio/segments_final.json [{t0,t1,text}] — mutaxassis AYNAN aytgani; shubhali joylar uchun variantlarni ball bilan solishtir:
$PY $SK/align.py score $PRJ/audio/clean16k.wav <t0> <t1> "variant 1" "variant 2" ...   # past ball = ovozga mosroq (MMS qisqasini yoqtiradi — 3 whisper kelishsa uzunini ol)
# 4. So'z vaqtlari (forced alignment)
$PY $SK/align.py words $PRJ/audio/clean16k.wav $PRJ/audio/segments_final.json $PRJ/audio/words_final.json
# 5. Kesimlar va yuz zonalari -> project.json "shots" (origin %, scale0/1, sub_y)
$PY $SK/cuts.py $PRJ/src/manba.mp4
$PY $SK/face_zones.py $PRJ/assets/base.mp4 $PRJ/project.json $PRJ/tahlil/zones.jpg    # varaqni KO'R
# 6. Yuz retushi (asl 4K -> 1080x1920, bir marta kodlash) -> assets/base_retush.mp4 ; avatar.jpg ni ham qo'y (IG avatar)
$PY -I $SK/retouch_src.py $PRJ/src/manba.mp4 $PRJ/assets/base_retush.mp4 0.65
# 7. project.json: "phrases" (ma'no bo'yicha 1–4 so'zli bo'laklar, words_final bilan aynan mos — common.chunks() tekshiradi), "accents"
# 8. Uslub fayllaridagi bo'g'inlarni (vaqt + matn + piktogramma) yangi mavzuga moslash — pastdagi "Yangi videoga moslash"
# 9. Yig'ish + tekshiruv
$PY $SK/build.py --project $PRJ A B C D
for L in A B C D; do (cd $PRJ/hf_$L && npx --yes hyperframes@0.8.171 check); $PY $SK/smooth_check.py $PRJ/hf_$L/index.html; done
(cd $PRJ/hf_A && npx --yes hyperframes@0.8.171 snapshot --at 1.6,8.2,27,43.6,53.9 --no-end --describe false)   # contact-sheet ni KO'R
# 10. Render (ketma-ket! 16 GB RAMda -w 1 + chunked encode) va yakunlash
for L in A B C D; do (cd $PRJ/hf_$L && PRODUCER_ENABLE_CHUNKED_ENCODE=true FFMPEG_ENCODE_TIMEOUT_MS=5400000 \
  npx --yes hyperframes@0.8.171 render -o renders/${L}_raw.mp4 -q delivery -w 1 -f 60 > renders/render.log 2>&1) && $SK/finish.sh $L $PRJ; done
# 11. QC: silliqlik (video) + o'tish oynalari kadrma-kadr
$PY $SK/smooth_check.py $PRJ/out/<fayl>.mp4 ; $PY $SK/qc.py $PRJ/out/<fayl>.mp4 A 1.3:sync 6.0:otish 53.6:cta   # tahlil/qc/*_strips.jpg ni KO'R
```

## project.json (videoga xos hamma narsa shu yerda)
```json
{ "name": "01_Tirnoq_tishlash", "dur_video": 59.216, "dur": 60.6,
  "media": {"base": "assets/base_retush.mp4", "voice": "audio/manba_auphonic.wav", "avatar": "assets/avatar.jpg"},
  "shots": [{"t0":0.0,"t1":6.133,"origin":"40% 34%","scale0":1.0,"scale1":1.04,"sub_y":1290}, ...],
  "phrases": ["Tirnoq tishlash odatimni", "17 yoshimda tashlaganman,", ...],
  "accents": ["17 yoshimda", "halol manikyur", "10–15 minut", ...],
  "words": "audio/words_final.json", "subs_end": 58.85,
  "output_names": {"A":"A_Xina_chizigi","B":"B_Binafsha_ipak","C":"C_Original_pasport","D":"D_Kundalik"}, "version": "v2" }
```
- `shots`: kamera «nafas» zoomi kadr bo'yicha (sine.inOut), navbat bilan 1.0↔1.04–1.12 — kesimda miqyos sakramaydi; `origin` = yuz markazi.
- `sub_y`: subtitr markazi (iyakdan ≥100 px pastda, qo'llar/mahsulotni to'smasin, ≤1450).
- `dur` = `dur_video` + ~1.4 s yakuniy karta. `subs_end` — oxirgi subtitr yakuniy karta paydo bo'lishidan oldin tugaydi.

## Yangi videoga moslash (uslub fayllari)
`scripts/style_{a,b,c,d}.py` dagi `build()` — namunaviy **bo'g'inlar ketma-ketligi** (hook → 1-bo'lim → sabab → 2-bo'lim → kosa/soat → Ca/Zn →
3-bo'lim → tirnoq chizmasi → chiplar → CTA obuna → yuboring → yakun). Uslubning **komponentlari** (scrim/band/doc/card, section(), ring(), vine(),
seal(), checkbox(), sweep/silk/UV/tear, subtitr, yakun kartasi) qayta ishlatiladi; yangi mavzuda:
1. Har bo'g'in vaqtini `words_final.json` dagi tegishli so'z boshlanishiga bog'la (masalan bo'lim «Birinchisi» so'zida, karta raqami raqam aytilganda).
2. Matnni mutaxassis so'zlaridan ol; piktogrammalar `common.ICONS` (nail, nail_bitten, nail_crack, check, shield, bowl, clock, cone, eye_off,
   arrow_up, plane, user, loop) — yangisi kerak bo'lsa 120×120 viewBox chiziqli SVG qo'sh.
3. Joylashuv: elementlar kadrning bo'sh zonasida (face_zones natijasi); scrim/band balandligi = shu kadr tepa bo'sh zonasi.
4. Matn enini `textw.tw(font, px, matn)` bilan o'lcha (brauzer shriftni kutmaydi) — ikonka/muhr bilan to'qnashmasin.
5. O'tishlar ro'yxati (`SWEEPS`/`SILKS`/`UV`/`TEAR`) — haqiqiy kesimlarga (va bo'lim boshiga) mos; ular SFX ham beradi.
6. Yakuniy karta matni: brend nomi, handle, telefon (mijoz tasdiqlagani).
`build.py` dan keyin `check` + `snapshot` — xato/ustma-ust tushish, yuzga tushish, kontrastni tuzat.

## Fayllar
```
SKILL.md · README.md · PROMPT.md (boshqa AI uchun bitta prompt) · LICENSES.md
scripts/   common.py (konfig, chunks, ikonka, NAIL_DIAGRAM, HTML skelet, GSAP yordamchilar, kamera) · style_a..d.py · build.py · finish.sh
           textw.py · align.py (MMS score/words, uz_num) · auphonic_clean.sh · auphonic_align.py · retouch_src.py · cuts.py · face_zones.py
           new_project.py · make_textures.py · qc.py · smooth_check.py · tr.py (faster-whisper) · sheets.sh (1 fps kontakt varaq)
assets/    fonts/ (14 OFL shrift) · gsap.min.js · textures/{guil,micro,grain}.png · sfx/{sweep_small,air_woosh,select_click}.wav · models/yunet.onnx
styles/    A_xina_chizigi.md · B_binafsha_ipak.md · C_original_pasport.md · D_kundalik.md  (palitra, shrift, har komponent, harakat, vaqtlar)
references/ rules.md · lessons.md · brand_xina_siren_tahlil.md · design-board/ (4 yo'nalish jonli taxta + media)
example/xina-tirnoq/  project.json · SSENARIY.md · audio/ (segments_final, words_final, tr uz/kk/tr) · analysis/ · previews/ · OUT_README.md
```
