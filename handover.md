# Handover — Sūtra Coverage → 100 %  (ON HOLD as of 2026-10-03; resume from here)

**Plan of record:** `docs/SUTRA_COVERAGE_100_PLAN.md` (v2) · **Law:** `CONSTITUTION.md` · **Program:** `ROADMAP.md`
**See it:** double-click `Panini Engine.command` → `/coverage` (confident sūtras by pāda; live recipe-free derivation
of nouns and laṭ verbs). Menu `c` refreshes the numbers. CLI: `make confident`, `make autonomy`.

## Where things stand
- **S0 done.** `tools/sutra_class.py` → `sig/sutra_class.json`, `docs/CONFIDENT_SUTRAS.md` (**216 of 3,983 confident**:
  99 operational + 117 structural). Exempt ratchet 3,205 (`tests/constitutional/test_exempt_ratchet.py`). Probes on clones
  go through `engine.scheduler.probe` and are not counted as firings.
- **S1 / ROADMAP C2 largely landed.** Loop (scheduler → resolver → apply_rule, no recipe): 11/11 certain subanta cases,
  3/3 bhū cells, laṭ kartari grid (6 roots × 9 cells), gaṇa-1 sweep **1,152 / 1,165** match the recipe
  (`.audit/tin_auto_sweep.py`, results in `.audit/tin_auto_sweep.json`). Suite: 19,948 passed.
  Mechanisms added: tape-fingerprint vacuity filter · Adhyāya 1 eligible in all phases · pada-merge at Tripāḍī boundary ·
  `apply_pratishedhas` before contention · resolver layers *upadeśa* (1.3.2) and *asiddha* (8.2.1) · tripāḍī cursor ·
  operational paribhāṣās (1.1.51) · adhikāra scope from records (`data/inputs/phase_adhikaras.json`).
- **Real rules written/repaired this stage:** 7.1.18, 2.4.75 (gaṇa 3), 6.1.10 (ślu witness), 6.1.78 (hears past lopa),
  8.4.46/47 (now VIBHASHA).

## Known gaps (the 13 gaṇa-1 misses are rule gaps, not loop gaps)
3.1.79 reads `vana~/zaRa~/kanI~` as tanādi by stem prefix · 7.3.75 (ṣṭhivu~ → ṣṭhīv) unmodelled · `SrA`/`jYA` homonym rows.
Recipe still makes राधे by a 6.1.87 shortcut; the loop uses the real 7.1.18 → śī route (C4 will reconcile).
Unmodelled in the loop: lakāras other than laṭ, ātmanepada/passive, juhotyādi ślu removal (placeholder term stays on tape),
kṛt/taddhita starts.

## Resume here (S1 remainder, in order)
1. **B2/B3** — declare conflicts (`apavada_of` / `blocks_sutra_ids`); the 87 निषेधs typed VIDHI (`docs/NISEDHA_REVIEW.md`; scholar confirms targets).
2. **The 393 invoked-but-unfinished sūtras** (see `sig/sutra_class.json`: status `gate_only`/`placeholder`/`working` with invoked=true), in Aṣṭādhyāyī order; delete pipeline code each real rule replaces, same commit.
3. **Gate C**: all 364 shipped derivations (`docs/data/traces/`) through the loop; other lakāras; then C3 (`derive()` → thin router) and C4 (pipelines → fixtures).
4. **S2** mechanisms (M1–M10 in the plan) before the S3 sweep. After every stage: `python3 -m tools.firing_coverage && make confident`, then report the confident list.

## Rules that bite
One file per sūtra (Art. 7) · no `_arm` keys / no utsarga narrowing (Art. 13/15) · no bare sūtra ids or `data/reference` mentions in `engine/` or sūtra files
(`test_prakriya_integrity`, `test_no_reference_import_from_engine`) · test expectations from Kāśikā/attested/oracle, never model-written (Art. 19).

## Caution
A second session commits to this repo (it swept uncommitted edits into `f6a213ce`). Check `git status`/`git log` before editing; prefer a worktree.
An old stash `trace noise` (branch claude/gan-3-rate-limit-handover) is still in `git stash list` — not mine, left alone.
