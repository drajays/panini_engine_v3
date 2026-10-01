# AMENDMENT 17 — Two ladders: *vipratipatti* (rule conflict) and *prāmāṇya* (text authority)

> Per Constitution **Art. 10**, this document records the proposed change, its
> rationale, and its acceptance status.

**Date opened:** 2026-10-01
**Author:** drajays (drafted from the arena two-ladder paper; numbering and
surgical corrections by Cursor after merit review)
**Status:** **ACCEPTED 2026-10-01** — signed in writing: "i sign implement this
and make engine better fully rule based". Articles 21 and 22 enter
`CONSTITUTION.md`; Art. 14 is amended in place; Art. 3 §2 is rewritten; Art. 10's
count becomes twenty-three (0–22).

This is **not** AMENDMENT 16. AMENDMENT 16 / Art. 20 (अर्थनिर्देश) stays.

---

## 1. The two questions that were being merged

| | Question | Answered by | When |
|---|---|---|---|
| **Ladder 1** | *Which rule wins?* (विप्रतिषेध) | Pāṇini's own devices, inside the śāstra | At **runtime**, every competing firing |
| **Ladder 2** | *What does the rule mean?* (प्रामाण्य) | The commentary tradition | At **design time**, once per dispute, recorded here |

यथोत्तरं मुनीनां प्रामाण्यम् belongs to **Ladder 2 only**. It says nothing about
how 8.3.59 vs 6.1.87 is settled at runtime — that is *asiddhatva* and *para*.

**Engineering consequence:** Ladder 2 is a citation discipline, never a runtime
input. Art. 2 and Art. 6 already forbid `cond()` from reading `data/reference/`;
by the same logic no commentary is consulted while a derivation is running.

Art. 14's "lower-numbered wins" clause made **Kāśikā outrank the Mahābhāṣya** as
a meaning authority. That is correct as an *evidence roster* ("what may I quote")
and indefensible as *prāmāṇya*. Split: Art. 14 stays the roster; Art. 22 is
meaning; Art. 21 is runtime conflict.

---

## 2. Ladder 1 — विप्रतिषेध (Art. 21)

A layer is reached only if the layer above ties. L0–L2 decide whether a conflict
exists at all. Nipātana is a **gate**, not a PŚ 38 strength term.

```
pre-conflict:
  L0  pāṭha / anuvṛtti / adhikāra
  L1  asiddhatva          (8.2.1, 6.4.22, 6.1.86)
  L2  pratiṣedha          (blocks_sutra_ids)
  L2b nipātana freeze     (dispatcher gate, already modelled)
  STOP if the remaining tie is vibhāṣā → fork (engine/vikalpa.py)

PŚ 38  पूर्वपरनित्यान्तरङ्गापवादानामुत्तरोत्तरं बलीयः
  L4  nitya               not_modelled → GAP, do not fall through silently
  L5  antaraṅga           not_modelled → GAP
  L6  apavāda             modelled, declared `apavada_of`
  L7  para (1.4.2)        modelled — Pāṇini's floor
  L8  pūrva               residue of PŚ 38

after:
  L9  sakṛdgati           modelled (`blocked_sutras`)
  L10 jñāpaka             CONFLICT_OVERRIDES + an amendment; never invented

diagnostic, never a winner:
  SOI (Rajpopat) may propose an undeclared apavāda; it must not decide
```

**What was wrong in the engine:** `engine/resolver.py` ranked Rajpopat SOI
**above** 1.4.2. An unnamed heuristic beat Pāṇini's own tie-breaker, and
undeclared apavādas never had to become `apavada_of`.

---

## 3. Ladder 2 — प्रामाण्य (Art. 22)

Reached when writing a sūtra file, never while `cond()` runs.

| # | Authority | Role |
|---|---|---|
| T0 | pāṭha (ashtadhyayi.com data, Bhāṣya-supported when MSS differ) | the text |
| T1 | वार्त्तिक (Kātyāyana) | śāstra, not commentary |
| T2 | महाभाष्य (Patañjali) | ceiling of interpretation |
| T3 | प्रदीप + उद्योत | whose reading of the Bhāṣya |
| T4 | परिभाषेन्दुशेखर | meta-rules (Ladder 1 L4–L9) |
| T5 | लघुशब्देन्दुशेखर | SK-level prakriyā disputes |
| T6 | SK cluster (Bhaṭṭoji + ṭīkās) | which rules tradition cites together; **zero** kram authority (Art. 3) |
| T7 | Kāśikā cluster (Kāśikā → Nyāsa → Padamañjarī) | udāharaṇa; T2 wins on conflict |
| T8 | प्रक्रिया primers | pedagogical; no deciding authority |
| T9 | modern scholarship (Cardona, Kiparsky, …) | zero prāmāṇya; modelling only |
| T10 | oracles (Vidyut, Saṃsādhanī, Heritage) | Art. 19: can prove wrong, never prove right |

**Declared school:** Nāgeśīya-navya-vyākaraṇa. Where the tradition is divided,
T4–T5 decide; where Nāgeśa is silent or contested, revert to T2. A departure is
an amendment, cited from the sūtra docstring.

An amendment in this repository is the **audit trail** of a Ladder 2 decision,
not a higher pramāṇa than T2.

---

## 4. Corrections vs the arena draft

1. Numbered **17**, not 16 (Art. 20 is अर्थनिर्देश).
2. Art. 14 is **not** split into 14A/14B — roster stays Art. 14; meaning is Art. 22.
3. Ladder 2 is **not** "only when L10 ties" — it is used every time a human writes `cond()`.
4. Nipātana is **not** a PŚ 38 strength layer.
5. nitya / antaraṅga are **not** implemented in this amendment — they are honest gaps.
6. SOI is **demoted**, not deleted — it proposes; *para* decides.
7. PŚ 50 is vendored from the **same** ashtadhyayi-com/data pāṭha as PŚ 38
   (not invented). It is cited on the antaranga layer; the *procedure* stays
   `not_modelled` until a testable conflict exists.

---

## 5. Code that lands with this acceptance

- `engine/resolver.py`: override/jñāpaka → apavāda → vikalpa stop → *para*. SOI never returns a `Decision`. Unmodelled L4/L5 named on the decision. An SOI proposal that disagrees with *para* is an Art. 18 gap (`undeclared_apavada_candidate`).
- Gaṇa vikaraṇas 3.1.69, 73, 77, 78, 79, 81 declare `apavada_of=("3.1.68",)` and drop SOI scores.
- `data/inputs/paribhasha_shekhara.json`: **all 133** PŚ pāṭha lines from ashtadhyayi-com/data (vyākhyā omitted). PŚ 50 असिद्धं बहिरङ्गमन्तरङ्गे is now cited on the antaranga layer (still `not_modelled` as a procedure). LŚ excerpt for 1.1.44. Catalog `data/inputs/grantha_catalog.json`: ārthika granthas are not runtime.
- Tests: layer order; no `"soi"` winner; SOI cannot beat *para*.

---

## 6. Acceptance

- [x] **Accepted** — 2026-10-01, drajays, in conversation: "i sign implement this
      and make engine better fully rule based" / "make sure we pass every test we
      build based on this new architecture conflict resolution rules".

Signed: drajays  Date: 2026-10-01
