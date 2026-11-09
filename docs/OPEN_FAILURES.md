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
