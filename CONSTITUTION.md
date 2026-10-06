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

The list is closed. A sūtra that does not fit one type cleanly is never given an
eleventh type. Its extra behaviour goes on the record as a class grounded in a
rule (e.g. `ArthaNirdesha`, Art. 20).

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
2. **Vipratipatti ladder** (Art. 21 / `engine/resolver.py`): when two sūtras
   both fire on the same state, the winner is decided by declared relations
   and Pāṇini's own devices (asiddhatva, pratiṣedha, apavāda, *para* 1.4.2).
   An unnamed heuristic (including Rajpopat SOI) may propose, never decide.
3. **Pratiṣedha** (explicit blocking): a PRATISHEDHA sūtra adds IDs to
   `state.blocked_sutras`. The dispatcher honours this before firing.

**No Siddhānta-Kaumudī ordering is ever consulted.** If a sūtra must fire
"early" for a derivation to succeed, that is the fault of the recipe, not
the engine.

---

## Article 4 — Anuvṛtti is Baked In

> Amended by **AMENDMENT 20** (see `docs/AMENDMENT_20.md`).

Every sūtra record carries two texts:

- `text_slp1` / `text_dev` — the **mūla pāṭha** as in ashtadhyayi.com `data.txt` (T0).
- `samagra_slp1` / `samagra_dev` — the **full, anuvṛtti-complete** sentence
  (ashtadhyayi.com `ss`; where that is empty, adhikāra + padas + anuvṛtti padas,
  marked "composed" in the file).

The engine never computes anuvṛtti at runtime and reads neither text.

Example: sūtra 1.3.3 has `text_slp1 = "halantyam"` and
`samagra_slp1 = "upadeSe antyam hal it"` — because 1.3.2's `upadeśe` and `it`
carry over and are part of the executable rule.

