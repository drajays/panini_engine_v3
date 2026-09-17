# Pāṇini Engine — architecture, process, roadmap

*Written 2026-09-15. Every number below was measured on this repository today; §1 says how to
reproduce each one.*

**Companion documents:** [`CONSTITUTION.md`](CONSTITUTION.md) (law) · [`docs/AMENDMENT_15.md`](docs/AMENDMENT_15.md) (Articles 15–19, proposed — the law this document assumes) · [`final_plan.md`](final_plan.md) (v4 engine internals).

**What this document is.** The program: what "best" means in checkable terms, what the machine
must become, the gates that keep quality from eroding, and the order of work.

**What it is not.** It does not replace [`CONSTITUTION.md`](CONSTITUTION.md) (the law — unchanged)
or [`final_plan.md`](final_plan.md) (the v4 engine-internals plan — still valid; it becomes
Phase A here). Three documents, three jobs: law · engine internals · program.

---

## 0. The one architectural decision

There are two codebases. They must become one.

| | `panini_engine_v3` (this repo) | `~/read` (panini-engine) |
|---|---|---|
| morphology | subanta · tiṅanta · kṛdanta · taddhita · samāsa | none (sandhi only) |
| tests | 19,117 | 141 |
| a rule is | Python `cond()`/`act()` per sūtra | a `RuleSpec` — **data** |
| rule order | hand-written ID lists, 187 pipelines | **1.4.2 executed**; loser recorded |
| conflict | utsarga narrowed by hand | `apavada_of` declared |
| asiddha | `tripadi_zone` flag | `written_by` ledger, provably loop-free |
| unmodelled | silent `SKIPPED` | `gap:` naming the missing sūtra |
| corpus | text inside records | 3,983 records, anuvṛtti/adhikāra pointers, **1,712 attested usages** |

**Decision: this repo is the trunk. `~/read` supplies the metatheory, the corpus, and the kit.**
Rebuilding morphology from 23 sūtras would discard years of verified work; reproducing the
metatheory by hand — as was done for 6.1.104 on 2026-09-15 — does not scale past a few rules.
`~/read` continues as (a) the reference implementation of each mechanism before it is ported,
(b) the corpus source, (c) the installable skill/agent/hook kit.

---

## 1. Measured baseline (2026-09-15)

| metric | value | how it was measured |
|---|---|---|
| sūtra records registered | 3,985 | `len(SUTRA_REGISTRY)` |
| `coverage_report()` claim | 3,985 implemented · 0 stubs · **100 %** | `coverage_report(SUTRA_REGISTRY)` |
| **sūtras ever invoked** across the whole suite | **569** | `apply_rule` wrapper over 19,117 tests |
| **sūtras that ever change the tape** | **296 (7.4 %)** | same run, comparing `flat_slp1()` before/after |
| sūtra files carrying the stub gloss `(सूत्रम् X)` | 2,418 (61 %) | `grep -rl 'why_dev.*(सूत्रम्' sutras/` |
| files whose `cond` is only `samhita_gate_eligible(...)` | 633 | grep |
| BLOCKED steps in the 364 shipped derivations | 24 | `docs/data/traces/` (dumped before the 6.1.104 fix) |
| tests | 19,117 passing, 1 skipped | `pytest -q` |

Read those rows together and the situation is exact:

1. **The coverage number is gamed** — not dishonestly, but structurally. A record counts as
   "implemented" because it exists, not because it does anything. The true operational rule base
   is **296**, and every plan must be written against that number.
2. **The paribhāṣā layer is nearly inert.** 24 blocks in 364 derivations. Rule conflicts are
   being resolved by editing conditions instead of by Pāṇini's own metarules — which is how
   6.1.102 came to narrow itself to dodge नादिचि.
3. **`final_plan.md` Phase 4 (the autonomous loop) is blocked for exactly this reason.** The
   resolver has no principled basis to choose — `_default_specificity()` counts declared fields.
   Pāṇini's answer is विप्रतिषेधे परं कार्यम्, अपवाद, and असिद्धत्व. Until those execute, the loop
   cannot pick rules, and no amount of scheduler tuning will fix it.

**The work is conversion, not construction.** The forms are already derived. What is missing is
that the machine derives them *for Pāṇini's reasons*, and that we can prove it.

---

