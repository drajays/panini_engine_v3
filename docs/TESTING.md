# TESTING (the loop, the batch, the proof)

Rule: speed comes from running fewer *redundant* tests and making derivations cheaper — never from weaker assertions.

## Where the time is (measured 2026-11-11, `sig/test_durations.json`)
A full `-n8` run is ~1.3 h (26,000 CPU-s). 65 % of it is three families that run many whole derivations per test: `test_krdanta_loop_k*`, `test_taddhita_loop_t*`, `test_svarthika.py` (one kṛdanta `explore()` = 15 branches ≈ 220 s cold). `--tier=fast` (skip tests ≥ 5 s) only saves ~7 % because those tests are many and medium-sized, so **tiers are not the speed-up; impact selection is.**

| Tier | Command | When | Cost |
|---|---|---|---|
| Edit loop | `pytest -n8 <the sūtra's own tests>` | every edit | seconds |
| **Impact** | `python3 -m tools.test_impact quick -n8` (or `--impact-base <sha>`) | before each commit | minutes when only sūtra files changed |
| Proof | `pytest -n8 tests/` (add `--record-durations`) | end of a session, nothing else running | ~1.3 h |
| Re-map | `python3 -m tools.test_impact record-lite -n8` | after the proof run, or after adding many tests | ~1.3 h (same as a full run) |

## Impact selection (`tools/test_impact.py`)
- The map `sig/test_impact.json` (git-ignored) says, per test, which sūtras fired or were dispatched (`record-lite`: no profiler, runs under xdist; workers write parts that the controller merges).
- A changed `sutras/**/sutra_A_B_C.py` selects the tests that touched A.B.C **and** every sūtra file that imports it (`with_importers`: iyanuvan_sthana, NGIT_SUPS …), transitively.
- A changed shared file (engine/, pipelines/, phonology/, core/, data/) selects **everything** with a lite map (no function table) — the honest default. The slow `record` (profiler) maps functions so a one-function edit selects less.
- A test missing from the map, a changed test file, and all of tests/constitutional always run.
- Known limit (widening): a cond edited to be true where it never was can reach a test that never recorded it. Impact runs are the fast loop; the proof run is the gate for "done".

## Engine speed-ups (behaviour-neutral)
Memoised pure sūtra-id helpers (`engine/strata.py`, `engine/phase.py`, `engine/scheduler.py`), a per-phase candidate pool, the memo-key tail hoisted out of the per-candidate loop, atom fast paths in `copy_meta` and `_canonical`. ≈ 30 % on a bhū cell (4.5 → 1.6 s), a few % more from the fast paths. Profile of one kṛdanta explore (715 s under cProfile): `_canonical` 19 %, `State.clone`/`copy_meta` 28 % (apply_rule clones the probe clone again), `_only_self_announced` 5 %. Next structural win: probes should not deep-clone twice — safe only once every rule's writes to nested `meta` are known to go through Term.meta.
Timings drift with the machine's power state (same commit: 1.6 s then 3.1 s) — compare against a baseline measured in the same minute.

- `--tier=fast|slow`, `--slow-secs`, `--record-durations` exist in tests/conftest.py (tests unknown to the file are fast).
- Never `git stash` or edit `engine/` while a proof run is going; use a worktree if you must.