**§2 Anunāsika is not anusvāra.** ँ is an `anunasika` tag on the vowel it is
written on (SLP1 `~` right after that vowel; `~` after a consonant is that
consonant's anunāsika inherent `a`: `han~` = हनँ). ं is the varṇa `M`. No code
path may merge them — 1.3.2 उपदेशेऽजनुनासिक इत् depends on the difference.

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

These **twenty-three** Articles (numbered 0 through 22) are amended only by:
1. Opening `docs/AMENDMENT_<N>.md` with the proposed change and rationale.
2. Passing every constitutional, forward, backward, and regression test
   with the proposed change applied to a branch.
3. Explicit written acceptance in the amendment file.

No silent edits. The Constitution's own change history is itself
auditable.

---

## Article 11 — Sūtra Interaction Graph (SIG) and uniform telemetry

**Role in architecture:** the engine maintains a **Sūtra Interaction
Graph (SIG)**: a chronological, rule-by-rule record of how derivations
traverse the sūtra registry. **Global** hooks (e.g. `ContextVar` in
`engine/telemetry.py`) and downstream tooling depend on a single, reliable
stream of sūtra applications.

**Strict law (non-optional):** all morphological transformations and every
sūtra application that affects `State` / `Term` as part of a Pāṇinian
**derivation** MUST be routed **exclusively** through
`engine.dispatcher.apply_rule`. **Direct mutation** of `State` or
`Term` to simulate a sūtra, or to apply phonological/operational
effects that should go through a registered sūtra’s `cond` / `act`,
is **forbidden** outside of `apply_rule`, except for purely structural
book-keeping in pipelines that does **not** stand in for a sūtra’s work
and is recorded in `State.trace` in a way that cannot be mistaken for
an applied rule. This ensures **100%** of rule-driven steps participate
in the SIG and in `notify_apply_rule_end` (and any other dispatcher-level
observers) without ad-hoc, per-pipeline hook wiring.

**Corollary:** the executors in `engine/executors/*` are invoked only from
`apply_rule` (the dispatcher is the only importer). Pipelines and recipes
call `apply_rule(sutra_id, state, …)`; they do not call `exec_*` directly.

---

## Article 12 — Fullest valid sūtra path; no duplicate shortcuts

When moving a derivation from **state A** to **state B** (e.g. prātipadika →
pada, or aṅga+pratyaya → surface), the implementation must seek the
**fullest** *śāstrīya* path that the Aṣṭādhyāyī admits through the engine —
**not** the smallest patch of one or two sūtras that happens to print the
target string.

1. **Rule-based and blind (Articles 2–3, 6–7, 11).** Every *vidhi* step
   must be a real `SutraRecord` with `cond(state)` satisfied from phonemic
   / saṃjñā / *upadeśa* / adhikāra signals. No *recipe* may read
   `data/reference/`, gold paradigms, or “expected Devanāgarī” in order to
   **choose** which sūtra fires. Shortcuts that **bypass** `apply_rule` for
   morphological work forbidden by **Article 11** remain **forbidden**.

2. **Prefer a dense, valid trace over a thin hack.** If two designs both
   produce a correct surface but one **skips** sūtra blocks that a comparable
   *śāstrīya* *prayoga* of the same *class* normally traverses
   (saṃjñā, adhikāra, *it*‑prakaraṇa, aṅgakārya, sandhi) **without**
   a pratisedha, optional-path, or tripāḍī *asiddhatva* account, the thinner
   design is **suspect**. Extend **sūtra** *cond* / **recipe** *order* so
   the trace reflects the **longer** *legitimate* application sequence —
   the one a scholar could still justify line-by-line (Article 0), not a
   Kaumudī *short circuit* (Article 3). This does **not** mean “maximize
   arbitrary rule count”: pratishedha, *asiddha*, and *anarthaka*
   *prayoga* exclusions still apply; **never** add spurious sūtra fires.

3. **No duplicate or forked *prakriyā* for the same *locus*.** The same
   *prayoga* class (e.g. a given *prātipadika* + *sup* paradigm) should use
   **one** canonical pipeline entry (e.g. a single `derive_*` for that
   stem) so all cells share the **same** rule spine unless a **documented**
   *vibhāṣā* / *śāstrīya* *choice* actually forks (Article 1). Ad hoc
   copy-paste recipes for the same derivation are **duplication** and
   complicate **SIG** audit (Article 11).

4. **Change policy.** If a “shortcut” is removed and more sūtras apply, or
   if a duplicate pipeline is merged into a canonical one, this is
   *progression toward* Article 12, not a regression, **provided** `cond`
   truth and **Article 3** order are preserved. Update
   `tests/regression/*` (including SIG baselines where used) as for any
   intentional trace change (Article 8, Article 9).

---

## Article 13 — Universal sūtra implementation architecture

**Goal:** every **VIDHI** / **SAMJNA** / **NIYAMA** (executable sūtra) should
be able to fire because **linguistic** predicates on `State` / `Term` are
true — not because a recipe flipped an ad hoc `state.meta["…_arm"]` switch.

1. **No new demo scaffolding in sūtra `cond` / `act`.** Do not add
   `state.meta` keys whose only purpose is to enable a single pipeline
   (`*_arm`, `corrected_v2_*`, prakriya ids, etc.) inside
   `sutras/adhyaya_*/pada_*/sutra_*.py`. Existing legacy uses are **technical
   debt** to be removed when that file is next refactored for behaviour.

2. **Pipelines remain the scheduler only (Article 7).** They call
   `apply_rule` and may set meta for **non-morphological** sequencing where
   the CONSTITUTION already permits it — but if a sūtra’s `cond` would read
   `False` without such a key, the fix belongs in **tags**, prior **SAMJNA**
   steps, **registry** entries, or **Term**-local completion flags — not in a
   permanent bypass arm.

3. **Enumerations and idempotency.** Dhātu lists or affix classes **named in
   the sūtra** (or loaded once from kosha data at import) live in
   **module-level** `frozenset`s or helpers. Per-rule completion flags on a
   `Term` use names derived from the **sūtra id** (e.g. `6_4_24_…_done`), not
   from demo ids.

4. **Detail and checklist.** See `docs/SUTRA_UNIVERSAL_RULE_ARCHITECTURE.md`.
   Cursor applies an additional project rule under
   `.cursor/rules/panini-sutra-universal-architecture.mdc` to matching paths.

**Relation to Article 2.** Article 2 still governs what `cond` may *read*.
Article 13 adds **how** new implementations should shape those reads: prefer
structural tags and registry over recipe flags; prefer phonological
predicates over surface fingerprints of a single example form.

### Article 13 §1 — Hardened by AMENDMENT 14

No file under `sutras/` may be committed if its `cond()` reads
`state.meta[K]` where `K` ends in `_arm` or matches the regex
`(?i)(corrected_v[0-9]+|P[0-9]+(_|$))`. The constitutional test
`tests/constitutional/test_no_new_arm_gates.py` enforces this on a
strict-additive basis: existing `_arm` reads are grandfathered and
counted; any commit increasing the count fails CI. Migrations that
*decrease* the count are always allowed.

Pipelines under `pipelines/` and orchestrators under `core/` may still
set `_arm` keys during the migration period, but each new write must
be accompanied by a removal in the same commit (net additive: zero or
negative).

---

## Article 14 — Authoritative Sources and Citation

> Added by **AMENDMENT 14** (see `docs/AMENDMENT_14.md`).

Every sūtra file under `sutras/adhyaya_*/pada_*/sutra_*.py` whose
`cond()` or `act()` makes a non-trivial linguistic decision **must**
name the textual source that justifies that decision. The
authoritative source roster is defined in `audit_cursor.md` § 0
and `audit_claude.md` § A. The roster names **what may be cited** in a
docstring. It does **not** decide what a rule means — that is Art. 22.

**Minimum citation** in each sūtra file's module docstring:

1. **Source #1** — ashtadhyayi.com row index (e.g. `i = 64003` for
   sūtra 6.4.3) — for `text_dev`, `text_slp1`, `padaccheda_dev`,
   `anuvritti_from`, `sutra_type`.
