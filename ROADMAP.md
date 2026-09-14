# Pāṇini Engine — architecture, process, roadmap

*Written 2026-09-15. Every number below was measured on this repository today; §1 says how to
reproduce each one.*

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

### Ambiguity is the product

For a learner, "सर्वाः is accusative plural feminine" is worth less than "सर्वाः could be X or Y;
it is Y here **because** it agrees with प्रजाः in liṅga, vacana and vibhakti, and because शास्ति
takes a कर्मन् (1.4.49)". So the analyser returns *ranked candidates with reasons*, never a single
answer, and the kāraka layer (1.4.23–55) plus agreement is what does the ranking.

The matching refusal: **an unknown word is a gap, never a guess.** No statistical fallback, no
"probably a noun". A closed world that says what it does not know is worth more to a scholar than
an open one that improvises.

## 5. Roadmap

Gates are binary. No phase starts before its predecessor's gate passes. Two clocks are reported at
every gate: **coverage** (operational sūtras) and **quality** (agreement, token coverage). A phase
that raises coverage and lowers quality is a failed phase.

### Phase A — Tell the truth (foundation)
*Land:* honest coverage metric (invoked · moved · tested · cited) replacing `coverage_report()`;
`sutra_lint` in the hook; `gaps.py` so every SKIPPED becomes a named missing sūtra; `bench/`
skeleton with a Vidyut differential runner and the first published agreement number; **the
generated-forms index** — `patha_pipeline.build_form_index()` generalised over the full dhātupāṭha
and a śabda list, verbs included. That index is one artifact doing three jobs: it makes analysis
possible, it *is* the honest coverage number, and it is the differential-test corpus against Vidyut.
*Gate:* one command prints a report card; the README's numbers are all reproducible; the honest
coverage number is committed.

### Phase B — Execute the metatheory
*Land:* `paribhasha/` — 1.4.2 as the resolver's basis, the apavāda graph (seeded from the corpus's
own pointers), asiddha strata replacing `tripadi_zone`, vibhāṣā forking as a first-class output.
Convert existing conflicts: every place where an utsarga was narrowed by hand becomes a declared
block. 6.1.104 ↔ 6.1.102 is the template and the acceptance test.
*Gate:* BLOCKED steps rise from 24 to the hundreds; no rule's `cond` contains a narrowing that
belongs to another sūtra; `test_autonomous_vs_recipe.py` xfails turn green for laṭ kartari.

### Phase C — Dissolve the pipelines
*Land:* the scheduler + resolver select rules; `derive()` becomes a thin router (this is
`final_plan.md` Phase 4/5, now unblocked). 187 pipelines become regression fixtures — kept as
tests, removed from the engine.
*Gate:* every rāma cell, every bhū cell and the 364 shipped derivations reproduce **through the
autonomous loop**, with identical surfaces and traces a scholar can read.

### Phase D — Rules as data
*Land:* the ~50-primitive vocabulary; the adhikāra→scope compiler (generated, not hand-written
`requires`); migration of the declarative mass of `sutras/` from code to records. The 2,418
stub-gloss files are either implemented as data or demoted out of the coverage count.
*Gate:* a new sūtra in an already-modelled shape needs a record and tests — zero engine edits.

### Phase E — Both journeys (moved ahead of breadth: the audience decided it)
*Land:* the dhātupāṭha completed for gaṇas 2–10 and a śabda list loaded; sandhi splitting as an
invertible transducer over the tripādī/saṃhitā rules; generate-and-test verification; kāraka
(1.4.23–55) and agreement as the ranker; the "explain this word" surface showing both journeys.
*Gate:* every word of a fixed teaching passage — Manusmṛti 7.18 is the acceptance case — split,
analysed, ranked with reasons, and re-derived forward with citations.

### Phase F — Breadth, measured
*Land:* frequency-ranked implementation driven by the gap list, prakaraṇa by prakaraṇa.
*Gate:* token-coverage ladder 60 % → 80 % → 90 % on a fixed **teaching** corpus (Gītā ·
Manusmṛti · Hitopadeśa · Pañcatantra — what learners actually read), published per release.

### Phase G — Accent and Vedic *(only after F)*
svara, Vedic variants, vārtikas. Refused until the classical core is measured.

---

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
