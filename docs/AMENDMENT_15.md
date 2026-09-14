# AMENDMENT 15 — Conflict, Coverage, Analysis, Gaps, and External Verification

> Per Constitution Art. 10, this document records the proposed change, its
> rationale, and its acceptance status. The corresponding edits are applied to
> `CONSTITUTION.md` **only after this file is accepted in writing** (§5).

**Date opened:** 2026-09-15
**Author:** drajayshukla (measurements and drafting by Claude)
**Status:** PROPOSED — not yet in force.

---

## 1. Background — what was measured

Everything in this section was measured on this repository on 2026-09-15 and is
reproducible.

| finding | number | how |
|---|---|---|
| sūtra records registered | 3,985 | `len(SUTRA_REGISTRY)` |
| `coverage_report()` verdict | implemented 3,985 · stubs 0 · **100 %** | `coverage_report(SUTRA_REGISTRY)` |
| sūtras ever **invoked** in the whole suite | 569 | `apply_rule` wrapper over 19,117 tests |
| sūtras that ever **change the tape** | **296 (7.4 %)** | same run, `flat_slp1()` before/after |
| files carrying the placeholder gloss `(सूत्रम् X)` | 2,418 | `grep -rl 'why_dev.*(सूत्रम्' sutras/` |
| files whose `cond` is only `samhita_gate_eligible(...)` | 633 | grep |
| BLOCKED steps across all 364 shipped derivations | 24 | `docs/data/traces/` |
| dhātupāṭha entries by gaṇa | 986 total, **971 in gaṇa 1** | `pipelines/dhatupatha` |

Four defects follow from those numbers, and each is a gap in the Constitution
rather than a bug in a file:

1. **Conflict is being engineered instead of declared.** `sutra_6_1_102._matches()`
   restricted itself to `i`/`u`-final aṅgas so that रामौ would come out right. The
   निषेध that actually does that work — 6.1.104 नादिचि — was a registered stub typed
   `VIDHI` with `blocks_sutra_ids = ()`. The form was correct; the grammar was not.
   Twenty-four blocks in 364 derivations says this is systemic, not incidental.
   (Repaired 2026-09-15 in commit `41bbff7`; the repair is the template, and nothing
   in the Constitution yet requires it.)

2. **Coverage counts registration, not firing.** A record counts as "implemented"
   because the file exists. The honest rule base is 296. Article 0 forbids a lookup
   table; it does not yet forbid a coverage number that reports files as rules.

3. **Analysis has no law.** The engine is acquiring a reverse direction
   (`pipelines/patha_pipeline.py`), and the obvious shortcut — writing reverse rules
   — would create a second grammar that silently drifts from the first.

4. **Silence is treated as success.** 6,496 SKIPPED steps in the shipped derivations
   report nothing. A context the engine cannot model is information, and it is being
   thrown away.

---

## 2. Proposed amendments

### 2.1 Article 15 (new) — Conflict is declared, never engineered

> **Article 15 — Conflict is declared, never engineered**
>
> A sūtra's `cond()` describes **its own** condition as Pāṇini states it. It may
> never be narrowed to avoid another sūtra.
>
> When two sūtras claim the same position, the loser is determined by a declared
> relation — `blocks_sutra_ids` (प्रतिषेध), `apavada_of` (अपवाद), adhikāra scope, or
> stratum — and the winner is chosen by the engine's paribhāṣā layer, primarily
> **1.4.2 विप्रतिषेधे परं कार्यम्**. The losing sūtra appears in the trace as
> `BLOCKED`, naming the rule that beat it and why.
>
> An utsarga that excludes a case in order to let an apavāda through is a
> constitutional violation even when every test passes, because the derivation then
> records a reason Pāṇini did not give.
>
> *Enforcement:* `tests/constitutional/test_no_engineered_conflict.py` — for every
> sūtra pair where a declared block exists, the utsarga's `cond` must be true at the
> blocked position; a `cond` that is false there has absorbed the निषेध.

### 2.2 Article 16 (new) — Coverage is firing, not registration

