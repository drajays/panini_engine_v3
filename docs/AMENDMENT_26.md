# AMENDMENT 26 — the brain is the final reference (DRAFT, awaiting the owner's signature)

**Requested by the owner 2026-10-21:** "make `~/data-master/ashtadhyayi-ai` the final reference for the engine … 100 %
authentic, must be based on rule … whatever other method we use, this must be updated as final reference."

## Text proposed for the constitution (new Article 24)
1. **Canonical store.** `~/data-master/ashtadhyayi-ai` (git `drajays/Ashtadhyayi_brain`) is the canonical store of the
   evidence the engine is built from: the ashtadhyayi.com pāṭha and commentaries (Art. 22 tiers), the teacher concept cards
   (Art. 23), the owner's rulings (`rulings/`) and the corrections of upstream values (`corrections/`).
2. **Brain first.** A ruling, a correction of upstream data, or a finding from any method (engine work, Vidyut, DCS,
   Saṃsādhanī, Heritage, AI) is recorded in the brain before engine code depends on it. Non-grantha sources are evidence
   only (Art. 19) and open an `open` ruling when they disagree.
3. **Engine checked against the brain.** `docs/SOURCE_CONFLICTS.md` mirrors the brain's rulings; the engine pins the brain
   commit it was checked against (`data/inputs/brain_version.json`); tests enforce both. Every sūtra commit cites brain
   evidence (Art. 14) or a ruling id.
4. **Authenticity.** A card is `accepted` only on a grade-A (corrected) quote; `verified` when every claim and form resolves in
   the brain's grantha tables; raw ASR alone is `gist-only`. Upstream files are never edited — corrections are overlays.
5. **Firewall unchanged.** The brain is design-time only; Art. 6 (no reads from `cond()`/`act()`) stands.

## Effect
Art. 14's evidence roster and Art. 22/23's tiers are unchanged; this article fixes *where* their output is stored and how the
engine is held to it. Implementation: `docs/BRAIN_FINAL_REFERENCE_PLAN.md` (B0–B1 done 2026-10-21).

**Signature:** _pending_
