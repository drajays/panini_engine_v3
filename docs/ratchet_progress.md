# Ratchet progress tracker (duplicate scheduling blocks)

Baseline: **112** duplicate scheduling-block groups.

This tracker is a *target trajectory* for the collapse campaign (largest-first),
so we can quickly sanity-check that each batch of collapses is moving the ceiling
down in a roughly linear way.

## Target milestones

```
START   : 112 duplicate groups
After   5: 107  (run: python audit/ratchet_collapse.py --run 5)
After  10: 102
After  20:  92
After  50:  62
After  80:  32
After 100:  12
After 112:   0  ← FULLY CANONICAL ENGINE
```

## Notes

- The *actual* curve may be better than this when one collapse removes multiple
  overlapping windows.
- The constitutional gate (`tests/constitutional/test_no_new_duplicates.py`)
  enforces a **ceiling**; after each successful collapse batch, lower the ceiling
  with:

```bash
python audit/ratchet_collapse.py --ratchet-to-current
```

