# Open failures (recorded 2026-11-09 for later correction)

Source: `tools/exercise_audit` after commits 996b98b4 … 43376140. Method: audit one sūtra with `.venv/bin/python scratch/aud.py <id>`, read the Kāśikā in the DB (texts, source=kashika), cite it, fix.

| Sūtra | State | Cause found | What is needed |
|---|---|---|---|
| 8.3.56 | FAIL | the stem `turAsAh` cannot be derived from its parts | ṇvi (3.2.62/63), 7.2.116 upadhā vṛddhi, 6.1.67 v-lopa, 6.3.137 dīrgha of tura → turā (Kāśikā 3.2.63) |
| 8.3.111 | DONE for the dhātu-initial ādeśa s (commit below); sāt half open | S147 | 5.4.52 as a real taddhita |
| 8.3.14 | DONE (real rule; kzantrf matches the DB derivation) | — | two-word and yaṅluk examples (punar ramate, apAspAH) need vākya / yaṅluk input |
| 8.3.22 | FAIL | `mAsAByAm` for expected `mAByAm`, plus doubled variants; the example may not belong to 8.3.22 at all (Kāśikā: bho/bhago/agho y-lopa) | read the DB derivation before touching |
| 8.3.28 | works (test pins it) | the audit cannot score it: examples are two-word (prāṅ ṣaṣṭhaḥ) | vākya input in the harness |
| 8.4.12 | FAIL | engine makes vṛtrahaṇau through 8.4.2 over a flat stem | samāsa segmentation (S126): vṛtra + han (3.2.87 kvip, 2.2.19) |
| 8.4.63 | FAIL | audit stem wrong (`pratyakSreRI`) and doubled variants | harness stem + vākya |
| 8.4.64, 8.4.65 | FAIL | need the doubled clusters (8.4.46/47) and examples the harness cannot build (cucyyate, kzuRatti …) | read each DB label; kṛdanta/sanādi entry points |
| 7.4 | open | san entry point (pipaviṣate …); svāpi branch of 7.4.67 | generic san/ṇic-san path |
| 8.4.47 | partly open | śar/khay and avasāne vārttika branches still make kzzantA, prANNkzzu (attested in the Kāśikā but they fire in isolated words) | decide whether isolated words may take them |
| lint | stale | sig/suite_sig.json does not know the new PRATISHEDHA sūtras (8.4.37/39/44, 8.3.111): they set `blocks_sutra_ids=()` on purpose | refresh with tools.test_impact record |
| tests | known | test_kirati_karati_split_prakriyas::test_P009 fails (1.3.3 order) since before this work | — |

## 2026-11-10 triage of the audit's "right form, sūtra did not fire" rows
| Sūtra | Finding |
|---|---|
| 7.1.79 | dadanti is made by 7.1.70 (nuṃ) in the kṛdanta/subanta route although 7.1.78 (nābhyastācchatuḥ) should bar it (the strī route does bar it: juhvatī). Fix: make 7.1.78 win over 7.1.70 in the subanta scanner (a trace showed 7.1.70 APPLIED before 7.1.78), then 7.1.79 as a VIBHASHA that inserts nuṃ (7.1.72 must skip abhyasta Śatṛ stems). An attempt was reverted: just listing 7.1.78 before 7.1.70 in pipelines/subanta.py did not reorder them. |
| 4.1.41 | engine rule is real (tests/regression/test_taddhita_basics.py via chain.strI); derive(stem, strīliṅga) goes ṭāp-only (gOrA), the audit cannot start from the base stem. Harness/route gap, not a missing rule. |
| 1.1.34 | tag-driven niyama; the audit passes no vivakṣā (saṃjñā/vyavasthā). |
| 8.2.2 | siddha-statement, not a firing rule. |
| 3.1.31, 3.4.109, 8.2.75 | not yet triaged (3.4.109 jus after abhyasta/vid; 8.2.75 dat-final dhātu + sip → ru/d). |

## 2026-11-10 (late) — añc stems: the user's Kāśikā text settles the nasal (6.4.138 / 6.4.139 / 6.3.138)
Source: the user's pasted Kāśikā + Bhāṣya-vṛtti text. anc + kvin: kvin is kit, so 6.4.24 drops the nasal *at the stem stage* (anc → ac); the stem is the
unfused tape [upasarga][ac] (pra + ac, prati + ac, ud + ac). In a bha (yac-bhaṃ 1.4.18) 6.4.138 deletes the a of ac, 6.4.139 turns it into ī after ud, and
6.3.138 lengthens the preceding aṇ before the bare c (pratīcā, prācaḥ: pra + c → prā + c). Strong cases get the nasal back from 7.1.70 (añcu is ugit).
Not built: the subanta pipeline takes a stem string, so [pra][ac] must stay two Terms to the sup (no 6.1.101 fusion before the pada). Next: let a lexicon
entry hand the subanta scanner a Term list; then 6.4.24 at kvin (the term-0 limit of that rule must go), origin_it:u for ugit.
7.1.79 (dadanti/dadati) is real now (7.1.78 bars 7.1.70 and 7.1.72; 7.1.79 VIBHASHA); the audit row stays FAIL only because the audit passes the bare stem
"dadat" with no vyutpatti record — it needs a krdanta entry point.

- **8.2.76 (rvor upadhā dīrgha):** real for a dhātu's own r/v (gīḥ, gīrbhyām). Open: (a) a dhātu's s→ru (pipaṭhīḥ, sajūḥ) — the s's origin is lost at pada-merge, so ru is excluded; (b) gīrṣu — 1.4.18 tags the stem bha before `su` because `s` is in `_YACI_HAL` (pre-existing); (c) the scanner opens an adhikāra before contending rules (fixed 2026-11-12) but 6.4.1's late opening was the reason 6.4.127 never fired.

