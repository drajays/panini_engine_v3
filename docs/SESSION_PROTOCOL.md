# Session protocol — plan the length, spend tokens once, hand over

Owner (2026-10-28): the register of left-out sūtras covers 1.1.1 onward for the Laghukaumudī scope and is updated after every session; extra agents may be used to finish faster; sessions are planned for length with a handover that saves tokens. (This lifts the earlier "no forks" rule for disjoint work only; the shortcut policy still stands: every shortcut marked `# SHORTCUT Sn` and in `docs/SHORTCUT_LEDGER.md`.)

## One session = one batch (≈ 25–40 sūtras of one prakaraṇa)
1. Read `handover.md` (last Update paragraph only) and `docs/DEFERRED_SUTRAS.md` for the next prakaraṇa.
2. Generate the batch from a table (pattern: `tools/` or scratch generator → `wrap`), vivakṣā values in `tools/build_vivaksha_schema.py`.
3. Focused tests while working; **the full suite once, at the end, by the main session only** (never two heavy jobs at once).
4. End-of-session checklist, in order: full suite green → `python3 -m tools.sutra_class` → `python3 -m tools.lk_plan` → `python3 -m tools.deferred_register` → one `Update` paragraph in `handover.md` (done, left out + where recorded, next) → commit only own files (never the unstaged edits of others).

## Agents
- Use an agent (fork) only for a **disjoint set of sūtra files** (e.g. one pāda, or 4.4 vs 5.1) with its own test file; it runs focused tests only and reports file list + failures in ≤ 10 lines.
- Shared files (`engine/*`, `tools/build_vivaksha_schema.py`, `data/inputs/*`, `docs/*`) are edited by the main session only; an agent proposes the line, the main session applies it.
- Never run the full suite in an agent. Forks inherit context, so prompts stay one paragraph.

## Length planning
- Start of session: state the batch and the stop point (the last sūtra id) in one line; stop there even if budget remains, run the checklist, hand over.
- Rule of thumb from 4.3/4.4: ~30 sūtras ≈ one generator + one test file + one suite run; a suite run is ~40–80 min wall time, so start it as soon as the batch's focused tests pass and do doc work (not source edits) while it runs.

## Commitments (owner, 2026-10-28)
- **End aim:** a blind, glass-box, rule-based engine that generates every Sanskrit word from Pāṇini's rules alone. Every sūtra acts through `apply_rule`; no recipe knows the answer.
- **No duplicates, no useless recurring work:** one sūtra, one implementation. The `_legacy_cond/_legacy_act` halves kept beside the loop versions (T2–T6 files) are a duplicate to be removed (ledger S24) as soon as `core/canonical_pipelines` and the old recipes run through the loop. Do not regenerate or rerun what has not changed (focused tests first; one full suite per session).
- **Tactical shift** (a shortcut, a stand-in, a narrow stub) only when exceptionally needed: mark `# SHORTCUT Sn`, add the ledger row with the replacement and the stage, list it in `docs/DEFERRED_SUTRAS.md`, and close it at the earliest practical point.
- **Machine load:** heavy jobs run singly and niced — `nice -n 15 python3 -m pytest tests -q -p no:cacheprovider` — never beside another heavy job, never xdist. A full run is one core by design; check `ps` before calling it hung (the log advances in 1 % steps, ~10 min each in the 80 % – 90 % band).
