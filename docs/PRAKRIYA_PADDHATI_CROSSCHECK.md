# Cross-check: Neelesh Bodas, प्रक्रियापद्धति: (5 Dec 2015) and प्रत्ययाधिकार: (8 Dec 2015)

Sources: `~/vyakaran to be done/प्रक्रियापद्धति_.pdf` (15 pp, 9-step order) and `प्रत्ययाधिकार__notes.pdf` (25 pp). Teaching aids, not authority (Art. 23 grade: citation-grade only after the Kāśikā agrees). Every sūtra number below was re-read in the Kāśikā (sqlite `texts`, source=kashika).
Gold data: `tests/fixtures/prakriya_paddhati_gold.json`; test: `tests/regression/test_prakriya_paddhati_gold.py` (18 cases).

## 1. Result
| | count |
|---|---|
| worked examples turned into gold | 18 (rāma+bhis, phala+jas, bhū+laṅ/laṭ/liṅ, paṭh+ktvā/lṛṭ/laṭ/liṅ, as+lṛṭ, kṛ+loṭ, kṛ+ṇvul, rāma+ṅe/ṭā, muni+am, sādhu+su, marut+bhyām, paṭh+laṭ miP) |
| final form attested by the source is among the engine's readings | 18 / 18 |
| order claims (sūtra A before B in the trace) checked | 24 pairs; 20 hold; 4 fail, all in 2 items (pp1.2b, pp6.3; §3) |
| engine bugs found | 1 (fixed) + 1 (not fixed, file locked) |
| source errors found | 7 (§4) |

## 2. Bodas' 9 steps vs the 13-box chart (PLAN §10)
They are the same order; the 13 boxes spell out each "decision + it-lopa" pair that Bodas folds into one step:
Bodas 1 ādeśa+it-lopa = boxes 1–2 · 2 pratyaya-nimittaka āgama+it-lopa = 3–4 · 3 ādeśa (after it-lopa)+it-lopa = 5–6 · 4 ādeśa-nimittaka āgama+it-lopa = 7–8 · 5 āgama-nimittaka kārya = 9 · 6 viśiṣṭa-pratyaya-nirmāṇa = 10 · 7 pratyaya-nimittaka kārya = 11 · 8 sandhi (ac only; hal-sandhi goes to tripāḍī) = 12 · 9 tripāḍī = 13.
**Box 10 is now defined** (it was open in §10): "the pratyaya changes into a new pratyaya after the āgama-kārya — mostly lakāra prakriyā": 3.4.79 ṭita ā… ṭer e, 3.4.90 āmetaḥ, 7.1.3 jho 'ntaḥ, 3.4.103 yāsuṭ + 3.4.107 suṭ, 7.2.79, 7.2.80, 3.4.100, 6.1.66 (his bhavet / paṭhet).
Bodas' own examples break his stage labels: in bhavet he shows guṇa 7.3.84 (stage 7) before yāsuṭ (stage 6). Treat the order as a heuristic; the stage audit (P4a) must expect such interleavings.

## 3. Engine vs source
**Same form, different order (not engine errors; P4a inputs):**
- `pp1.2b` bhū+laṅ: Bodas does aṭ (6.4.71, stage 2) before l → tip (3.4.78, stage 3); the engine does 3.4.78 first, then 6.4.71. Form abhavat unchanged. Open question for the owner: is aṭ's nimitta the lakāra (before ādeśa) or the sthānivat laṅ (after)?
- `pp6.3` bhū+liṅ: engine applies 3.4.100 (itaś ca) before 3.4.103 yāsuṭ and **never applies 3.4.107 suṭ in vidhi-liṅ** (it is armed for āśīrliṅ only: `suw_recipe`/`ashir_liG`); 7.2.79 then removes the one s. Bodas/Kāśikā: yāsuṭ + suṭ, then 7.2.79 removes both, then 3.4.100. Form bhavet is right; the trace has a missing step. Lives in `pipelines/tinanta.py` (left untouched by this pass; the masj change is now committed, 911916b4) and `sutras/adhyaya_3/pada_4/sutra_3_4_107.py`.

**Engine bug, FIXED:** as + lṛṭ (3pl) produced a spurious reading `BUsyaJi` (no iṭ, jhi not turned into anti) next to bhaviṣyanti, with 7.2.44 recorded 189 times in that branch. Cause: 2.4.52 stamps the new bhū `upadesha_slp1 = "BU~"`, and 7.2.44's ūdit test is `"U~" in up`, so bhū looked ūdit and the vibhāṣā toggle re-fired until the loop cap. Fix: `sutras/adhyaya_7/pada_2/sutra_7_2_44.py` `_NOT_UDIT = {"BU~"}`; test `tests/unit/test_7_2_44_bhu_adesha_not_udit.py` (failed before, 379 s; passes after, 11 s — the loop is gone). Same class of bug could hide behind any `"~" in upadesha` test; grep when touching 6.4.88 / 7.4.73 which already special-case BU/BU~.

**Engine bug, NOT fixed (file out of scope for this pass):** `pipelines/tinanta.derive` accepts `"liN"`, `"laN"`, `"luN"` (the tin_upadesha key spellings) without error and derives **laṭ** (`derive("BU","liN","kartari",3,1)` → bhavati). Only the SLP1 names `liG laG luG lRG AsIrliG` dispatch. An unknown name should raise; normalise via `_LAKARA_KEY` and reject the rest.