> **Article 16 — Coverage is firing, not registration**
>
> A sūtra counts as **implemented** only when all four hold:
> 1. it is **invoked** by at least one derivation in the test suite;
> 2. it **changes the state**, or is explicitly `r1_form_identity_exempt`;
> 3. it carries a **citation** to sūtra text and to the source that justifies its
>    predicate (Art. 14);
> 4. it carries **≥ 3 positive and ≥ 2 negative tests** — "must not fire here" is
>    half of what a sūtra means.
>
> Everything else is **registered**, not implemented, and the two counts are
> reported separately. No document, README, or interface may present the registered
> count as coverage.
>
> *Enforcement:* `coverage_report()` returns both counts and the honest number is a
> committed artifact; `sutra_lint` fails a rule that claims implementation without
> the four conditions.

### 2.3 Article 17 (new) — Analysis proposes, generation verifies

> **Article 17 — Analysis proposes, generation verifies**
>
> The engine has exactly one rule base, and it runs in one direction: generation.
>
> Analysis (pada-cheda, morphological identification, kāraka labelling) may only
> **propose candidates**. A candidate becomes an answer only when the forward engine,
> run on that candidate, reproduces the input string exactly. The accepted analysis
> ships with that forward derivation.
>
> No reverse rule may be written. Sandhi may be *inverted* mechanically as an
> over-generating candidate source; morphology may be *enumerated* into an index.
> Neither is a rule.
>
> **The form index is a cache, never a grammar.** Any table of generated forms is a
> build artifact: regenerated from the engine, never hand-edited, and re-derived in
> CI. A form in the index that the engine can no longer derive is a build failure.
>
> *Enforcement:* `tests/constitutional/test_index_is_regenerable.py` — a sample of
> the index must re-derive; `test_no_reverse_rules.py` — no rule file may declare an
> operation whose direction is surface → constituent.

### 2.4 Article 18 (new) — A gap is an output

> **Article 18 — A gap is an output**
>
> When the engine cannot derive or cannot analyse, it must say **what is missing**,
> naming the sūtra, the dhātu, or the lexical entry that would close the gap.
> Silence is a bug.
>
> An unrecognised word is a gap, never a guess. No statistical fallback, no
> "probably a noun", no partial form presented as a derivation. A closed world that
> states its boundary is worth more to a scholar than an open one that improvises.
>
> Gaps are emitted in the trace and aggregated into a frequency-ranked worklist;
> that list, not intuition, orders implementation.

### 2.5 Article 19 (new) — We do not grade our own homework

> **Article 19 — We do not grade our own homework**
>
> Correctness claims are settled against sources outside this repository:
> attested usage from the corpus, the classical commentaries, and at least one
> independent implementation.
>
> Every release publishes its agreement rate and the commands that reproduce it.
> A disagreement with an external oracle is a **work item**, never a verdict in
> either direction: the other implementation may be wrong, and the investigation is
> the deliverable.
>
> No number may appear in the README that a reader cannot regenerate with one
> command.

---

## 3. Consequences for existing Articles

- **Article 0** is unchanged and is the reason for all five additions.
- **Article 7 (No Rule Bundles)** is strengthened by Art. 15: a pipeline's ordered
  list is itself a bundle of scheduling decisions, and Art. 15 moves those decisions
  into declared relations.
- **Article 12 (Fullest valid sūtra path)** and Art. 16 are complementary: Art. 12
  governs the path taken, Art. 16 governs what may be counted.
- **Article 14 (Authoritative Sources)** supplies condition 3 of Art. 16.
- No existing Article is repealed or weakened.

## 4. Migration, and what is grandfathered

Adopting Art. 16 changes the reported coverage from 3,985 to ~296 on the day it
lands. That is the point, not a regression: the number stops being about files.

The 2,418 placeholder files are **not** deleted. They are reclassified from
implemented to registered, and they become the worklist Art. 18 requires.

Art. 15's enforcement test is expected to fail in several places on its first run
(6.1.102 was one; it is repaired). Per the rollback convention below, each failure
is investigated individually; none may be silenced by weakening the test.

## 5. Acceptance

This Amendment takes effect only when signed here. Until then, `CONSTITUTION.md`
is unchanged and Articles 15–19 have no force.

```
Accepted by: ________________________  date: __________
```

## 6. Rollback

If the enforcement tests in §2 break more than five currently-passing forward tests
on their first run, this Amendment is suspended and the authors either refine the
test to match true intent or open `AMENDMENT_15_revision.md`. A failing enforcement
test is never silenced to restore a green suite.
