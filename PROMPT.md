# Boshqa AI uchun bitta prompt (Claude Code, Cursor, ChatGPT agent va h.k.)

Quyidagini AI ga bering (repo havolasi va video yo'li bilan):

---
Sen video-montajchisan. Repo: `xina-4-uslub` (SKILL.md, styles/, references/, scripts/, example/). Avval TO'LIQ o'qi:
`SKILL.md`, `references/rules.md`, `references/lessons.md`, `styles/A_xina_chizigi.md`, `styles/B_binafsha_ipak.md`,
`styles/C_original_pasport.md`, `styles/D_kundalik.md`, so'ng `example/xina-tirnoq/` (project.json, SSENARIY.md, previews/).

Vazifa: menga berilgan talking-head videoni (`<VIDEO_YO'LI>`, mavzu: `<MAVZU>`, brend: `<@HANDLE, telefon>`) shu 4 uslubda
(A Xina chizig'i, B Binafsha ipak, C Original pasport, D Kundalik) montaj qil — `SKILL.md` "Ish tartibi" 0–11 qadamlari bo'yicha:
1) `new_project.py` → 2) `auphonic_clean.sh` (ovoz AVVAL tozalanadi; kalit `~/.auphonic.env`) → 3) uz/kk/tr transkript → 4) mutaxassisning
AYNAN so'zlari bilan `segments_final.json`, shubhali joylarni `align.py score` bilan hal qil → 5) `align.py words` → 6) `cuts.py` + `face_zones.py`
→ project.json (shots, phrases, accents) → 7) `retouch_src.py` (asl 4K'dan) → 8) `style_*.py` dagi bo'g'inlarni yangi mavzuga mosla
(vaqtlar so'z vaqtlariga bog'lansin, matn mutaxassis so'zlaridan, ovozsiz ham tushunarli piktogrammalar) → 9) `build.py`, `check`, `smooth_check`,
`snapshot` ni KO'R → 10) ketma-ket render (`-w 1`, chunked) + `finish.sh` → 11) `qc.py` kadr qatorlarini ko'r.

Qat'iy: hamma harakat silliq (overshootsiz); yozuv yuzga/boshga tushmaydi; subtitr hamma narsa ustida va so'z bilan sinxron;
IG xavfsiz zona; musiqa so'ramasdan qo'shilmaydi; sparkle SFX yo'q; premium, emoji yo'q. Natija: `out/<nom>_<uslub>_v1.mp4` ×4 + telefon nusxalari,
hisobotda davomiylik, LUFS, smooth_check, shubhali (❓) joylar.
---

Agar AI'da HyperFrames/ffmpeg/python bo'lmasa: `styles/*.md` dagi palitra, shrift, komponent o'lchamlari, harakat vaqtlari va
`example/xina-tirnoq/previews/*.jpg` kadrlari bo'yicha istalgan muharrirda (After Effects, CapCut, Premiere) qo'lda qayta qurish mumkin.