## 4. Errors in the source (do not copy into the engine)
| source says | Kāśikā says |
|---|---|
| 7.2.25 iḍ-āgama (×3) | 7.2.35 ārdhadhātukasyeḍ valādeḥ (7.2.25 is abhi-… niṣṭhā) |
| 7.2.72 napuṃsakasya jhalacaḥ | 7.1.72 |
| 6.1.146 ogurṇaḥ (guru+aṇ) | 6.4.146 uvarṇāntasya bhasya guṇaḥ taddhite |
| 8.4.52 jhalāṃ jaś jhaśi | 8.4.53 (8.4.52 is dīrghād ācāryāṇām) |
| "प्रावग्वतेष्ठक्" 5.1.18 | prāg vator ṭhañ |
| 36+31+3+27 = 141 arthas | = 97; the 44 prāg-dīvyatīya arthas are omitted from the sum (44+36+31+3+27 = 141) |
| "500+ pratyayas" (पञ्चशताधिकाः) | his own table sums to 487 (12+21+18+124+21+10+281) |

## 5. What प्रत्ययाधिकार: adds (checked against the repo)
- **Twelve sanādi in three groups** (his table, verified against the Kāśikā): dhātu-only — san 3.1.5-7, yaṅ 3.1.22-24, yak 3.1.27, āya 3.1.28, īyaṅ 3.1.29; prātipadika-only — kyac 3.1.8,10,19, kāmyac 3.1.9, kyaṅ 3.1.11,12,14-18, kyaṣ 3.1.13, kvip (vārttika, not a sūtra); both — ṇic 3.1.21,25 (nominal) and 3.1.26 (hetumati, verbal), ṇiṅ 3.1.20 (nominal) and 3.1.30 (kamer ṇiṅ, verbal). PLAN §9 was wrong in giving kyaṣ 3.1.13-15: it is 3.1.13 only (3.1.14-18 are kyaṅ); fixed there.
- **Scope risk for G1:** `adhikara_scope_index.json` puts 3.1.25 (nominal ṇic) under the dhātoḥ head 3.1.22, but its base is a prātipadika; same for ṇiṅ 3.1.20 (not under) vs 3.1.30 (under). A strict `adhikara_in_effect` gate will block or mis-gate the nominal ṇic when G1 is built. Decide per sūtra which head governs before wiring.
- **Vārttika pratyayas** (kvip as 12th sanādi) need a vārttika route; the engine's law is sūtra-only.
- **Vikaraṇa law** "vikaraṇa only after a lakāra is attached; lakāra → tiṅ → vikaraṇa": engine agrees (3.4.78 before 3.1.68 in bhavati, paṭhiṣyanti, paṭhanti).
- **kṛt four-way split** (kṛtya 3.1.95–132 / pūrvakṛt 3.1.133–3.2.188 / uṇādi at 3.3.1 / uttarakṛt 3.3.2–3.4.76) is the Kaumudī's, not Pāṇini's; use it as a coverage index, not as a gate. Engine data: `krit_pratyaya.json` 54 entries vs his 124 → counts of what is not yet derivable.
- **Taddhita blocks**: five arthādhikāras (prāg-dīvyatīya aṇ 4.1.83–4.3.168, prāg-vahatīya ṭhak 4.4.1–74, prāg-ghitīya yat 4.4.75–144, prāk-krītīya cha 5.1.1–36, prāg-vatīya ṭhañ 5.1.18–115) + the mahotsarga/apavāda pairs per artha; the scope index matches his heads; `taddhita_pratyaya.json` has 4 entries vs his 281.
- **Sautra root found:** 3.1.29 ṛti (īyaṅ) is a sautra dhātu beside stambh/stumbh/skambh/skumbh (3.1.82); add to G3.

## 6. Fix list / owner decisions
1. (done) 7.2.44 bhū not ūdit.
2. `pipelines/tinanta.derive`: reject unknown lakāra names (liN/laN/luN fall back to laṭ). Now unblocked (masj committed).
3. 3.4.107 suṭ in vidhi-liṅ (and order 3.4.100 vs 3.4.103) — decide trace fidelity vs recipe shortcut; ledger entry if it stays.
4. Aṭ before or after tiṅ ādeśa (box 3 vs box 5 reading) — card C-L2-3.
5. G1 scope heads for nominal ṇic/ṇiṅ.
6. P4a stage audit takes the 5 ordering claims in §7.

## 7. Ordering claims for P4a (from the notes)
1. aṭ/āṅ-type āgamas of a lakāra precede its ādeśa (st 2 < st 3) — engine diverges (pp1.2b).
2. ādeśa before it-lopa only if the sūtra applies to the pratyaya in its upadeśa shape (st 1: bhis → ais, jas → śi); an ādeśa that needs the it-less shape waits for st 3 (ṇvul → vu → aka 7.1.1; ḍha → eya 7.1.2).
3. vikaraṇa after tiṅ ādeśa; guṇa/vṛddhi (st 7) after all āgamas and nirmāṇa (st 4–6) — engine holds (pp4.1, pp5.3, pp7.1).
4. ac-sandhi (6.1.77 ff., 6.1.87, 6.1.107) after st 7; hal-sandhi only in tripāḍī — engine holds (pp8.2, pp8.3, pp9.x).
5. tripāḍī strictly in sūtra order, same-stage rule (earlier operates) — engine holds (pp9.1 8.4.2, pp9.2 8.2.66 < 8.3.15).
