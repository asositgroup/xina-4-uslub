# Foydalanuvchi qoidalari (hammasi — har montajda amal qiladi)

Manba: foydalanuvchining to'g'ridan-to'g'ri tuzatishlari (2026-10-05 … 2026-10-21). Ustuvorlik: foydalanuvchi qoidasi > uslub > referens.

## Ovoz
1. **Auphonic avval** (2026-10-18): «video tashlasam auphonic.com orqali orqa shum tovushini olib keyin montaj qilishing kerak».
   `scripts/auphonic_clean.sh` — faqat audio (FLAC) yuklanadi, video emas; natija WAV asl videoga `-c:v copy` bilan ulanadi.
   Standart: `speech_isolation`, to'liq (0), dereverb to'liq, leveler, −16 LUFS, maxpeak −1. Musiqa saqlanishi kerak bo'lsa `--method dynamic`.
   Bepul tarif jingli (~6.4 s, «…Free Audio Post-Production») BOSHIGA yoki OXIRIGA qo'shiladi — `auphonic_align.py` o'zi topib kesadi va sinxronni tekshiradi.
2. **Musiqa so'ramasdan qo'shilmaydi.** Qo'shilsa: sokin, zarbsiz, nutqni to'smaydi (nutq polosasida ≥19 dB median / ≥14 dB eng yomon);
   bu foydalanuvchi pompalanuvchi ducking'ni yoqtirmaydi — doimiy past bed.
3. **SFX**: faqat yumshoq whoosh/click. «Trling» sparkle/chime/sehrli qo'ng'iroq HECH QACHON.
4. Yakuniy ovoz −14 LUFS, TP −1.5, 2-pass lineal loudnorm (`finish.sh`).

## Subtitr (2026-10-20)
5. «subtitr textini mavzudan experttan kelib chiqqan holda o'zgartir va subtitr orqada qolmasin»:
   - matn = mutaxassisning AYNAN aytgani (adabiy imlo), qisqartirilmaydi, o'z so'zlarimiz bilan almashtirilmaydi;
   - shubhali joy: uz/kk/tr whisper + `align.py score` variantlar; hal bo'lmasa foydalanuvchiga ❓ bilan aytiladi;
   - vaqt: MMS forced alignment, bo'lak birinchi so'zida chiqadi (−0.05 s), oxirgi so'zi tugaguncha turadi, keyingisi bilan almashadi;
   - subtitr hamma qatlam USTIDA (o'tishlar ham yopmaydi);
   - kartalar/sarlavhalar matni ham uning so'zlari («minut», «bir kunda»), raqamlar u aytgan paytda chiqadi.
6. O'zbek lotin imlosi tekshiriladi (oʻ/gʻ → `o'`/`g'`, yangi gap bosh harf), oxirgi nuqta subtitrda qo'yilmaydi.

## Tasvir
7. **Hamma narsa silliq** (2026-10-05): kirish `expo.out` + blur→0 (subtitr 0.38 s, karta 0.7–0.9 s), chiqish `power2.inOut` ≥0.26 s;
   `back.out` / `elastic` / `bounce` / qisqa `yoyo` YO'Q; layout xossalari (top, height, letterSpacing) tween qilinmaydi; `filter` tween faqat `fromTo` bilan.
   Kamera «nafas» kadr bo'yicha `sine.inOut`, kesimda miqyos sakramaydi. Render fps = 60.
8. **Yuz/bosh ochiq**: hech bir yozuv/karta yuzga tushmaydi (B-roll'dagi yuzga ham); scrim/band/panel bosh tepasidan oldin tugaydi;
   qo'ldagi mahsulot/ish (manikyur) to'silmaydi; o'tish (sweep/ipak/yirtiq) faqat bir lahza yuzdan o'tishi mumkin.
9. **IG xavfsiz zona**: hech narsa y>1450 da emas; 1000–1700 polosada x>930 da emas; subtitr ≈1170–1420 (kadrga qarab).
10. **Retush** (2026-10-20): «yuzni retush qil lekin videoning kachestvasiga ta'sir qilmasin» — asl 4K'dan bir marta kodlash (CRF 13),
    YuNet + teri niqobi + bilateral (yuz o'lchamiga mos radius), kuch 0.65; qosh/kiprik/ko'z/lab keskin; zoom bilan oldin/keyin tekshir.
11. **Ovozsiz tushunarli** (2026-10-15): har g'oya piktogramma, sabab→natija, raqam bilan; ortiqcha so'z qo'shilmaydi.
12. **Premium, bachkana emas**: emoji yo'q, multfilm effekti yo'q, kamtarona (diniy auditoriya — hijob, ochiq kiyim yo'q).
13. **Referensdan faqat texnika**: boshqa muallifning kadr/metaforasi ko'chirilmaydi (o'g'irlik deb qabul qilinadi).

## Ish tartibi
14. Uzun ishda qisqa holat xabarlari; "tayyor" deyishdan oldin render va fon jarayonlari haqiqatda tekshiriladi (check, smooth_check, kadrlar).
15. Eski versiya o'chirilmaydi: `out/v1/`, yangisi `_v2` nomi bilan; telefon nusxasi <30 MB.
16. Mijozdan tasdiqlanmagan ma'lumot (telefon, narx) yakunda ishlatilsa — foydalanuvchiga aytiladi.
