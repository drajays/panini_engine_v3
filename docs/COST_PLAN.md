# Cost-efficient routine for the remaining sūtras (2026-10-24)

1. **Pick by evidence, not by sūtra number:** `docs/data/subanta_gauge.json` (brain cells) and `docs/data/lk_gaps.json` rank sūtras by failing forms. Work a *cluster* (one stem family, 4–8 sūtras) per cycle.
2. **Iterate on the cheap loop:** `python3 -m tools.gcell <stems>` (seconds) + the focused test subset; never `make full-check` while a cluster is half-done.
3. **One `make full-check` per cluster** (≈11 min), then commit. The firing-ledger rebuild (`python3 -m tools.firing_coverage`, ≈12 min) only when the lint says so (a new pratiṣedha or a new unexercised-but-claimed sūtra).
4. **Read once:** `python3 -m tools.lk_show a b c …` for all sūtras of the cluster in one call; no `make brain` dumps.
5. **Write the cell test with the fix:** append the cluster's stems to `tests/regression/data/brain_declension_cells.json` (generated from the gauge) so evidence and regression land together.
6. **Shared helpers first** (`engine/declension.py`): a new rule is ~20 lines — site, condition, act; the pool slot in `pipelines/subanta.py` is the only wiring.
7. **Re-run the gauge (4 min, 8 workers) only between clusters** to pick the next one.