## 2. What "best engine ever made" means (five falsifiable claims)

A claim nobody can check is marketing. These are checkable by anyone on a clean checkout.

| # | claim | check |
|---|---|---|
| 1 | **Most derivations correct** | differential agreement vs Vidyut / Heritage / Samsaadhanii on published sets; accuracy on the 1,712 attested prayogas |
| 2 | **Deepest *traced* coverage** | a rule counts only if it fires, moves the state, and has a cited test — enforced by `sutra_lint`, not by a register |
| 3 | **Both directions** | generation and analysis (surface → split → stem → vibhakti/kāraka) held to one standard |
| 4 | **Explainable** | every step: sūtra text, anuvṛtti-resolved reading, gloss, commentary citation, the rule it beat and why, counterfactuals |
| 5 | **Reproducible** | one command regenerates every number in the README |

The headline metric is **not sūtra count**. It is **token coverage on running text**: the fraction
of words in a real corpus the engine can derive *and explain*. Sūtra count is an input.

---

## 3. Architecture — the machine Pāṇini would recognise

```
phonology/      varṇa, pratyāhāra, savarṇa, joiner              (foundation — keep)
core/           transliteration, trace view, canonical blocks
engine/
  state.py      tape: Terms, tags, meta, provenance             (keep)
  vocabulary/   NEW  ~50 typed operations: ādeśa · lopa · āgama · dvitva · ekādeśa ·
                guṇa/vṛddhi/savarṇa-dīrgha · samprasāraṇa · ṇatva/ṣatva · it-lopa …
  paribhasha/   NEW  the metatheory, executable:
                  1.4.2 vipratiṣedhe paraṃ kāryam — later wins, loser recorded
                  apavāda graph — declared, never hand-narrowed
                  asiddha strata (8.2.1 / 6.4.22 / 6.1.86) — a visibility matrix, not a flag
                  vibhāṣā — forks the state; every branch is an output
                  1.1.56 sthānivadbhāva — already present, made uniform
  scheduler.py  candidate selection from the rule set (no pipeline lists)
  resolver.py   decides by the paribhāṣā layer; records why
  gaps.py       NEW  an unmodelled context is an output naming the missing sūtra
sutras/         rule records — migrating from cond/act code toward declarative data
pipelines/      shrinking: recipes become tests, not the engine
bench/          NEW  differential runners, form grids, report card
analysis/       LATER  sandhi lattice · splitter · morphological analyser · kāraka
```

Five design rules that keep it honest as it grows:

- **A rule is data with a citation.** Scope from the adhikāra graph, declarative conditions, an
  operation from the vocabulary, optionality, stratum, citation, tests. New *sūtras* must never
  add engine branches; new *mechanisms* may — and the mechanism budget is finite (§4).
- **A rule may never narrow itself to avoid a conflict.** If another sūtra should win, say so:
  `apavada_of`, `blocks`, or the stratum. This is the single rule that would have prevented the
  6.1.102 defect, and it is the one most easily broken under deadline.
- **No rule without a negative test.** "Must not fire here" is half of what a sūtra means.
- **Gaps are outputs.** The engine must say *which sūtra is missing*, turning the roadmap into a
  queryable, frequency-ranked list instead of 6,496 silent SKIPPEDs.
- **Provenance is load-bearing.** रामः + अपि → रामोऽपि but पुनर् + अपि → पुनर् अपि. Same sound,
  different history. Preserve `Term.meta` through every operation.

---

## 4. Process — what makes shortcuts impossible

Quality is not a virtue here; it is a set of gates that fail loudly.

**Per-rule gate** (`sutra_lint`, wired into the PostToolUse hook):
a rule must cite corpus text (never text typed from memory), fire on a real linguistic condition
(no arm flags), move the state or declare itself R1-exempt, carry ≥3 positive and ≥2 negative
tests, and declare its conflicts. A rule failing any of these is not "partially done" — it is not
a rule, and `coverage` must not count it.

**Per-batch gate** — batches are 10–30 sūtras of one prakaraṇa, so a regression has a short bisect
path. If a batch needs **more than one new mechanism, stop and design the mechanism first.** That
is the whole difference between 50 primitives and 3,983 special cases.

