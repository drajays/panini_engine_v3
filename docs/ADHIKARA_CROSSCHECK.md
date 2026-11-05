# Adhikāra spans: our index vs RKMVU `core/architecture.json` (2026-10-31)
Source of theirs: cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site/data/core/architecture.json (73 spans; local copy scratch/rk/arch.json, not committed).
Ours: data/inputs/adhikara_scope_index.json = the ashtadhyayi.db `adhikara` column (identical except the head sūtra itself is listed on itself in the DB). 73 heads each; 71 heads agree.

Verdicts (probe = does the head word occur in `samagra_slp1` of the sūtras in the disputed range):
- 8.1.16 padasya (ours ends 8.3.54), 8.2.82 pluta (8.2.107), 2.3.1 anabhihite (2.3.72): ours right; RKMVU ends one sūtra late (probable off-by-one in their data).
- 4.1.82 samarthānām (ours to 5.4.160, theirs 5.2.140): keep ours (standard Kāśikā extent to end of taddhita).
- 4.4.75 prāg ghitād yat: **FIXED.** Kāśikā: yat governs up to (not incl.) 5.1.5 tasmai hitam; ours stopped at 4.4.144, so 5.1.1–5.1.4 were missing; `EXTEND` in tools/build_scope_index.py adds them. RKMVU's end 5.1.136 is wrong (later yat sūtras in 5.1 name yat themselves). Scheduler does not read this index yet (shadow phase), so no behaviour change.
- FINAL (all from Kāśikā "prāk/yāvat" wording; `EXTEND` in tools/build_scope_index.py): 3.3.141 head added (3.3.142–151, prāk 3.3.152); 5.1.78 kālāt extended to 5.1.97 (yāvat). Ours already right, RKMVU off by one: 6.1.84 (to 6.1.111), 6.1.135 (to 6.1.157), 7.3.10 (to 7.3.31), 6.2.64 (to 6.2.136), 6.2.111 (to pāda end 6.2.199). 4.1.92 is an arthanirdeśa, not an adhikāra (Kāśikā); keep our 4.2.92 śeṣe. 4.1.3 end and the lone 6.2.14 head: Kāśikā gives no end, left as is.
