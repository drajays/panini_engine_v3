# CONSTITUTION.md — Pāṇini Engine v3

> The supreme philosophical law. Nothing in this repository may be committed
> that violates these Articles. `README.md` describes layout; this file
> describes law.

---

## Article 0 — Purpose

The engine exists to **derive any Pāṇinian form mechanically**, in a way
that a classical scholar could audit line-by-line. It is not a parser,
not a lookup table, not a Kaumudī stylesheet. It is an interpreter for
the Aṣṭādhyāyī as a rewrite system.

**Glass box, not black box.** If you cannot explain every step in
Pāṇini's own terms, the engine has failed — even if the surface form
is correct.

---

## Article 1 — The Ten-Fold Sūtra-Lakṣaṇa

Per the classical śloka:

```
षड्विधं सूत्रलक्षणम्: संज्ञा परिभाषा विधिः नियमः अतिदेशः अधिकारः।
दशविधं योजयति: + प्रतिषेधः अनुवादः विभाषा निपातनम्।
```

Every sūtra in this engine carries exactly **one** `SutraType`:

| # | Type         | Devanāgarī  | Behaviour                                    |
|---|--------------|-------------|----------------------------------------------|
| 1 | SAMJNA       | संज्ञा      | Registers a technical term                   |
| 2 | PARIBHASHA   | परिभाषा     | Sets an interpretive gate                    |
| 3 | VIDHI        | विधि        | Performs a phonemic operation                |
| 4 | NIYAMA       | नियम        | Restricts a prior vidhi                      |
| 5 | ATIDESHA     | अतिदेश      | Transfers a property by analogy              |
| 6 | ADHIKARA     | अधिकार      | Opens/closes a scope gate                    |
| 7 | PRATISHEDHA  | प्रतिषेध     | Blocks a named rule                          |
| 8 | ANUVADA      | अनुवाद      | Pure restatement (trace-only)                |
| 9 | VIBHASHA     | विभाषा      | Optional rule (forks the derivation)         |
| 10| NIPATANA     | निपातन      | Exceptional form, freezes the state          |

The 6-fold list is the ontological taxonomy; the 10-fold list is the
**operational** taxonomy, and the engine executes on the latter.

---

## Article 2 — Mechanical Blindness

The engine is **blind** in the following strict sense:

1. It does not know what a "subanta" or a "tiṅanta" *means*. It only knows
   that certain `SutraType`s operate when certain phonemic/saṃjñā conditions
   are met in the state.
2. `cond(state)` may inspect:
   - Varṇas by their SLP1 phonemes and tags (`anunasika`, `it_candidate_*`)
   - Pratyāhāra memberships (`AC`, `HAL`, `IK`, ...)
   - Saṃjñā registry (`ghi`, `nadi`, `sarvanama`, ...)
   - It-tags on Varṇas
   - Adhikāra stack
   - Upadeśa identity on a pratyaya Term (`upadesha_slp1 == "Ne"`)
3. `cond(state)` **may not** inspect:
   - `(vibhakti, vacana)` or `(lakāra, puruṣa, vacana)` coordinates
   - Surface Devanāgarī spelling of any Term
   - The target form being derived
   - Any file in `data/reference/`
   - Kaumudī headings, ordering, or "prakaraṇa" labels

A static test (`tests/constitutional/test_no_vibhakti_read_in_cond.py`)
refuses commits that violate rule (3).

---

## Article 3 — Aṣṭādhyāyī Kram

Rules are scheduled in Aṣṭādhyāyī order, modified only by:

1. **Tripāḍī asiddha gate** (8.2.1): sūtras 8.2.1 through 8.4.68 are
   invisible to all prior sūtras. The gate is implemented in `engine/gates.py`.
2. **Rajpopat's SOI/DOI** (resolver.py): when two sūtras both fire on the
   same state, specificity-of-input and direction-of-information resolve
   the conflict — not pāda number.
3. **Pratiṣedha** (explicit blocking): a PRATISHEDHA sūtra adds IDs to
   `state.blocked_sutras`. The dispatcher honours this before firing.

**No Siddhānta-Kaumudī ordering is ever consulted.** If a sūtra must fire
"early" for a derivation to succeed, that is the fault of the recipe, not
the engine.

---

## Article 4 — Anuvṛtti is Baked In