## From the अ-इ-उकारान्त PDF gold (2026-11-14; `tests/regression/test_paddhati_subanta_ai_u.py`, detail `docs/AI_U_SUBANTA_GOLD.md`)
28 strict xfails, none a wrong final form except the two vocatives. Each flips to a failure the day it is fixed.

- **6.1.103 fuses 6.1.102** (rAma/muni/sADu 2-3): the act deletes the stem vowel and writes the long vowel + n itself; the PDF (and the Kāśikā order) has 6.1.102 first, then s→n. Needs 6.1.102's Sas branch for masculine ik-finals + 6.1.103 reduced to s→n.
- **6.1.90 not seen for the sup's āṭ** (mati/Denu/nadI/vaDU 4-1, 5-1, 6-1): 7.3.112 inserts A inside the affix; 6.1.90 reads a separate `aTa_agama` Term. 6.1.88 gives the same ai. Fix = make 7.3.112's āṭ its own Term (as the verbal āṭ is).
- **ā-stem ṅit-sups (S2)** (mAlA 3-1, 5-1, 6-1, 7-1): ṭāp stays a separate Term; 7.3.105/113/116 + 6.1.101 not walked (7.1.12 fires on the pre-ṭāp aṅga).
- **neuter ik-stem sambuddhi** (vAri, maDu 8-1): only `vAre`/`maDo`; missing `vAri`/`maDu` (7.1.23 luk, 1.1.63 blocks guṇa) — PDF note [52]: guṇa is the pakṣa via the anityatva of 1.1.63. Wrong-form class: the primary reading is absent.
- **7.1.24 identity am→am** (Pala 2-1, 8-1): SKIPPED; the PDF uses it to bar 7.1.23.
- **6.4.3 nāmi** (rAma/Pala 6-3: 7.3.102 lengthens first, same form; mAlA/nadI/vaDU 6-3: already long, vacuous).

## LK case gate, adhyāya 1 + 2 (2026-11-14; tools/lk_cases, fixtures tests/fixtures/lk_cases/a1,a2)
| Sūtra | State | Cause found | What is needed |
|---|---|---|---|
| 1.3.14 / 1.3.15 | FAIL | derive() never reads the karmavyatihāra vivakṣā (arthaViSeSa=karmavyatihAra): 1.3.14 reads a tag `karmavyatihAra_usage` that nothing sets, 1.3.15 never runs: `vyatilunAti` for expected `vyatilunate` | rewrite 1.3.14 on `vivaksita`, wire 1.3.14/15 into the bootstrap pada list; 1.3.15 needs gatyartha/hiṃsārtha root classes |
| 1.3.32 45 53 54 55 | UNRUNNABLE | no sense / sakarmaka / tṛtīyā-yoga vivakṣā keys; 1.3.45 jñā gives jānāti (not wired) | add keys (AMENDMENT 25 schema) + rewrite as pada-by-sense sūtras like 1.3.66 |
| 1.3.62 / 1.3.74 | UNRUNNABLE | `san_recipe` gives `eeDizate` (should be edidhiṣate), `nic_recipe` on kṛ gives `kfayate` (should be kārayate) | the sanādi recipes are broken for these roots (V4_CYCLE: sanādi laṭ only, recipe) |
| 1.3.91 / 1.3.92 | UNRUNNABLE | luṅ of dyut lacks the ātmanepada reading adyotiṣṭa; lṛṭ of vṛt gives vartiṣyati (iṭ) — parasmaipada must be aniṭ vartsyati (7.2.59) | 1.3.91/92 optional reading + 7.2.59 |
| 1.3.82 | note | ā+mṛṣ gives āmṛṣyati; Kāśikā āmṛṣyate (DP mṛṣa~ is labelled ubhayapadī, divādi) | check the DP label / 1.3.12 svaritet for mṛṣ |
| 1.1.59, 1.4.8, 2.4.62 | FAIL | the sūtra is never recorded in the trace for cakratuḥ/dadatuḥ/petatuḥ, bhūpataye, aṅgāḥ (forms right: another path makes them); 1.4.8 also gives `pataye` for asamāsa pati (Kāśikā: patye) | atideśa/saṃjñā sūtras must be invoked; 1.4.8 asamāsa condition |
| 2.4.78 / 2.4.79 | FAIL | luṅ of ghrā lacks the sic-luk reading `aghrAt`; tan ātmane lacks `atata` | 2.4.78/79 vibhāṣā reading in the luṅ spine |
| 2.4.49 | FAIL | iṅ + liṭ gives `aDIye`, Kāśikā adhijage (gāṅ ādeśa) | 2.4.49 in the liṭ spine |
| 2.1.x / 2.2.x | see sig/lk_case_verdicts/a2.json | samāsa machine slice 2 covers 2.1.6/24/36/37/40/51/52/57, 2.2.8/18/24/29, 2.4.17/18/26/71 only; others leave the members un-compounded | slice 3 |
| 1.2.x, 1.4.15/21/105/107, 2.3.x, 2.4.84 | UNRUNNABLE | no harness entry (kṛdanta with upasarga, ekaśeṣa, upapada yuṣmad/asmad, kāraka→vibhakti) — reasons are in each case's `note` | harness entry points (tools/exercise_audit `_derive`), not engine rules |
