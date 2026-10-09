# AMENDMENT 24 — Rule-basedness; the ācārya method as the final conflict layer

**Status:** accepted 2026-10-09 on the owner's instruction: "the engine must always be rule-based on Pāṇini sūtras, vṛtti, vārttika, paribhāṣā;
add Dr. Pushpa Dixit's concept as a further conflict-resolution method". Branch `amendment-24`; merged after the constitutional tests pass.

## Problem
Art. 23 (AMENDMENT 23) says who decides *concepts*, but it does not say what a **runtime** decision may rest on, and it does not place the
ācārya method on the conflict ladder (Art. 21). The engine audit (`docs/ENGINE_VS_PUSHPA_AUDIT.md`) found decisions resting on probing
heuristics (W10), hand-typed pair verdicts (W8) and numeric ranges (W2, W11).

## Decision
1. **Basis (new Art. 23 §0).** Every runtime decision rests on the sūtras, the vṛtti (Art. 22 T7), the vārttikas (T1) and the paribhāṣās
   (Paribhāṣenduśekhara and the Bhāṣya's paribhāṣās). The decision record names its basis. Nothing else may decide: not a teacher's name,
   not a surface form, not a count, not an unnamed heuristic.
2. **Further method (Art. 21 and Art. 23 §2a).** Ladder 1 gains a final layer, **ācārya-prakriyā**: when every modelled layer leaves two or more
   candidates, or a conceptual question is open, the *accepted* concept cards decide — prakaraṇa block (a rule outside the active prakaraṇa is
   not offered), stage (sopāna) order, aṅga per pratyaya, the same-stage asiddha rule. A card enters the engine only as **sūtra-grounded
   data** (blocks, nimitta predicates, stage membership); its decision record names the card id and the sūtras it rests on. Pushpa Dixit's
   name never appears in `cond()`/`act()`.
3. **Art. 23 §2** is read together with §0: objective granthas decide; in doubt Pushpa Dixit; her method is also the last ladder layer.
4. **Status of the layer:** `ācārya-prakriyā` is `not_modelled` until phases P4/P5 of `docs/PRAKARANA_MACHINE_PLAN.md`; a conflict that would turn
   on it is an Art. 18 gap naming the layer, as for any unmodelled layer.
5. **Topical prakaraṇas (Art. 23 §6 widened).** A block is delimited by an adhikāra head **or** by anuvṛtti descent of a kārya word from a
   head sūtra (pāṭha data: `sutras.anuvrtti`), e.g. नुम् from 7.1.58 → 7.1.58–83, सम्प्रसारणम् from 6.1.13 → 6.1.13–44. Key A for such a block is the
   anuvṛtti chain itself.

## Verification
`pytest tests/constitutional` on the branch; only `CONSTITUTION.md` and `docs/` change; no engine code in this amendment.

## Acceptance
Owner, 2026-10-09 (session instruction quoted above).
