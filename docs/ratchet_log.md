# Ratchet log

## 2026-04-25 15:57:47

- **baseline_before**: 112
- **baseline_after**: 75
- **current_duplicates**: 75
- **delta**: 37

## 2026-04-25 23:13:35

- **baseline_before**: 75
- **baseline_after**: 39
- **current_duplicates**: 39
- **delta**: 36

## 2026-04-26 05:19:40

- **baseline_before**: 39
- **baseline_after**: 3
- **current_duplicates**: 3
- **delta**: 36

## 2026-04-26 05:45:59

- **baseline_before**: 3
- **baseline_after**: 0
- **current_duplicates**: 0
- **delta**: 3


## 2026-10-01 09:55 — T0 baseline (CURSOR_HANDOVER.md)

Tree at `6cbfa8fa` (only Claude's untracked `docs/CURSOR_HANDOVER.md` and a stale
generated trace `docs/data/traces/tinanta.derive_abhavaM.json` outside the commit —
the latter is a case-insensitive filename clash with `derive_abhavam`, not engine work).

- **pytest tests -q**: 19753 passed, 5 skipped, **0 failed** (baseline failing ids: none)
- **Vidyut bench** (`python3 -m bench.run`): 417/417 agree
- **arm-gated cond() reads** (`test_no_new_arm_gates`): 0 (baseline 0)
- **`"…_arm"` string literals left in `sutras/`** (non-cond): 136
- **glass-box trace gaps** (`tools.glassbox_gaps`): 48 in 40 derivations (ceiling 48)
- **placeholder sūtra files**: 914 (ceiling 915)
- **hand-pushed adhikāra frames**: 5 `_push_adhikara` calls in `engine/adhikara_automation.py`, 7 push sites in engine/core/pipelines