2. **Source #2** — Kāśikā Vṛtti udāharaṇa (and pratyudāharaṇa where
   applicable), quoted in Devanāgarī.
3. **Cross-validation** — either (a) a note that the surface output
   was verified against Vidyut (`github.com/ambuda-org/vidyut`) and/or
   Saṃsādhanī (`sanskrit.uohyd.ac.in/scl/`), OR (b) a regression-test
   reference under `tests/regression/` that pins the surface.

**Citation source precedence:**

```
1. ashtadhyayi.com data repo (sūtra pāṭha, padaccheda, anuvṛtti)
2. Kāśikā Vṛtti (Vāmana + Jayāditya)
3. Mahābhāṣya (Patañjali) + Pradīpa + Uddyota
4. Siddhānta-Kaumudī + Tattva-bodhinī  ← cross-reference only;
   never drives engine ordering (Art. 3)
5. Laghu-Siddhānta-Kaumudī
6. Prakriyā-Kaumudī / Prakriyā-Sarvasva
```

Tier 2 (paribhāṣā: Paribhāṣenduśekhara, Vyāḍi, Śākaṭāyana;
ancillaries: Liṅgānuśāsana, Phiṭ-sūtras, Uṇādi-sūtras), Tier 3
(Dhātupāṭha, Gaṇapāṭha), Tier 4 (Vidyut, Saṃsādhanī, Sanskrit
Heritage, Sanskrit Abhyas), and Tier 5 (Cardona, Kiparsky, Sharma, Vasu, Joshi &
Roodbergen) are cited as supporting evidence per the full roster.

**Forbidden as sources:** unverified blog posts, LLM output without
independent verification, Wikipedia (use to locate primary then cite
primary), PDFs without edition lineage, surface-form transliterators
as a source of rule logic.

