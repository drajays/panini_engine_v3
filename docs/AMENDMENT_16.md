# AMENDMENT 16 — Two ladders: *vipratipatti* (rule conflict) and *prāmāṇya* (text authority)

> Per Constitution **Art. 10**, this document records the proposed change, its
> rationale, and its acceptance status. The corresponding edits are applied to
> `CONSTITUTION.md` **only after this file is accepted in writing** (§7).

**Date opened:** 2026-10-01
**Author:** drajayshukla (drafted with agent assistance)
**Status:** **OPEN — awaiting written acceptance.** No article text in
`CONSTITUTION.md` has been changed by this file yet.

---

## 1. Background — the two questions that keep getting merged

The question that prompted this amendment was asked as one question:

> For a Pāṇini rule-based engine, what order of *rule conflict* and *text
> authority* must we accept?

It is **two** questions, and the repository currently has one flat answer
(Art. 14) plus a resolver that quietly mixes śāstra with engineering taste.

| | Question | Answered by | When it is asked |
|---|---|---|---|
| **Ladder 1** | *Which rule wins?* (विप्रतिषेध / बाध्य-बाधक) | Pāṇini's own devices — all of them **inside** the śāstra | At **runtime**, on every competing firing |
| **Ladder 2** | *What does the rule mean / which reading is right?* (प्रामाण्य) | The commentary tradition | At **design time**, once per dispute, recorded here |

The classical maxim **यथोत्तरं मुनीनां प्रामाण्यम्** belongs to **Ladder 2**
and only to it. It says nothing about how a conflict between 8.3.59 and 6.1.87
is settled at runtime — that is settled by *asiddhatva* and *para*, which no
commentary can override.

**The engineering consequence is the important part:** Ladder 2 is a
*citation discipline*, never a runtime input. Art. 2 and Art. 6 already forbid
`cond()` from reading `data/reference/`; by the same logic no commentary is
ever consulted while a derivation is running. Authority resolves when a human
writes a sūtra file; what executes is Ladder 1.

### 1.1 What is measured in this repository today

| finding | value | where |
|---|---|---|
| Paribhāṣā layers the resolver knows | 5 (`apavada`, `para`, `nitya`, `antaranga`, `once_beaten`) | `data/inputs/paribhasha_shekhara.json` → `resolver_layers` |
| …of which actually execute | **2** (`apavada`, `para`) | `engine/resolver.py` |
| …declared `not_modelled` | **2** (`nitya`, `antaranga`) | `tests/constitutional/test_vipratisedha_resolver.py::test_unmodelled_layers_are_declared_not_hidden` |
| Ladder-1 layers with **no** representation at all | `nipatana`, `vikalpa`-as-stop-condition, `jñāpaka` | — |
| Paribhāṣās vendored | 8 (PŚ 13, 38, 40, 52, 54, 55, 57, 66) | `data/inputs/paribhasha_shekhara.json` |
| Strength ladder quoted (PŚ 38) | पूर्वपरनित्यान्तरङ्गापवादानामुत्तरोत्तरं बलीयः | `engine/paribhasha.py` |
| An **engineering heuristic** ranked **above** Pāṇini's own 1.4.2 | SOI (Layer C) fires before *para* (Layer D) | `engine/resolver.py:resolve_with_reason` |

---

## 2. Ladder 1 — विप्रतिषेध: which rule wins

Consult in order. A layer is reached **only if the layer above it ties**.
L0–L2 are not "strength" at all — they decide whether a conflict exists.

### L0 — पाठ + अनुवृत्ति (eligibility, not conflict)

Before two sūtras can compete, each must be *in scope*: correct pāṭha, correct
anuvṛtti, correct adhikāra, correct *it*-saṁjñā. Anuvṛtti is baked in (Art. 4);
adhikāra scope is a gate (Art. 3 §1). Most apparent "conflicts" die here.

### L1 — असिद्धत्व (invisibility, not strength)

An *asiddha* rule is not *weaker* — its output literally does not exist for the
observer. This is ordering, so it precedes every strength comparison.

| domain | sūtra | range |
|---|---|---|
| tripādī | 8.2.1 पूर्वत्रासिद्धम् | 8.2.1–8.4.68 |
| abhīya | 6.4.22 असिद्धवदत्राभात् | 6.4.22–6.4.129 |
| ṣatva-tuk | 6.1.86 षत्वतुकोरसिद्धः | 6.1.84–6.1.111 |