**Per-merge gate** — `bench --regress`: agreement and token coverage may not drop. Never grade our
own homework: the oracle is Vidyut (≈2,000 sūtras, per-step traces), Heritage/Samsaadhanii where
forms overlap, and the 1,712 attested prayogas. A disagreement is a ranked work item, not a verdict.

**Per-session gate** — the audit hook refuses to end a session with a broken corpus or rule base.

**Authoring discipline** — a model may propose candidate rules and candidate tests; a model may
never produce a derivation or a form that enters the golden set. Every expectation is cited or
attested. A failing test is a bug in the rule, never in the expectation.

**Coverage that cannot be gamed** — replace `coverage_report()` with the measurement in §1: invoked,
moved, tested, cited. The number will fall from 3,985 to ~296 on the day it lands. That fall is the
most valuable single change in this document.

---

## 4.5 Both journeys: how analysis is built

The product this is for: paste a verse — दण्डः शास्ति प्रजाः सर्वा दण्ड एवाभिरक्षति — and get every
word split out, taken back to its root, and then derived forward again, each step citing its sūtra.

**Measured on this repo, 2026-09-15.** Of the five derivable words in that line, four already
generate correctly today: दण्डः · प्रजाः · सर्वाः · रक्षति. शास्ति fails — not for want of rules
(the adādi tiṅanta path has tests) but because `data/inputs/dhatupatha_upadesha.json` holds 986
roots of which **971 are gaṇa 1**; gaṇas 2–10 have 15 entries between them. And
`pipelines/patha_pipeline.py` already analyses by the right method — it generates every cell of
its lexicon and indexes the surfaces — but the lexicon is 28 stems, 451 forms, nominals only, and
it splits on whitespace.

So the gap to this product is **data and two mechanisms**, not a new engine.

### The rule that makes it tractable

> **Analysis proposes; generation verifies. There is never a reverse rule.**

Forward derivation is a relation (one-to-many, because vibhāṣā forks). Analysis is preimage
computation on that relation, and by blind search it is exponential. Two properties of the grammar
make it cheap, and they are different properties, so they get different machinery:

| layer | property | method |
|---|---|---|
| **morphology** (subanta · tiṅanta · kṛt · taddhita) | a lemma's paradigm is **finite** — 24 nominal cells, 9 × lakāra verbal cells | **enumerate**: generate every cell once, index surface → (lemma, features, derivation id). The analyser is a *cache of the generator*, so it can never disagree with the grammar. |
| **sandhi** (saṃhitā + tripādī) | a **local** relation over varṇa boundaries with bounded context | **invert**: compile to a finite-state transducer and run it backwards to get a lattice of candidate splits — over-generating on purpose. |
| **samāsa · derived stems** | unbounded (compounds nest) | recursive search over the same rule set, bounded by the lattice and the index. |

Every candidate that survives is then **re-generated forward and compared to the input string**.
That check is what licenses the answer — and it is also the teaching artifact, because the reverse
journey and the forward journey are then literally the same trace read in two directions.

### So yes — a database, under three conditions

The index is a real store, and it should be one: `sqlite3` is in the standard library, it is a
single file, it indexes a surface column in microseconds, and it needs no service. Scale only
forces a change of representation, not of design — `vidyut-kosha` holds tens of millions of forms
at roughly a byte each with a finite-state transducer, and that is the upgrade path if SQLite
stops fitting.

A row holds: surface (SLP1 and Devanāgarī) · lemma · features · **derivation id** · branch id ·
provenance. The derivation id is what makes the forward journey reproducible on demand instead of
stored — the trace is regenerated by the engine, never cached as text.

The three conditions are what keep it from becoming a second grammar:

1. **Generated, never authored.** No hand-edited rows, ever. The index is the graph of the
   generation function restricted to the lexicon.
2. **Regenerated in CI; drift is a build failure.** A form in the index the engine can no longer
   derive fails the build — that is the whole safety property.
3. **Never consulted to derive.** Lookup answers *"what could this be?"*; only the engine answers
   *"why is it this?"*. An engine that reads its own cache to produce a derivation has become the
   lookup table Article 0 forbids.

### Ambiguity is the product

For a learner, "सर्वाः is accusative plural feminine" is worth less than "सर्वाः could be X or Y;
it is Y here **because** it agrees with प्रजाः in liṅga, vacana and vibhakti, and because शास्ति
takes a कर्मन् (1.4.49)". So the analyser returns *ranked candidates with reasons*, never a single
answer, and the kāraka layer (1.4.23–55) plus agreement is what does the ranking.