Every sūtra's `text_slp1` / `text_dev` is the **full, anuvṛtti-complete**
form. The engine never computes anuvṛtti at runtime.

Example: sūtra 1.3.3 (`halantyam`) is stored as
`"hal antyam upadeśe 'n it"` — because 1.3.2's `upadeśe` and `it` carry
over and are part of the executable rule.

The field `anuvṛtti_from` on `SutraRecord` is **metadata only** — it
tells scholars which earlier sūtras contributed terms, but the engine
does not read it.

This eliminates an entire class of v2 bugs where anuvṛtti-computation
disagreed between the engine and the Prathama-āvṛtti.

---

## Article 5 — Red Flag Invariants

Enforced by `engine/r1_check.py` at every rule application:

- **R1.** A VIDHI / NIYAMA / NIPATANA whose `cond(state)` returned True but
  whose execution left `render(state) == render(state_before)` is a **bug**.
  The dispatcher raises `R1Violation`. Do not suppress by editing the check.
- **R2.** A SAMJNA that fires but does not add an entry to `state.samjna_registry`
  is a bug.
- **R3.** A PARIBHASHA that fires but does not set a gate is a bug.
- **R4.** An ADHIKARA whose scope does not contain the currently-firing
  sūtra ID, yet which is on the stack, is a bug (gate leak).
- **R5.** A rule whose `cond` reads from `data/reference/` is a bug.

---

## Article 6 — Input / Reference Firewall

```
┌─────────────────────┐           ┌─────────────────────┐
│   data/inputs/*     │ ───read── │   engine, sutras,   │
│  (upadeśa, maheś.   │           │    phonology, ...   │
│   sutras, gaṇa ...) │           │                     │
└─────────────────────┘           └────────┬────────────┘
                                           │
                                           │   produces
                                           ▼
                                  ┌─────────────────────┐
                                  │  State.trace +       │
                                  │  rendered surface    │
                                  └────────┬────────────┘
                                           │
                                           │   compared by
                                           ▼
┌─────────────────────┐           ┌─────────────────────┐
│  data/reference/*   │ ◀──read── │    tests/*, tools/* │
│   (gold paradigms,  │           │  (NOT the engine)   │
│  Kāśikā examples)   │           │                     │
└─────────────────────┘           └─────────────────────┘
```

`data/reference/` is readable only by `tests/` and `tools/`. A
constitutional test refuses any engine/sūtra import that references
`data/reference/`.

---

## Article 7 — No Rule Bundles

Every sūtra is one file under `sutras/adhyaya_X/pada_Y/sutra_X_Y_Z.py`.

**Forbidden:**
- Modules like `anga_guna_rules.py`, `tinanta_rules.py`, `vikarana_rules.py`
  that bundle many rules in one file.
- Helper functions that apply multiple sūtras without routing through
  `apply_rule()`.
- Inline rule dicts inside `derive_*` pipelines.

A sūtra file has **exactly one** `SutraRecord` and **exactly one** pair
of `cond(state) / act(state)` functions.

---

## Article 8 — Prakriyā is a Test, Not a Target

The 24 `रामः … रामेषु` paradigm cells, the seven `भवति … भवन्ति`
tiṅanta cells, and any future cells exist to **stress the engine**.

- When the engine passes a cell, that is evidence of correctness.
- When the engine fails a cell, we fix the *sūtra file* or the *recipe* —
  **never** the dispatcher, the resolver, the gates, or the SutraType
  executors.
- If a cell reveals a genuine engine defect, we write a `tests/regression/`
  test first, then fix the engine, then re-run all tests.

---

## Article 9 — Backward Testability

Every forward derivation must be **replayable**: given
`State.trace`, `tools/replay_trace.py` reconstructs the final form by
re-applying each listed sūtra to the initial state, and asserts equality
with the originally-recorded final form.

This is a defence against silent trace corruption and against hidden
engine paths that bypass `apply_rule()`.

---

## Article 10 — Amendment Procedure

These ten Articles are amended only by:
1. Opening `docs/AMENDMENT_<N>.md` with the proposed change and rationale.
2. Passing every constitutional, forward, backward, and regression test
   with the proposed change applied to a branch.
3. Explicit written acceptance in the amendment file.

No silent edits. The Constitution's own change history is itself
auditable.
