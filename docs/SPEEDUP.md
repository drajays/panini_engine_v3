# SPEEDUP — making the glass-box engine fast without making it less rule-based

Rule: speed is bought only where it cannot change which sūtra fires, in which order, or what the trace says.
The grammar (cond/act, canonical order, `apply_rule`-only, `origin:<sutra_id>` stamps) is never touched.
A speedup is accepted only if the constitutional suite and an output-equality check (forms + traces) are identical before/after.

## Measured baseline (2026-11-09, `derive("pac","laT","kartari",3,1)`)
- ≈14 ms wall, 111 `apply_rule` calls (the pipelines call rules by name in a fixed order; nothing scans the whole sūtra table).
- cProfile (46 ms): `State.clone()` ≈ 24 ms (deepcopy of `Term.meta`), `extract_chronological_sutra_sequence` ≈ 5 ms (111 calls), rest is small.
- So the review's "skip 98% of cond calls with a 64-bit mask" does not apply: there is little to skip.

## Plan (in order of payoff / effort)
1. **Cheap `clone()`** — keep sūtras mutating in place. `Term.meta` shallow copy + copy only mutable values (set/list/dict) one level; `Varna` tags shared-until-write is NOT used (in-place `v.tags.add` exists). Gate: constitutional + unit output equal.
2. **Trace sequence incremental** — `extract_chronological_sutra_sequence` recomputed every step; keep it append-only or compute lazily.
3. **Prefix memoization** (paradigm / corpus runs): cache the state after initial upadeśa it-lopa, keyed on the full input incl. meta; replay keeps the origin stamps. Only if full-paradigm runs are slow in practice.
4. **Re-profile.** Only then consider: a per-sūtra `required_mask` pre-filter (needs each mask derived from the sūtra's own saṃjñā words and kept in sync with `cond`; a stale mask silently disables a rule, so add a test that compares masked vs unmasked firing), bitset pratyāhāras, tuple-based copy-on-write state (rewrites every sūtra that does `varnas.insert`), mypyc / Rust core (after the Laghukaumudī is finished).

## Equality harness
`tools/speed_equal.py` — runs a fixed set of derivations (tiṅanta, subanta, kṛdanta; several lakāras/gaṇas), writes final form + full trace (sutra_id, status, form_before/after) as a digest. Run before and after each step; digests must match exactly.

## Not doing
- Anything that reads vibhakti/vacana/lakāra coordinates in a mask (Art. 2), reorders rules (Art. 3), or bypasses `apply_rule`.
