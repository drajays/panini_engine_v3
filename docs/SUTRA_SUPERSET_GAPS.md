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

## Update 2026-10-04 (after the ātmanepada loop work)

Loop vs recipe, ātmanepada, first 20 gaṇa-1 roots (`python3 -m tools.loop_vs_recipe tinanta --lakara X --pada atmane --limit 20`):

| lakāra | agree /180 | remaining |
|---|---|---|
| laṭ, luṭ, lṛṭ, loṭ, laṅ, liṅ | 180 | — |
| liṭ | 178 | 2pl `cakfDve` for `cakfQve`: 8.3.78 needs the aṅga/pratyaya boundary, which the Tripāḍī merge discards |
| luṅ | 171 | `muda~`: 1.2.11 makes sic kit before iṭ arrives (7.2.35 only opens after 6.4.71); Vidyut gives `amodizi` |
| āśīrliṅ | 96 | 2sg `ṣṭhās` (8.3.59 + ṣṭutva) and 2pl `ḍhvam` (8.3.78) not reached |

The Vidyut⊆engine gap list above is measured on the recipe path (`pipelines.tinanta.derive`) and is unchanged: the top item, 1.3.12 (683 of 756 cells), is `SKIPPED` in the recipe for every ātmanepadī root because 1.3.12 has no structural condition (the dhātu's anudātta/ṅit it-marker is not read off the tape). That is the next rule to make structural, then 3.4.113/114 (saṃjñā recognition in the liṭ/luṅ recipes), then 8.3.111, 7.4.61, 8.4.37.

## Update 2 (1.3.12, 3.4.113, 3.4.114)

`tools/sutra_superset.py --roots 12 --lakara laT liT laG luG lRT loT liG`: cells with **no** Vidyut sūtra missing from the engine rose from 7 to 400 of 756.
- 1.3.12 now fires for ātmanepadī roots (its cond was self-contradictory: it read the same meta key as both a veto and a requirement).
- 3.4.113 now classifies a tiṅ behind a vikaraṇa (luṅ: dhātu + sic + tiṅ); the luṅ recipe also calls 3.4.114 for the sic.

Still missing, by size: 3.4.107 suṭ in ātmanepada liṅ (recipe path), 8.3.111 (a padādi-s ṣatva prohibition Vidyut records; our rule is a gate stub), 1.3.2/1.3.3 (Vidyut records them on the lakāra's own it-letters), 7.2.13 and 1.3.3 in liṭ dual cells, 7.4.61, 8.3.24, 1.1.5, 3.1.40 (āṃ-liṭ in the recipe path).
