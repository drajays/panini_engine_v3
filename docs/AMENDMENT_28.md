# AMENDMENT 28 — Article 24: the word-generation cycle (accepted by the owner 2026-10-31)

**Status:** accepted: *"put in constitution so that we remember this entire word generation web/cycle"* (owner, 2026-10-31), after the owner's four diagrams (prātipadika ↔ dhātu graph; adhyāya 1–2 prakṛti / 3–5 pratyaya / 6–8 pada; nested adhikāras 3.1.1 ⊃ 4.1.1 ⊃ 4.1.3 ⊃ 4.1.76; vākya = padasamūha). Adds Article 24; changes no existing Article.

## Problem
The engine had each arrow of the cycle as a separate entry point (docs/V4_CYCLE.md) but nothing stated the cycle as law, so recipes (kyac for two stems, ṭāp only in the subanta preflight, san/ṇic as laṭ-only flags) could grow without a connection between stages.

## Change
CONSTITUTION.md gains Article 24 and the Article 10 count becomes twenty-five (0 through 24). Enforcement: tests/unit/test_chain.py and tests/unit/test_chain_cycle.py (each stage composes with the next; the MVP examples run end to end); the ratchet is docs/V4_CYCLE.md (open links only shrink).
