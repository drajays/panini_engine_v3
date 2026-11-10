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
