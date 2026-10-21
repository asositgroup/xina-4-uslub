# Namuna: «Tirnoq tishlash odatini tashlash — 3 layfxak» (@xina_siren, 2026-10-18…20)

Manba: 1792337215369777.mp4 (59.2 s, 2144×3840 60 fps, qizil hijobli mutaxassis manikyur qilib gapiradi; 7 kadr, kesimlar
6.133 / 14.867 / 32.467 / 44.40 / 49.80 / 55.133). Asl ovoz −36.6 LUFS salon shovqini bilan → Auphonic speech_isolation → −15.5 LUFS.

| Fayl | Nima |
|---|---|
| `project.json` | kadrlar (origin, zoom, subtitr y), 44 subtitr bo'lagi, aksentlar, davomiylik, media yo'llari |
| `SSENARIY.md` | kadrlar jadvali (yuz zonalari), adabiy matn, bo'g'inlar va piktogrammalar |
| `audio/segments_final.json` | mutaxassisning aynan so'zlari (11 gap, vaqt oynalari) |
| `audio/words_final.json` | 110 so'z — MMS forced alignment vaqtlari (start/end/score) |
| `audio/tr_*.json` | whisper uz (asl va toza), kk, tr transkriptlari — solishtirish uchun |
| `analysis/` | 1 fps kontakt varaq, yuz/zona to'ri |
| `previews/` | v2 snapshot varaqlari (A–D), o'tish oynalarining QC qatorlari, retush oldin/keyin zoom |
| `OUT_README.md` | topshirilgan v2 fayllar tavsifi |

Katta media repoda YO'Q (mijoz videosi): `src/manba.mp4`, `assets/base_retush.mp4`, `audio/manba_auphonic.wav`, `assets/avatar.jpg`.
Tayyor videolar telefon nusxalari — GitHub Releases «v2-namuna». Qayta yig'ish: media'ni shu papkaga qo'ying (project.json → media) va
`python scripts/build.py --project example/xina-tirnoq A B C D`. Skill orqali yig'ilgan HTML asl v2 bilan baytma-bayt bir xil ekani tekshirilgan.
