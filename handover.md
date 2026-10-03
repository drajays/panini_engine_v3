# Handover — Sūtra Coverage → 100 %

**Date:** 2026-10-03 · **Plan of record:** `docs/SUTRA_COVERAGE_100_PLAN.md` (v2 — supersedes the earlier draft)
**Law:** `CONSTITUTION.md` (Art. 2, 3, 7, 13, 15, 16, 21) · **Program:** `ROADMAP.md`

## Measured state
registered 3,983 · invoked 778 · moved 385 · bench agreement 81.1 % (338/417).
3,414 files set `r1_form_identity_exempt=True` and `engine/coverage.py` counts invoked+exempt as moved — the
metric is leaky. 615 Adhyāya-6 files (6.1:170, 6.2:195, 6.3:129, 6.4:121) are gate-only placeholders
(`return samhita_gate_eligible(...)`, `act` only sets a gate key) — unwritten rules, not stubs.

## Next steps, in order (do not skip ahead)
1. **S0** — exempt-flag audit + ratchet (only structural classes may be exempt); `tools/sutra_class.py` →
   `sig/sutra_class.json`; per-class numbers in `make coverage`. Record bench baseline.
2. **S1** — B2/B3 (declared conflicts, 87 निषेधs), C2 (vacuity filter, `para` only for same-site contention),
   then finish the 393 invoked-not-moved sūtras in Aṣṭādhyāyī order; delete pipeline code each real rule replaces.
3. **S2** — one design session per mechanism (M1–M10 in the plan) before any bulk sweep; ≤1 new mechanism per batch.
4. **S3** — sweep pāda by pāda 1.1 → 8.4 (accent 6.2 deferred to Track G). Track B (analysis, Phase E) runs in parallel after S1.

## Rules that bite
- One file per sūtra (Art. 7); a generator may *emit* files from a cited table, never a bundle module.
- No `_arm` keys, no utsarga narrowing (Art. 13/15); declare `apavada_of`/`blocks`.
- Tests expectations come from Kāśikā udāharaṇa / attested prayogas / oracle — never model-written (Art. 19).
- Placeholders may hide pipeline shortcuts: a newly real rule that breaks a form is an Art. 18 gap, not a revert.

## Open input
Hours/week (ROADMAP §7.1) — the plan is order- and gate-based and does not depend on it.
