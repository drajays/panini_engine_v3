# Cost-efficient routine for the remaining sūtras (2026-10-24)

1. **Pick by evidence, not by sūtra number:** `docs/data/subanta_gauge.json` (brain cells) and `docs/data/lk_gaps.json` rank sūtras by failing forms. Work a *cluster* (one stem family, 4–8 sūtras) per cycle.
2. **Iterate on the cheap loop:** `python3 -m tools.gcell <stems>` (seconds) + the focused test subset; never `make full-check` while a cluster is half-done.
3. **One `make full-check` per cluster** (≈11 min), then commit. The firing-ledger rebuild (`python3 -m tools.firing_coverage`, ≈12 min) only when the lint says so (a new pratiṣedha or a new unexercised-but-claimed sūtra).
4. **Read once:** `python3 -m tools.lk_show a b c …` for all sūtras of the cluster in one call; no `make brain` dumps.
5. **Write the cell test with the fix:** append the cluster's stems to `tests/regression/data/brain_declension_cells.json` (generated from the gauge) so evidence and regression land together.
6. **Shared helpers first** (`engine/declension.py`): a new rule is ~20 lines — site, condition, act; the pool slot in `pipelines/subanta.py` is the only wiring.
7. **Re-run the gauge (4 min, 8 workers) only between clusters** to pick the next one.

## Session cost rules (2026-10-30, owner: "minimise the cost in the next session, keep quality")
Measured this session: a fork inherits the whole conversation, so each fork's input cost grows with the main thread; six forks at once hit the monthly spend limit three times (each hit loses a round). Rules:
1. **Start every session with a clean context** (`/clear`), read only `docs/STATE.md` (one page), then spawn forks while the main context is still small — a fork launched at turn 5 costs a fraction of one launched at turn 300.
2. **At most 3 agents at once**; prefer 2 big disjoint batches over 6 small ones. Never launch agents just before a known limit reset; resume only after it.
3. **Mechanical work → a fresh non-fork agent with a model override** (`model: "sonnet"` or `"haiku"` and a self-contained prompt): generator runs, test generation from DB examples, merges of data files. Judgment work (core sandhi/it-saṃjñā/scheduler, amendments) stays on forks of the main model.
4. **Main thread stays terse**: no pasted agent reports in full; merge, apply the ≤25-line shared edits, one status table per batch.
5. **Heavy jobs once**: one niced full suite per merged set (≈ 2 h); the firing-ledger rebuild already ran a full suite (22k tests) — do not run both in a session. Focused tests first; constitutional tests (≈ 1 min) before every merge.
6. **Merge recipe** (conflicts are always the schema builder): `git merge`; resolve `tools/build_vivaksha_schema.py` by keeping both sides' lines; `python3 -m tools.build_vivaksha_schema`; commit.
7. **Prompts**: pre-allocated ledger ids, the laws in `/tmp/core.txt`-style file kept in `docs/AGENT_RULES.md` so a prompt is 5 lines; list the sūtras, the test-file name, the id range — nothing else.