**Status:** modelled — `engine/gates.py`, `engine/strata.py`,
`data/inputs/asiddha_strata.json`, test `test_asiddha_strata.py`.

### L2 — प्रतिषेध (Pāṇini's own blocking)

A sūtra whose own text forbids another: typed `PRATISHEDHA`, carrying
`blocks_sutra_ids`. The engine's worked example is Art. 15's: 6.1.102
प्रथमयोः पूर्वसवर्णः claims every अक्-final aṅga, and 6.1.104 नादिचि blocks it.

**Status:** modelled (`engine/gates.py`).

### L3 — निपातन

Where Pāṇini fixes the form outright (निपातनम्), the fixed form wins within its
own domain — the general rules are not "beaten", they are simply not what the
sūtra asks for.

**Status:** `NIPATANA` exists in `SutraType` (Art. 1) but is **not** a resolver
layer. **Gap.**

### L4 — नित्य vs अनित्य

A rule is *nitya* if it is obtained whether or not the rival applies; *anitya*
if it is obtained only when the rival does not. The nitya rule is applied
first. (PŚ 38.)

**Status:** declared `not_modelled`. A conflict that turns on nityatva is
currently decided by the layers *below* it and **does not say so** — which is
an Art. 18 defect, not merely a missing feature.

### L5 — अन्तरङ्ग vs बहिरङ्ग

असिद्धं बहिरङ्गमन्तरङ्गे — the bahiraṅga rule is asiddha with respect to the
antaraṅga. Two named exceptions, both already vendored:

- PŚ 52 अन्तरङ्गानपि विधीन् बहिरङ्गो लुग् बाधते (luk defeats antaraṅga)
- PŚ 54 अन्तरङ्गानपि विधीन् बहिरङ्गो ल्यब्बाधते (lyap defeats antaraṅga)
- PŚ 55 वार्णादाङ्गं बलीयो भवति (āṅga rules are stronger than varṇa rules)

**Status:** declared `not_modelled`. PŚ 50 itself is **not vendored** (§6.1).

### L6 — अपवाद vs उत्सर्ग

PŚ 57 **अन्तरङ्गादप्यवादो बलवान्** — the exception beats the general rule even
when the general rule is antaraṅga. Exception to the exception: PŚ 66
अपवादो यद्यन्यत्र चरितार्थस्तर्ह्यन्तरङ्गेण बाध्यते — an apavāda that is
already *caritārtha* elsewhere yields to the antaraṅga.

**Status:** modelled, and — critically — **declared**: an apavāda wins only if
the sūtra record says `apavada_of` (Art. 15: conflict is declared, never
engineered).

### L7 — पर — 1.4.2 विप्रतिषेधे परं कार्यम्

of two rules of equal strength wanting the same position, the **later** in the
Aṣṭādhyāyī wins. This is Pāṇini's own tie-breaker and it is the floor of the
whole ladder.

**Status:** modelled (`engine/resolver.py` Layer D).

### L8 — पूर्व

The first term of PŚ 38. Operative only in the *pūrvatra* contexts; rare, and
in practice only reached when *para* is unavailable.

### L9 — सकृद्गति (persistence, not a decision)

PŚ 40 सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितमेव — what has once been set
aside stays set aside. This is why `state.blocked_sutras` persists for the rest
of a derivation.

**Status:** modelled.

### L10 — ज्ञापक

When the śāstra gives no explicit resolver, Pāṇini's own wording sometimes
implies one (*jñāpakāt siddham*). This is推理, not śruti: it must be cited from
the **Mahābhāṣya**, never invented, and recorded as an amendment.

**Status:** **not modelled.** Any use of jñāpaka must appear in the trace with
its Bhāṣya citation or not appear at all.

### Stop condition — विकल्प (before L4, not after)

If the tie is genuine optionality — वा / विभाषा / अन्यतरस्याम् / उभयथा — the
engine must **fork, not pick**. `engine/vikalpa.py` and
`test_vikalpa_branches.py` already do this. Choosing a winner inside a vibhāṣā
is not conflict resolution; it is deleting half the grammar.

### Ladder 1 summary

