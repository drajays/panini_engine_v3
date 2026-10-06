# AMENDMENT 21 — vārttika convention (proposed; implementation deferred to Track G)

**Status:** proposed. Records the convention so nobody invents a different one; no vārttika file is added now
(`docs/SUTRA_COVERAGE_100_PLAN.md` Track G: vārttikas come after Gate E).

## Convention

1. **Id:** `<sūtra id>.v<n>` — e.g. `6.1.89.v1` — where `n` is the vārttika's order under that sūtra in
   ashtadhyayi.com `sutraani/vartika.txt` (921 vārttikas). Same shape as the codes Vidyut emits (`3.1.96.2` style),
   so traces from both line up.
2. **File:** `sutras/adhyaya_A/pada_P/varttika_A_P_N_<n>.py`, one vārttika = one file = one record, beside its sūtra.
3. **Record:** a `SutraRecord` with `sutra_id = "<A.P.N>.v<n>"`, its own `SutraType` (Art. 1 — a vārttika is a vidhi,
   pratiṣedha, … in its own right), `text_dev` = the vārttika text, `samagra_*` = it with the parent's anuvṛtti,
   and `varttika_of = "<A.P.N>"`.
4. **Authority:** T1 (Art. 22) — a vārttika outranks every commentary; where it conflicts with the sūtra's plain
   reading, the vārttika wins and the docstring says so.
5. **Required when implemented:** `SutraRecord._validate_basics` accepts the `.v<n>` suffix; `test_sutra_identity`
   learns the `varttika_` filename; the registry keys stay strings.

## Source

ashtadhyayi.com `sutraani/vartika.txt`; listed per sūtra by the reference brain (`knowledge_api.py dossier <id>`).

## Acceptance

Pending.
