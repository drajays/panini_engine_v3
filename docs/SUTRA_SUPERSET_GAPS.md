# Vidyut-sūtra ⊆ engine-sūtra gap list

Invariant (user, 2026-10-04): in no derivation may Vidyut fire a sūtra our engine does not execute; the engine adds every further sūtra Pāṇini's rules make applicable.

Measured with `.venv/bin/python -m tools.sutra_superset --roots 12 --lakara laT liT laG luG lRT loT liG` (first 12 gaṇa-1 roots, kartari, default pada). "Executed" = trace status APPLIED, APPLIED_VACUOUS, DEFINED, VACUOUS or AUDIT (not SKIPPED/BLOCKED). The web pages /dhaturupa and /shabdarupa show the same comparison per cell, missing sūtras in red.

```
756 cells · 7 with no Vidyut sūtra missing from the engine · 749 with gaps
  683  1.3.12
  108  3.4.113
  108  3.4.114
   72  8.3.111
   56  1.3.3
   55  1.3.2
   48  3.4.107
   42  7.2.13
   18  7.4.61
   15  1.3.4
   11  8.4.37
   10  6.1.90
   10  1.3.21.v7
    9  8.3.24
    9  3.1.40
    9  1.1.5
    3  1.3.7
    1  1.4.14
    1  1.2.4
    1  3.4.82
    1  3.4.89
```

Reading it:
- **1.3.12** (683) and most of 3.4.107 / 3.4.113-114 / 1.3.2-4: the first twelve gaṇa-1 roots are mostly ātmanepadī, and Vidyut derives them in ātmanepada by default while the engine's `derive` defaults to parasmaipada. These close with ātmanepada (3.4.79–93, 3.4.102, 3.4.106) and 1.3.12 as the pada-assigning step — the handover's next item.
- **8.3.111, 7.4.61, 8.4.37, 6.1.90, 8.3.24, 1.1.5, 3.1.40**: real per-rule gaps (the loop/recipe reaches the form by another route and never records the rule).
- Work order: ātmanepada first, then re-run this tool and take the remaining codes one by one. Add a ratchet (gap count may only fall) once the baseline is stable.
- Not available from Vidyut: sandhi. `vidyut.sandhi` offers only a splitter, no rule-by-rule application, so a sandhi parallel page has no Vidyut sūtra list to compare against.