**Conflict resolution:** When two roster sources disagree about *what a
rule means*, the prāmāṇya ladder (Art. 22) decides. The numbered roster
only says what may be quoted. If the disagreement is notable, the
resolution is documented in `docs/AMENDMENT_<N>.md` and the sūtra
docstring links to that amendment. Runtime conflict between sūtras is
Art. 21, never this list.

**Article 12 reinforcement (added by AMENDMENT 14):** No new file
under `pipelines/` may carry the substring `_corrected_` or
`_corrected_P` in its name. Constitutional test
`tests/constitutional/test_no_corrected_pipelines.py` refuses such
commits. The substring implies the canonical pipeline is wrong; fix
the canonical pipeline instead.

**Article 8 §2 clarification (added by AMENDMENT 14):** The web UI's
default trace filter shows only `APPLIED` (form-changing) rows.
`AUDIT` and `APPLIED_VACUOUS` rows remain recorded by the engine
and available via a "विस्तरः" toggle. Their absence from the default
view is **not** a regression. Engine trace completeness is verified
by `tests/regression/`, not by the UI default.

**Constitutional test added under this Article:**
`tests/constitutional/test_sutra_source_citation.py` refuses commits
that touch a sūtra file without updating the citation fields named
above.

---

## Article 15 — Conflict is declared, never engineered

> Added by **AMENDMENT 15** (see `docs/AMENDMENT_15.md`).

A sūtra's `cond()` describes **its own** condition as Pāṇini states it. It may
never be narrowed to avoid another sūtra.

When two sūtras claim the same position, the loser is determined by a declared
relation — `blocks_sutra_ids` (प्रतिषेध), `apavada_of` (अपवाद), adhikāra scope, or
stratum — and the winner is chosen by **Art. 21 Ladder 1**, whose floor is
**1.4.2 विप्रतिषेधे परं कार्यम्**. The losing sūtra appears in the trace as
`BLOCKED`, naming the rule that beat it and why. A specificity score may
*propose* a winner; it may not *be* one.

An utsarga that excludes a case in order to let an apavāda through is a
constitutional violation **even when every test passes**, because the derivation
then records a reason Pāṇini did not give.

*Worked example (the template):* 6.1.102 प्रथमयोः पूर्वसवर्णः had narrowed itself
to i/u-final aṅgas so that रामौ would come out right; 6.1.104 नादिचि, the निषेध
that actually does that work, was a stub typed `VIDHI` with no blocks. Repaired
2026-09-15: 6.1.102 claims every अक्-final aṅga, 6.1.104 is a `PRATISHEDHA`
blocking it, and the trace shows APPLIED → BLOCKED → वृद्धि.

*Enforcement:* `tests/constitutional/test_no_engineered_conflict.py`
(scheduled: ROADMAP Phase B3).

---

## Article 16 — Coverage is firing, not registration

> Added by **AMENDMENT 15**.

A sūtra counts as **implemented** only when all four hold:

1. it is **invoked** by at least one derivation in the test suite;
2. it **changes the state**, or is explicitly `r1_form_identity_exempt`;
3. it carries a **citation** to sūtra text and to the source that justifies its
   predicate (Art. 14);
4. it carries **≥ 3 positive and ≥ 2 negative tests** — "must not fire here" is
   half of what a sūtra means.

Everything else is **registered**, not implemented, and the two counts are
reported separately. No document, README, or interface may present the
registered count as coverage.

*Enforcement:* `engine/coverage.py` + `tests/constitutional/test_coverage_is_honest.py`
(in force). The ≥3/≥2 split lands with `sutra_lint` (ROADMAP Phase A2).

---

## Article 17 — Analysis proposes, generation verifies

> Added by **AMENDMENT 15**.

The engine has exactly one rule base, and it runs in one direction: generation.

Analysis (pada-cheda, morphological identification, kāraka labelling) may only
**propose candidates**. A candidate becomes an answer only when the forward
engine, run on that candidate, reproduces the input string exactly. The accepted
analysis ships with that forward derivation.

No reverse rule may be written. Sandhi may be *inverted* mechanically as an
over-generating candidate source; morphology may be *enumerated* into an index.
Neither is a rule.