```
L0  pāṭha / anuvṛtti / adhikāra   ─┐
L1  asiddhatva                     │ is there a conflict at all?
L2  pratiṣedha                    ─┘
L3  nipātana                      ─┐
L4  nitya                          │ PŚ 38 — नित्यान्तरङ्गापवादानां
L5  antaraṅga                      │ उत्तरोत्तरं बलीयः
L6  apavāda                       ─┘
L7  para (1.4.2)                  ── Pāṇini's own tie-breaker
L8  pūrva                         ── residue of PŚ 38
L9  sakṛdgati                     ── persistence
L10 jñāpaka                       ── last resort, Bhāṣya-cited
──────────────────────────────────────────────────────────────
    STOP FIRST if the tie is विकल्प → fork (engine/vikalpa.py)
```

---

## 3. Ladder 2 — प्रामाण्य: which text wins

Reached **only** when Ladder 1 ties at L10, or when the *reading* of a sūtra
itself is disputed. This ladder governs the docstring of a sūtra file; it never
governs a running derivation.

### T0 — the pāṭha itself

The Aṣṭādhyāyī. No commentary may contradict it. Where manuscripts differ
(*pāṭhabheda*), the reading the **Mahābhāṣya** supports wins. Canonical
pāṭha/padaccheda/anuvṛtti source for this engine: the ashtadhyayi.com data
repo (`i = 1·adhyāya·pāda·sūtra`), cross-checked against a critical edition.

### T1 — वार्त्तिक (Kātyāyana)

Part of the śāstra, not a commentary on it: Kātyāyana supplies rules the sūtras
do not state, and the Bhāṣya argues over them. **Omitted from the commonly
circulated list — this is the single largest gap in it.** For an engine,
vārttikas are executable rule material, not opinion.

### T2 — महाभाष्य (Patañjali)

**भाष्यकारवचनं परम्.** The ceiling of interpretive authority.
यथोत्तरं मुनीनां प्रामाण्यम् — Pāṇini < Kātyāyana < Patañjali — operates
*within* T0–T2 and stops there.

### T3 — भाष्य-व्याख्यान: प्रदीप (Kaiyaṭa) + उद्योत (Nāgeśa)

You cannot cite "the Mahābhāṣya says X" without saying *whose reading* of the
Mahābhāṣya. The Uddyota **is** Nāgeśa reconciling the tradition — so any
hierarchy that names Nāgeśa as final adjudicator must name the Uddyota here,
above the Śekhara.

### T4 — परिभाषेन्दुशेखर (Nāgeśa)

The authority for **meta-rules** — exactly Ladder 1's L4–L9 — and for the
validity of a paribhāṣā. Where Nāgeśa's reading is contested, the older
paribhāṣā traditions (Vyāḍi, Śākaṭāyana) are consulted.

### T5 — लघुशब्देन्दुशेखर (Nāgeśa on the Siddhānta-Kaumudī)

Decisive for disputes *at the SK level* — i.e. for prakriyā, not for pāṭha.

### T6 — the Siddhānta-Kaumudī cluster

सिद्धान्तकौमुदी (Bhaṭṭoji) + प्रौढमनोरमा (Bhaṭṭoji) + तत्त्वबोधिनी
(Jñānendra Sarasvatī) + बालमनोरमा (Vāsudeva Dīkṣita). One cluster, one author
at its head. Authoritative for **which rules tradition cites together** and for
exemplification.

> **Art. 3 carve-out, restated:** the SK's *arrangement* has **zero** authority
> for engine scheduling. "No Siddhānta-Kaumudī ordering is ever consulted."
> Ranking Prauḍhamanoramā above the SK (or the reverse) is therefore
> inconsequential for this engine — neither may move a sūtra in the kram.

### T7 — the Kāśikā cluster

काशिकावृत्ति (Jayāditya + Vāmana) + न्यास / काशिकाविवरणपञ्जिका (Jinendrabuddhi)
+ पदमञ्जरी (Haradatta). The richest **udāharaṇa / pratyudāharaṇa** corpus in
the tradition, and a witness to readings older than the SK. Where it departs
from T2, **T2 wins**.

### T8 — प्रक्रिया and primers

प्रक्रियाकौमुदी (Rāmacandra), प्रक्रियासर्वस्व (Nārāyaṇa Bhaṭṭa),
लघुसिद्धान्तकौमुदी (Varadarāja), सुधा / सरला ṭīkā. Pedagogical. No authority to
decide a dispute — they deliberately omit exceptions.