The matching refusal: **an unknown word is a gap, never a guess.** No statistical fallback, no
"probably a noun". A closed world that says what it does not know is worth more to a scholar than
an open one that improvises.

## 5. Roadmap — sequential

Gates are binary. No phase starts before its predecessor's gate passes; inside a phase the steps
are ordered and each one is a session's work with a committed deliverable. Two clocks are reported
at every gate: **coverage** (implemented sūtras, Art. 16 sense) and **quality** (agreement, token
coverage). A phase that raises coverage and lowers quality is a failed phase.

### Phase A — Tell the truth
*No new grammar. Everything here is instrumentation, and everything after it depends on these
numbers being real.*

| # | deliverable | check |
|---|---|---|
| A1 | `coverage_report()` returns **registered** and **implemented** separately (invoked · moved · cited · tested); the honest number is committed | the number drops 3,985 → ~296 and the README is corrected |
| A2 ✅ | `sutra_lint` (`make lint`) — seven checks, three of them ratcheted; `why_not` explains any sūtra's fate in one derivation | ratchet frozen at arm-in-cond 33 · coordinate-in-cond 34 · **nisedha-as-vidhi 87**; enforced by `tests/constitutional/test_sutra_lint_ratchet.py` |
| A3 ✅ | `engine/gaps.py` + `make gaps` — three typed gap kinds, each dry-run verified | **281 gaps on the 417-cell grid**: 202 unscheduled (a rule whose cond was true, that would have changed the form, and that no pipeline asked) + 79 oracle disagreements. The dry-run filter is the whole design: without it the same grid reports 17,285 |
| A4 ✅ | `bench/` — 417-cell grid, Vidyut oracle committed as CSV so the comparison reproduces without installing it (`make bench`) | **81.1 % agreement (338/417)**: all 192 nominal cells agree; every one of the 79 disagreements is verbal — पा 45, कृ 25, गम् liṭ 6, नी liṭ 3. Pinned by `tests/regression/test_bench_agreement.py` |
| A5 ✅ | form index v1 — `engine/form_index.py` + `make index`: 986 dhātus × 5 lakāras × 9 and 72 stems × 24 | **45,936 forms · 35,426 distinct surfaces · 1,012 lemmas · 162 gaps**, built in 50 s; 300/300 sampled rows re-derive. The 10 MB SQLite file is a build artifact and is **not** committed — `data/index/manifest.json` is the committed fingerprint |

**Gate A: closed (2026-09-15).** A1–A5 all land, each with a command and a committed number:
`make coverage` · `make lint` · `make gaps` · `make bench` · `make index`.

    registered 3,985 · implemented 254 · agreement 81.1 % · gaps 281 · index 45,936 forms

The index already answers the analysis question the product needs: रामौ returns three readings
(prathamā, dvitīyā, sambodhana dual), नद्यौ returns three, and गच्छति returns none — the last being
the same gap the worklist ranks. **Phase B starts next**, with its 87 निषेधs and 202 unscheduled
rules already enumerated.

The two instruments corroborate, which is the strongest evidence either is measuring something
real: the 79 cells where Vidyut disagrees need exactly the rules the gap list ranks highest —
कृ needs 6.4.110 (*karuvas → kuruvas*), गम् liṭ needs 7.4.62 (*gamgama → jamgama*), पा needs
6.4.64 (*pAi → pi*). Phase B and Phase F now share one worklist.

### Phase B — Execute the metatheory
*The layer whose absence blocks everything else.*