**The form index is a cache, never a grammar.** Any table of generated forms is
a build artifact: regenerated from the engine, never hand-edited, re-derived in
CI. A form in the index that the engine can no longer derive is a build failure.
The engine never consults the index to derive — an engine that reads its own
cache to produce a derivation has become the lookup table Art. 0 forbids.

*Enforcement:* `tests/constitutional/test_index_is_regenerable.py`,
`test_no_reverse_rules.py` (scheduled: ROADMAP Phase E3/E5).

---

## Article 18 — A gap is an output

> Added by **AMENDMENT 15**.

When the engine cannot derive or cannot analyse, it must say **what is missing**,
naming the sūtra, the dhātu, or the lexical entry that would close the gap.
Silence is a bug.

An unrecognised word is a gap, never a guess. No statistical fallback, no
"probably a noun", no partial form presented as a derivation. A closed world
that states its boundary is worth more to a scholar than an open one that
improvises.

Gaps are emitted in the trace and aggregated into a frequency-ranked worklist;
that list, not intuition, orders implementation.

*Enforcement:* `engine/gaps.py` (scheduled: ROADMAP Phase A3).

---

## Article 19 — We do not grade our own homework

> Added by **AMENDMENT 15**.

Correctness claims are settled against sources outside this repository:
attested usage from the corpus, the classical commentaries, and at least one
independent implementation.

Every release publishes its agreement rate and the commands that reproduce it.
A disagreement with an external oracle is a **work item**, never a verdict in
either direction: the other implementation may be wrong, and the investigation
is the deliverable.

No number may appear in the README that a reader cannot regenerate with one
command.

*Enforcement:* `bench/` differential runner (scheduled: ROADMAP Phase A4).

---

## Article 20 — अर्थनिर्देश: meaning-assigning heads reach both ways

> Added by **AMENDMENT 16** (see `docs/AMENDMENT_16.md`).

Some sūtras state the *meaning* in which affixes are taught rather than an
operation. The Kāśikā marks them अर्थनिर्देश, which are connected "पूर्वैरुत्तरैश्च
प्रत्ययैः" — with the affixes taught before them and after them. The template is
4.1.92 तस्यापत्यम्.

1. Such a sūtra stays `ADHIKARA` (Art. 1). Its forward reach *is* adhikāra, by
   **1.3.11 स्वरितेनाधिकारः**.
2. Its backward reach is declared with `SutraRecord.artha_nirdesha =
   ArthaNirdesha(artha, artha_dev, purva_from, source)`. The frame it opens covers
   `purva_from` … `adhikara_scope[1]` and carries `artha`. Affix sūtras read the
   meaning from that frame, never from a recipe flag.
3. Backward reach is granted **only** when a vṛtti states it. The `source` field
   quotes that sentence, and the sūtra docstring repeats it verbatim (Art. 14).
   A site taxonomy label (e.g. `data.txt` type `AD`) is never sufficient.
4. The forward end is the end of the section the meaning governs, as the
   commentaries fix it (4.1.92 → 4.1.178), not a later adhikāra's end.

*Enforcement:* `tests/constitutional/test_artha_nirdesha.py`;
`tests/unit/test_adhikara_gate_scope.py`.

---

## Article 21 — Rule conflict is resolved by Ladder 1, in order

> Added by **AMENDMENT 17** (see `docs/AMENDMENT_17.md`).

When two or more sūtras claim the same position, the winner is decided by
Ladder 1, in order: pāṭha/anuvṛtti → asiddhatva → pratiṣedha → nipātana
freeze → **vikalpa stop (fork)** → nitya → antaraṅga → apavāda → para
(1.4.2) → pūrva → sakṛdgati → jñāpaka.

