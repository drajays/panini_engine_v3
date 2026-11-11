# TESTING (the loop, the batch, the proof)

Rule: speed comes from making derivations cheaper and from running fewer *redundant* tests — never from weaker assertions.

| Tier | Command | When | Cost |
|---|---|---|---|
| Edit loop | `.venv/bin/python -m pytest -n8 --tier=fast <the sūtra's own tests>` | every edit | seconds–minutes |
| Impact | `python3 -m tools.test_impact quick --base <sha>` | before a commit (needs `sig/test_impact.json`) | minutes |
| Batch | `.venv/bin/python -m pytest -n8 --tier=fast tests/` | end of a cluster | tens of minutes |
| Proof | `.venv/bin/python -m pytest -n8 --record-durations tests/` | end of a session, nothing else running | ~2 h; refreshes `sig/test_durations.json` |
| Slow only | `… --tier=slow tests/` | the krdanta_loop_k* / paradigm files, overnight | the rest |

- `--tier` reads `sig/test_durations.json` (nodeid → seconds, committed). A test is *slow* if recorded ≥ `--slow-secs` (5). A test not in the file is always in the fast tier, so a new test can never be skipped.
- Fast + slow together = the whole suite; the proof run is the gate for "done".
- Engine speed-ups (2026-11-11, behaviour-neutral, memoising pure functions of a sūtra id or hoisting state-constant memo-key parts): `engine/strata.py` (`_tuple`, `in_tripadi`, `sees_tripadi_nimitta`), `engine/phase.py` (`sutra_in_phase`, `is_tripadi_sutra`), `engine/scheduler.py` (`_id_tuple`, `_phase_pool`, `effective_candidates` key tail). One bhū cell 4.5 s → 1.6 s under cProfile; bhū paradigm file 267 s → ~180 s. Remaining hot spots: `enumerate_candidates` (per-step cond sweep), `core_loop.apply_pratishedhas`, `tape_fingerprint`/`_canonical`.
- Never `git stash` or edit `engine/` while a proof run is going; run it from a clean worktree if you must keep working.