| # | deliverable | check |
|---|---|---|
| B1 ✅ | the resolver's layers are **paribhāṣās, cited** from a vendored Paribhāṣenduśekhara slice: PŚ 38 पूर्वपरनित्यान्तरङ्गापवादानामुत्तरोत्तरं बलीयः is the ladder, PŚ 57 gives अपवाद, and *para* carries its Aṣṭādhyāyī id **from the data**, never from a literal in engine code | `Decision(winner, layer, reason_dev, losers)`; `record_decision()` writes each beaten rule into the trace as BLOCKED, naming the winner and the paribhāṣā. नित्य and अन्तरङ्ग are declared `not_modelled` rather than silently skipped |
| B2 | apavāda graph — `apavada_of` / `blocks_sutra_ids` seeded from the corpus's own pointers; declaration mandatory for new rules | no new rule merges without its conflicts declared |
| B3 | convert every engineered conflict; 6.1.104 ↔ 6.1.102 is the template | **Measured: none of the 87 निषेधs typed VIDHI ever fires, and the corpus names a block target for exactly one of them.** So this is not a sweep — it is 87 unimplemented rules with the wrong label, listed in `docs/NISEDHA_REVIEW.md` with text, padaccheda, adhikāra, Kāśikā udāharaṇa and a *proposed* target for a scholar to confirm. The lint now separates the dangerous case (a निषेध typed VIDHI that **fires** — an error, zero today) from the backlog (87, ratcheted) |
| B4 ✅ | `engine/strata.py` — असिद्धत्व as a matrix: **8.2.1** पूर्वत्रासिद्धम् (including *within* the tripāḍī, which the flag never modelled), **6.4.22** असिद्धवदत्राभात्, **6.1.86** षत्वतुकोरसिद्धः; ranges and their authority in `data/inputs/asiddha_strata.json` with a `not_modelled` list | the 8.2.66 ⇄ 8.3.34 cycle is now broken by an **asymmetry that can be stated**: 8.2.66 cannot see 8.3.34, 8.3.34 can see 8.2.66. `explain()` names the sūtra that hides it. The gate's bounds come from the matrix; wiring the loop's *visibility* to it belongs with Phase C |
| B5 ✅ | `engine/vikalpa.py` — `choose()` fixes the reading of named विभाषा rules and the dispatcher consults it (after a recipe step, before the sūtra's default); `explore()` replays a derivation down every combination and returns the distinct completed branches, bounded at 2⁶ | **6.4.38 वा ल्यपि यields आगत्य् and आगय् from the same pipeline, unmodified** — the policy is read by the dispatcher, so no pipeline has to be parameterised to be explored |

Phase B's worklist is now enumerated: `make lint` reports **87 sūtras whose padaccheda carries the
standalone word न — निषेधs typed VIDHI with no declared block**, exactly the shape 6.1.104 had. Only
*one* PRATISHEDHA in the registry has न in its padaccheda. Converting those 87 is the bulk of B3.

**Phase B status:** B1 ✅ B2 ✅ B3 → review (see the row) B4 ✅ B5 ✅.

**Gate B:** measured on `sig/suite_sig.json` — today the whole suite produces **229 BLOCKED
firings against 164,048 SKIPPED**, and only **six sūtras are ever blocked at all** (101 of those
blocks are the 6.1.102 repair of 2026-09-15). The gate is an order-of-magnitude rise in blocked
firings and in distinct blocking sūtras; no `cond` may contain a narrowing that belongs to another
sūtra; the autonomous-loop xfails turn green for laṭ kartari.

### Phase C — Dissolve the pipelines

| # | deliverable | check |
|---|---|---|
| C1 ✅ | `tools/autonomy_report.py` + `make autonomy` — drives scheduler → resolver → apply_rule with no recipe and classifies the outcome as **reached · halted · diverged** | **All 11 certain subanta cases halt at step 0: 126 candidates offered, 0 effective.** Two findings, both measured — see below |
| C2 | resolver decides using Phase B; `specificity_score` retired in favour of declared relations | no pipeline supplies ordering |
| C3 | `derive()` becomes a thin router onto the loop (`final_plan.md` Phase 4/5) | |
| C4 | the 187 pipelines become regression fixtures — kept as tests, removed from the engine | |

**What C1 found, and what C2 must therefore do.**

*Without* a vacuity filter the loop **diverges**: ~2,400 registry records have a permissive `cond`
and an `act` that does nothing, and *para* picks them in descending sūtra order — 6.4.167, 6.4.166,
6.4.165 … — rewriting रामसुँ as रामसुँ until the 500-iteration budget dies. So:

1. **A candidate that would not change the tape is not a candidate.** The same dry-run idea that
   took the gap report from 17,285 findings to 4 belongs in the scheduler.

2. With that filter the divergence becomes an honest halt, and the real blocker shows: every case
   stops at *stem + raw upadeśa* — रामसुँ, रामजस्, रामटा, हरिऔ, नदीऔ — where the next rule needed is
   **it-saṃjñā and it-lopa (1.3.2 · 1.3.7 · 1.3.8 · 1.3.9)**. The scheduler cannot offer them: they
   sit in the `upadesha` phase pool, the state is past that phase, and the chain is forward-only.
   **The phase model contradicts उपदेशे** — 1.3.2's condition is the presence of an upadeśa on the
   tape, which 4.1.2 creates *after* the upadeśa phase has closed. A phase chain is a pipeline in
   disguise (Art. 7), and this is where it bites.

3. *para* is also being asked the wrong question. विप्रतिषेधे परं कार्यम् settles two rules contending
   for **the same site**; the loop hands it every applicable rule at once. C2 must apply the
   non-conflicting ones and reserve para for genuine same-site contention.

`tests/regression/test_autonomy_baseline.py` pins all of this: it fails the day a candidate advances
रामसुँ, which is the day C2 starts working.

**Gate C:** every rāma cell, every bhū cell and all 364 shipped derivations reproduce through the
autonomous loop, with traces a scholar can read.

### Phase D — Rules as data

| # | deliverable | check |
|---|---|---|
| D1 | the ~50-operation vocabulary (ādeśa · lopa · āgama · dvitva · ekādeśa · samprasāraṇa · ṇatva/ṣatva · it-lopa …) | one implementation, reused; the mechanism budget is enforced per batch |
| D2 | adhikāra → scope compiler; generated scopes replace hand-written `requires` | a lint proves no rule contradicts its adhikāra |
| D3 | migration of the declarative mass of `sutras/` from code to records | |
| D4 | the 2,418 placeholders implemented as records or demoted out of the count | |

**Gate D:** a new sūtra in an already-modelled shape needs a record and tests — zero engine edits.

### Phase E — Both journeys *(the product; moved ahead of breadth because the audience is scholars and learners)*

| # | deliverable | check |
|---|---|---|
| E1 ◐ | dhātupāṭha completed for gaṇas 2–10 (was: 986 roots, 971 of them gaṇa 1) | **started (2026-09-17)**: 1,060 roots bulk-imported from `ashtadhyayi-com/data` (`scripts/build_dhatupatha_upadesha_v3.py`), **986 → 2,046 entries**, all gaṇas now populated. शास् (अनुशिष्टौ) is in the data, but शास्ति itself does not yet derive: it shares its plain upadeśa `SAsu~` with शासु (इच्छायाम्), and the two are traditionally distinguished only by svara (udātta/anudātta iṭ) — invisible to `pipelines.tinanta.derive()`, which reads the bare SLP1 string. That is an accent-modeling gap, not a data gap; correctly deferred to Phase G |
| E2 ◐ | śabda / prātipadika list loaded with provenance | **started**: 13 attested paradigms vendored from ashtadhyayi.com (`data/reference/shabda_gold/`), **312/312 cells derive correctly** — नदी went 17/24 → 24/24 the same day, by implementing 7.3.112 आण् नद्याः, 7.3.116 ङेराम्, 7.3.107 अम्बार्थनद्योर्ह्रस्वः, scheduling the स्त्री saṃjñās (1.4.3–1.4.5) and restricting 6.1.103 to its own पुंसि. `make shabda` shows any paradigm as a table; `--cell V-N` shows that cell's prakriyā |
| E3 | form index v2 — every vibhāṣā branch, with derivation ids so the forward journey is reproducible on demand | |
| E4 | sandhi splitting: the saṃhitā/tripādī stratum compiled to an invertible relation → over-generating lattice | दण्ड एवाभिरक्षति → दण्डः + एव + अभिरक्षति, each cut citing its sūtra |
| E5 | generate-and-test verification (Art. 17) | a candidate is accepted only if re-generation reproduces the input exactly |
| E6 | kāraka (1.4.23–55) and agreement as the ranker | ranked candidates **with reasons**, never one answer |
| E7 | the "explain this word" surface — both journeys, side by side | |

**Gate E:** every word of Manusmṛti 7.18 — दण्डः शास्ति प्रजाः सर्वा दण्ड एवाभिरक्षति — split,
analysed, ranked with reasons, and re-derived forward with citations.

### Phase F — Breadth, measured
Frequency-ranked implementation driven by the Phase A gap list, prakaraṇa by prakaraṇa.
**Gate F:** token-coverage ladder 60 % → 80 % → 90 % on a fixed teaching corpus — Gītā ·
Manusmṛti · Hitopadeśa · Pañcatantra — published per release.

### Phase G — Accent and Vedic
Svara, Vedic variants, vārtikas. **Refused until every gate above has passed.**

## 6. What we refuse

- **No ML in the derivation path.** A model that is 97 % right destroys the only property that
  matters. Models propose candidates for review; they never produce forms.
- **No rule in code.** `if sutra_id == "6.1.101"` is a design failure, not a shortcut.
- **No utsarga narrowed to dodge an apavāda.** Declare the conflict.
- **No unverifiable claim.** Every rule cites; every test is a citation or an attestation; every
  number is one command away.
- **No test weakened to pass.** A failing test is a bug in the rule.
- **No accent, no Vedic, no vārtika before the classical core is measured.**
- **No guessed analysis.** An unrecognised word is a gap naming what is missing, never a
  statistical fallback (§4.5).
- **No second engine.** One trunk (§0).

---

## 7. Decisions needed

1. **Hours/week and horizon** — changes the schedule, not the order.
2. ~~**Primary audience**~~ — **decided 2026-09-15: scholars and learners first** (explanation,
   commentary, teaching mode); NLP pipelines later. §5.5 and the phase order below follow from
   this.
3. **Cooperation stance** — approach Ambuda (Vidyut) and UoH with the benchmark early, or build
   the lead first? Recommendation: early. A benchmark with two engines on it is worth more than
   one with ours.
4. **Corpus licensing** — pursue explicit upstream terms (recommended) or standardise on
   public-domain commentaries plus our own annotations, keeping the corpus swappable.


---

## 8. What to take from the field

Nothing here is a dependency of the derivation path (Art. 19 allows oracles, not crutches).
Confirm every licence before vendoring any data — Art. 6's firewall applies to all of it.

| project | what it is | what we take | what we do not take |
|---|---|---|---|
| **Vidyut** (ambuda-org, Rust, **MIT**, Python bindings) | `vidyut-prakriya` derives with per-step sūtra traces; `vidyut-kosha` stores tens of millions of forms at ~1 byte each; `vidyut-sandhi` applies *and undoes* sandhi; `vidyut-cheda` segments | **the primary differential oracle** (A4), and `kosha` as the proof that the form index is the right artifact — and the design to copy for E3 | derivations. Our engine must derive, or the project has no reason to exist |
| **Sanskrit Heritage** (Huet, INRIA) | very large lexicon; finite-state segmenter; the reference for lexicon-directed splitting | the segmentation **method** for E4, and a second opinion on splits | the lexicon wholesale, until terms are explicit |
| **Samsaadhanii** (Amba Kulkarni, UoH) | the only serious **Pāṇinian kāraka parser**; sandhi splitter; analyser/generator | the kāraka/dependency design for E6 — this is the closest prior art to our §4.5 ranker | its formalism; ours must stay sūtra-traceable |
| **DCS** (Digital Corpus of Sanskrit, Hellwig) | large morphologically analysed corpus | the **token-coverage denominator** for Gate F, and attested forms for tests | its analyses as ground truth without review |
| **ashtadhyayi.com data** | 3,983 sūtras with anuvṛtti/adhikāra pointers, resolved text, commentaries, 1,712 attested usages | the corpus we already consume; the pointer graph seeds B2 and D2 | bulk redistribution — no licence file upstream |
| **SanskritVerb / ashtadhyayi.com tools** (Dhaval Patel) | verb-form generation with displayed prakriyā | a cross-check on tiṅanta forms and a model for teaching output | |
| **Formal literature** — Mishra's *Simulating the Pāṇinian System*; Hyman on sandhi as finite-state calculus; Huet & Goyal on segmentation and completeness | the mathematics under §4.5 | the formal justification for E4's inversion and for enumerating morphology | |
| **SandhiKosh** and published split gold sets | benchmark data for splitting | Gate E/F metrics that are comparable to other work | |

The strategic reading: **`vidyut-kosha` already proves the index idea at scale, and Samsaadhanii
already proves the kāraka layer.** Neither publishes a per-step, sūtra-cited derivation *for an
analysed word in running text* — that join is the opening, and it is exactly what §4.5 produces.
