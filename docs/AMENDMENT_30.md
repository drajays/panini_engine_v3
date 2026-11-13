# AMENDMENT 30 — open vivakṣā: explore every applicable meaning (proposed; owner said "go ahead" 2026-11-13)

**Status:** accepted to pilot on tiṅanta + kṛdanta. Touches Amendment 25 only by adding *how a request leaves a key open*; the law "only the request sets a vivakṣā, at tape init, from a closed cited vocabulary; a sūtra asks only for a value its own samagra names" is unchanged.

## Problem
Amendment 25 takes one fixed value per key from the caller. A caller (the exercise audit, the reader, a user) usually does not know which meanings apply, so tables of guessed meanings grow in tools (`_KRT_VIV`), and 1.3.47-50 / 1.3.66 cannot be reached at all (`derive()` has no vivakṣā input).

## Rule
1. **Request** = `vivaksha={key: value | OPEN | DEFAULT}`. A value is fixed by the user; `OPEN` means "explore"; `DEFAULT` (or omitted) is the key's unmarked value.
2. **Probe and replay** (`engine/vivaksha_explore.py`, outside the derivation): run the derivation with every open key at its default and record which keys a sūtra's `vivaksita(...)` asked about (a read-only trace, never a write). For each asked open key, rerun once per schema value of that key (plus the default), the value placed on the tape **at tape init**, as now. Repeat until no new key is asked. Only asked keys are explored: no product over the whole schema.
3. **Output**: each reading is a `Branch` whose `choices` hold the vibhāṣā choices *and* `("vivaksha", key, value)` entries, so every surface form carries the meaning that produced it and every step is an `apply_rule` trace as before.
4. **Schema fields per key** (`tools/build_vivaksha_schema.py` builds them; each value stays cited): `default` (unmarked value), `applies_to` (entry points: tinanta, krdanta, taddhita, subanta, samasa), `requires` (e.g. kartrabhiprAya only with a ṇic Term), `gloss_dev` / `gloss_en`.
5. **Intent vs context**: keys are `kind: intent` (speaker's choice: explored or fixed) or `kind: context` (facts of the sentence: vyaktavāc agent, samuccāraṇa, vipralāpa). A context key is never explored; it is supplied by the caller or, later, by the text layer from neighbouring words.
6. **New values** (1.3.47-50, 1.3.66, kṛt meanings) enter the schema only with a citation: the sūtra's samagra, or the Kāśikā under Amendment 27's route.

## Invariants (tests)
- `set_vivaksha` is still called only from `engine/tape_init` (`test_vivaksha_set_only_by_tape_init`); replay builds a new tape per branch.
- `vivaksita` stays the only reader; asking for a key marks it asked, never changes the result.
- A derivation that asks no open key yields exactly one branch, equal to today's `derive()`.
- No word recipe: a meaning is never inferred from a surface form.

## Not changed
Fixed-value callers, every sūtra's `cond`, the closed vocabulary, the rule that the engine never guesses a value.