### T9 — modern scholarship

Cardona, Kiparsky, Joshi & Roodbergen, Rama Nath Sharma, Vasu. **Zero
prāmāṇya**, and indispensable. Kiparsky in particular is the best available
authority on *how to formalise* asiddhatva and strata — that is a claim about
**modelling**, and this engine should treat it as such (it already does, in
`data/inputs/asiddha_strata.json`).

### T10 — oracles

Vidyut, Saṃsādhanī, Sanskrit Heritage, DCS. **Not authority at all.** They are
test fixtures (Art. 19). They can prove the engine is *wrong*; they can never
prove the engine is *right*.

### Domain-limited authorities (pramāṇa *within* their domain only)

| domain | authority |
|---|---|
| affix inventory & anubandha | धातुपाठ, गणपाठ — the upadeśa the sūtras presuppose |
| kṛt/vṛddhi exceptions | उणादिसूत्र |
| accent of prātipadikas | फिट्सूत्र (Śāntanava) |
| liṅga assignment | लिङ्गानुशासन |
| pronunciation, sthāna, svara | पाणिनीयशिक्षा (Vedāṅga) |
| artha / sphoṭa / śabda-tattva | वाक्यपदीय (Bhartṛhari) → परमलघुमञ्जूषा (Nāgeśa) → वैयाकरणभूषणसार (Kauṇḍa Bhaṭṭa) |
| non-Pāṇinian systems — सरस्वतीकण्ठाभरण (Bhoja), Cāndra, Kātantra | **no deciding authority inside the Pāṇinian system**; admissible only as *pāṭha-sākṣin* (a witness to a reading) or for historical comparison |

### The engine's own last word

For this repository the final entry in Ladder 2 is **this repository**: a
disputed point is settled by a decision written into `docs/AMENDMENT_<N>.md`
and cited from the sūtra's docstring (Art. 14, Art. 15). That is what makes a
trace auditable to a scholar — not which commentary the author happened to
prefer, but that the choice is *visible* and *reversible*.

---

## 4. Corrections to the commonly circulated ranking

The list that prompted this amendment ranks 13 texts with the Mahābhāṣya at #1
and Nāgeśa as final adjudicator. The top and the bottom are right; the middle
needs six changes before an engine can use it.

| # | circulating claim | verdict | correction |
|---|---|---|---|
| 1 | Vārttikas not listed | ✗ | Insert Kātyāyana at **T1** — śāstra, not commentary; often *is* the rule the engine needs |
| 2 | Pradīpa / Uddyota not listed | ✗ | Insert Kaiyaṭa + Nāgeśa's Uddyota at **T3**, below the Bhāṣya and above the Śekhara |
| 3 | Padamañjarī (6) > Nyāsa (7) > Kāśikā (8) | ✗ | A commentary cannot outrank its own mūla. Keep the **Kāśikā** first for udāharaṇa evidence, then Nyāsa, then Padamañjarī — and put the whole cluster at **T7** |
| 4 | Prauḍhamanoramā (4) > Siddhānta-Kaumudī (5) | ~ | Both are Bhaṭṭoji's; treat as one cluster at **T6**, and note the SK's arrangement carries no authority for kram (Art. 3) |
| 5 | "Nāgeśa is the final decisive authority" | ~ | A **school position** (Nāgeśīya-navya-vyākaraṇa), not universal. The engine must *declare* its school (§5.3) rather than inherit one silently |
| 6 | "काशिका-भाष्ययोः विरोधे भाष्यमेव प्रमाणम्" | ~ | The principle is correct and follows from T2 > T7; the *sentence* is a modern pedagogical maxim, not a mūla-vākya. State the principle; do not cite it as śāstra |
| 7 | Sarasvatīkaṇṭhābharaṇa — "zero authority" | ✗ | No *deciding* authority inside the system; still admissible as *pāṭha-sākṣin*. Bhoja's grammar is substantially Pāṇinian |

**One addition, not a correction:** a rule engine needs *jñāpaka* (L10) and
*vikalpa* as a stop condition (§2). Neither appears in any text-ranking list,
and both decide real conflicts at runtime.

---

## 5. Proposed amendments to `CONSTITUTION.md`

### 5.1 Article 14 — split into two ladders

Art. 14's present precedence list is:

```
1. ashtadhyayi.com   2. Kāśikā   3. Mahābhāṣya+Pradīpa+Uddyota
4. SK+Tattvabodhinī  5. Laghu-SK  6. Prakriyā-Kaumudī
```

with "when two roster sources disagree, the lower-numbered wins". That makes
**Kāśikā outrank the Mahābhāṣya**, which is defensible *as an evidence roster*
("what may I quote to justify this `cond()`") and indefensible *as a prāmāṇya
ladder* — it inverts **यथोत्तरं मुनीनां प्रामाण्यम्**.

Proposed: keep the list, rename it **Article 14A — Evidence roster (citation
discipline)**, and strike the "lower-numbered wins" clause, replacing it with
"the roster determines what may be cited, not what the rule means". Add
**Article 14B — Prāmāṇya ladder (Ladder 2 of AMENDMENT 16)** for meaning.

### 5.2 Article 20 (new) — the vipratipatti ladder

> **Article 20 — Rule conflict is resolved by Ladder 1, in order**
>
> When two or more sūtras claim the same position, the winner is decided by
> Ladder 1 of `docs/AMENDMENT_16.md`, in order: pāṭha/anuvṛtti → asiddhatva →
> pratiṣedha → nipātana → nitya → antaraṅga → apavāda → para → pūrva →
> sakṛdgati → jñāpaka. A vibhāṣā tie is forked, never resolved.
>
> Every layer is either **modelled** or **declared `not_modelled`**. A conflict
> that would turn on an unmodelled layer is recorded as a gap (Art. 18) naming
> the layer — it is never silently settled by the layer below.
>
> **No layer may be an unnamed heuristic.** A specificity score may *propose* a
> winner; it may not *be* one. A proposed apavāda must be promoted to a
> declared `apavada_of` in the sūtra record, or recorded as an amendment,
> before the next release.

### 5.3 Article 21 (new) — declared school

> **Article 21 — The engine declares its school**
>
> This engine is **Nāgeśīya-navya-vyākaraṇa**: where the tradition is
> genuinely divided, the Paribhāṣenduśekhara and Laghuśabdenduśekhara decide
> (Ladder 2, T4–T5), and where Nāgeśa is silent or contested the engine
> reverts to the Mahābhāṣya (T2). Any departure from this default is an
> amendment and is cited from the sūtra docstring.

*(Art. 10's "These twenty Articles (numbered 0 through 19)" becomes
"twenty-two (0 through 21)".)*

---

## 6. Proposed code changes (deferred until §7 is signed)

### 6.1 `data/inputs/paribhasha_shekhara.json`

- Add resolver layers for `nipatana`, `vikalpa`, `jñāpaka` with `status`.
- Vendor **PŚ 50** (असिद्धं बहिरङ्गम् अन्तरङ्गे) — **text to be transcribed
  from a named print edition before it lands**; Art. 14 forbids inventing a
  citation, so this entry stays absent until the edition is recorded.
- Promote `nitya` and `antaranga` from `not_modelled` only when implemented;
  until then, write the contact into the trace as a **gap**.

### 6.2 `engine/resolver.py`

- **Demote Layer C (SOI) below L7 (para).** Today an engineering heuristic
  (Rajpopat's Specificity of Input) beats 1.4.2 विप्रतिषेधे परं कार्यम् —
  Pāṇini's own tie-breaker. That is backwards, and it makes Art. 15's
  "declared relation" requirement optional, because an undeclared apavāda is
  quietly settled by a score instead of by `apavada_of`.
- Add a `nipatana` layer between `pratiṣedha` and `nitya`.
- Add the vibhāṣā stop condition before L4 and hand the tie to
  `engine/vikalpa.py`.
- Record every unmodelled-layer contact as a gap (Art. 18), naming the layer.

### 6.3 Tests

- `tests/constitutional/test_vipratisedha_resolver.py`: assert the **layer
  order** from Art. 20, and assert that no decision cites a layer string that
  is not a paribhāṣā or an Aṣṭādhyāyī sūtra id (this is what catches
  `"soi"`-style heuristics).

---

## 7. Acceptance

Per Art. 10, the changes in §5 take effect only when this section is signed.

- [ ] **Accepted** — Articles 14A/14B, 20, 21 enter `CONSTITUTION.md`;
      §6 changes are scheduled.
- [ ] **Rejected** — record the reason and the alternative order below.

Signed: ____________________  Date: __________
