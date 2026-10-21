# Brain as the final reference — plan (owner, 2026-10-21)

Owner: "make `~/data-master/ashtadhyayi-ai` the final reference for the engine — 100 % authentic, rule-based; whatever
other method we use, the brain must be updated; make best use of the Pushpa Dixit cards." Decisions taken the same day:
rulings live in the brain (engine mirrors them) · AMENDMENT 26 drafted for signature · the agent commits and pushes the brain
repo · cards from raw ASR notes stay `gist-only`; the agent may mark a card **verified** when every claim and form checks
against the brain's grantha tables, `accepted` still needs a grade-A quote.

## Principle
Knowledge flows **into the brain first, the engine second**, and the engine is tested against the brain. The brain is never
read by `cond()`/`act()` (Art. 6 unchanged).

## Steps
| step | what | state |
|---|---|---|
| B0 | `rulings/R-*.json` (owner rulings, evidence verified in the brain DB) + `corrections/X-*.json` (overrides of upstream values, anchored to the exact upstream text); `rulings/validate.py`; dossier prints both; SC-001..007 + SC-T mirrored (R-001..011), X-001 7.1.37 | **done** (brain 660ceb1) |
| B1 | engine checked against the brain: mirror test (`tests/constitutional/test_brain_rulings_mirror.py`), pinned brain commit (`data/inputs/brain_version.json`), Kāśikā-quote ratchet (`tools/kashika_quote_check.py`, `test_kashika_quotes_ratchet.py`: 106 docstrings label a paraphrase "Kāśikā" — ceiling only falls); next: sūtra pāṭha/samagra equal to the brain after corrections | mirror + pin + quote ratchet done |
| B2 | `make brain-sync`: engine status per sūtra (firing ledger, sutra_class), apavāda/blocks declarations and test forms exported into the brain each release, replacing hand-written `engine_status` in cards | next |
| B3 | cards → tests: accepted/verified cards' `data_tests` become engine regression tests (failing ones xfail with the card id = ranked gap list); cards gain `ruling_ids`, `engine_tests`; `verified` status in `cards/validate.py`; the 1,078 open questions ranked by the engine work they block and asked in batches | next |
| B4 | other methods (Vidyut, DCS, Saṃsādhanī, Heritage, AI) enter the brain only as evidence; a disagreement opens an `open` ruling | rule written in the brain guide |
| B5 | governance: AMENDMENT 26 (signature); AGENTS.md and the brain guide say "brain first"; a sūtra commit cites brain evidence or a ruling id | draft `docs/AMENDMENT_26.md` |

## Open owner questions (recorded as pending in the brain)
R-006: lakāra-ṅ / महिङ् exclusion from kṅit · R-005: 7.4.46 for दो / देङ् · 1.2.19/20/22 misreadings · 7.3.84 vs 7.3.86
(देवित्वा) · 7.2.56 उदितो वा · plan step (d) core-loop vacuity filter.