The executable meta-rule book is Nāgeśa's **परिभाषेन्दुशेखर**, vendored as
`data/inputs/paribhasha_shekhara.json` (full 133-paribhāṣā pāṭha from
ashtadhyayi-com/data). A decision names the PŚ number it implements. Ārthika
granthas (वाक्यपदीय, वैयाकरणभूषणसार, परमलघुमञ्जूषा) and the
Laghuśabdenduśekhara **do not pick a runtime winner**.

Every layer is either **modelled** or declared `not_modelled`. A conflict that
would turn on an unmodelled layer is recorded as an Art. 18 gap naming the
layer — it is never silently settled by the layer below.

**No layer may be an unnamed heuristic.** Rajpopat SOI may *propose* an
undeclared apavāda; it may not *be* the winner. A proposed apavāda must be
promoted to `apavada_of` or recorded as an amendment.

*Enforcement:* `tests/constitutional/test_vipratisedha_resolver.py`.

---

## Article 22 — Prāmāṇya (which text wins) and declared school

> Added by **AMENDMENT 17**; T7 widened by **AMENDMENT 18**.

Art. 14 is the **evidence roster** (what a docstring may cite). This article
is the **meaning ladder**. It is used when a human writes a sūtra file; it is
never an input to `cond()`.

| # | Authority | Notes |
|---|---|---|
| T0 | pāṭha | ashtadhyayi.com data; Bhāṣya-supported when MSS differ |
| T1 | वार्त्तिक (Kātyāyana) | śāstra, not commentary |
| T2 | महाभाष्य (Patañjali) | ceiling of interpretation |
| T3 | प्रदीप + उद्योत | whose reading of the Bhāṣya |
| T4 | परिभाषेन्दुशेखर | meta-rules — this is also Art. 21's runtime book |
| T5 | लघुशब्देन्दुशेखर | SK-level prakriyā disputes; zero kram authority (Art. 3) |
| T6 | SK cluster | which rules tradition cites together; zero kram authority |
| T7 | Kāśikā → Nyāsa → Padamañjarī; **ashtadhyayi.com sūtra data incl. `sutra_prayogas` examples** (AMENDMENT 18) | udāharaṇa; equal evidence to Prathamāvṛtti/Kāśikā; T2 wins on conflict |
| T8 | प्रक्रिया primers | pedagogical; no deciding authority |
| T9 | modern scholarship | zero prāmāṇya; modelling only (Kiparsky on strata) |
| T10 | oracles | Art. 19: can prove wrong, never prove right |

**Declared school:** this engine is **Nāgeśīya-navya-vyākaraṇa**. Where the
tradition is divided, T4–T5 decide; where Nāgeśa is silent or contested, revert
to T2. A departure is an amendment, cited from the sūtra docstring.

**Domain-limited (not vipratipatti):** धातुपाठ, गणपाठ, उणादि, फिट्सूत्र,
लिङ्गानुशासन, पाणिनीयशिक्षा; and the ārthika granthas वाक्यपदीयम्,
वैयाकरणभूषणसारः, परमलघुमञ्जूषा (`data/inputs/grantha_catalog.json`).

An amendment in this repository is the audit trail of a Ladder 2 decision, not
a higher pramāṇa than T2.

**Digitised sources:** the pāṭha and commentaries are read from
[`github.com/ashtadhyayi-com/data`](https://github.com/ashtadhyayi-com/data)
(ashtadhyayi.com's own data repo). The RKMVU Grammar site
(`cs.rkmvu.ac.in/~tamal/learn/sanskrit/Grammar/site`) is a learner front-end
over that corpus plus Vidyut; it is not a second pāṭha and it is never copied
into `cond()`. Sanskrit Abhyas ([`sanskritabhyas.in/en`](https://sanskritabhyas.in/en))
is an independent अभ्यास (declension, conjugation, kṛt, taddhita, nāmadhātu,
sandhi); it is pedagogical surface gold (Art. 19), not a pāṭha, and never
copied into `cond()`. See `data/inputs/grantha_catalog.json`.

*Enforcement:* `tests/constitutional/test_vipratisedha_resolver.py`
(`runtime_granthas` is PŚ only; LŚ excerpts are quoted, not executed).
