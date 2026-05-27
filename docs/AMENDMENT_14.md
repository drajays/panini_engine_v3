# AMENDMENT 14 — Authoritative Sources & Anti-Patchwork Hardening

> Per Constitution Art. 10, this document records the proposed change,
> its rationale, and its acceptance status. The corresponding edits
> are applied to `CONSTITUTION.md` and `.cursorrules` only after this
> file is accepted in writing.

**Date opened:** 2026-05-22
**Author:** drajayshukla (with audit research by Claude)
**Status:** PROPOSED — accepted on signing below.

---

## 1. Background

The engine's stated purpose (Art. 0) is to be a glass-box,
mathematically rule-based interpreter of the Aṣṭādhyāyī. Two
problems have grown over time:

1. **Source under-citation.** Most sūtra files do not name the
   commentarial source that justifies the predicate in their
   `cond()`. When a sūtra is later rewritten, the next editor cannot
   tell whether the existing logic reflects Kāśikā, Bhāṣya, SK, a
   computational oracle, or guesswork.
2. **Patchwork persistence.** Article 13 §1 names `_arm` meta keys
   as technical debt "to be removed when that file is next
   refactored." In practice ~84% of sūtra files still gate their
   `cond()` on an `_arm` flag, and pipelines actively write those
   flags. Article 13 is aspirational, not enforced.

Both problems undermine Art. 0 (glass-box).

## 2. Proposed amendments

### 2.1 Article 14 (new) — Authoritative Sources & Citation

A new Article is added between current Art. 13 and Art. 10's
amendment procedure (which becomes effectively Art. 99 in the
existing numbering — keep amendment procedure at the end). The new
Article reads:

> **Article 14 — Authoritative Sources and Citation**
>
> Every sūtra file under `sutras/adhyaya_*/pada_*/sutra_*.py` whose
> `cond()` or `act()` makes a non-trivial linguistic decision must
> name the textual source that justifies that decision. The
> authoritative source roster is defined in `audit_cursor.md` § 0
> and `audit_claude.md` § A. The roster's precedence order is binding.
>
> Minimum citation requirement in each sūtra file's module docstring:
>
> - **Source #1** (ashtadhyayi.com row index) — e.g. `i = 64003`
>   for sūtra 6.4.3.
> - **Source #2** (Kāśikā udāharaṇa) — quoted in Devanāgarī.
> - Either a **cross-validation note** (Vidyut, Saṃsādhanī, Sanskrit
>   Heritage) confirming the surface output, OR a **regression test
>   reference** under `tests/regression/` that verifies the surface.
>
> Constitutional test
> `tests/constitutional/test_sutra_source_citation.py` (added under
> this amendment) refuses commits that touch a sūtra file without
> updating these citation fields.
>
> Sources outside the roster (blogs, LLM output, unattributed PDFs,
> Wikipedia) **may not** be cited as justification. Wikipedia may be
> consulted to *locate* a primary source; the citation must then
> name the primary.
>
> When two roster sources disagree, the lower-numbered (higher
> precedence) source wins. If the disagreement is itself notable,
> the resolution is documented in `docs/AMENDMENT_<N>.md` and the
> sūtra docstring links to that amendment.

### 2.2 Article 13 hardening

Article 13 §1's prohibition on new `_arm` keys is tightened from
"should not" to **MUST NOT**:

> **Article 13 §1 (revised) — No new arm flags, period.**
>
> No file under `sutras/` may be committed if its `cond()` reads
> `state.meta[K]` where `K` ends in `_arm` or matches the regex
> `(?i)(corrected_v[0-9]+|P[0-9]+(_|$))`. The constitutional test
> `tests/constitutional/test_no_new_arm_gates.py` enforces this on
> a strict-additive basis: existing `_arm` reads are grandfathered
> and counted; any commit increasing the count fails CI.
>
> Existing arms are technical debt and remain bounded above by the
> grandfathered count. Migrations that *decrease* the count are
> always allowed; commits that *increase* it (including same-day
> reinstatement after a delete) are refused.
>
> Pipelines under `pipelines/` and orchestrators under `core/` may
> still set `_arm` keys during the migration period, but each new
> write must be accompanied by a removal in the same commit (net
> additive: zero or negative).

### 2.3 Article 12 enforcement — duplicate prakriyā ban

Add to Article 12 §3:

> No new file under `pipelines/` may carry the substring
> `_corrected_` or `_corrected_P` in its name. The substring
> implies a pre-existing canonical pipeline is wrong; the canonical
> pipeline must be fixed instead. Constitutional test
> `tests/constitutional/test_no_corrected_pipelines.py` refuses
> commits that add such files.

### 2.4 Article 8 §2 clarification — UI display vs. engine truth

Add to Article 8 §2:

> The web UI's default trace filter shows only `APPLIED` rows
> (form-changing). `AUDIT` and `APPLIED_VACUOUS` rows remain
> *recorded* by the engine and *available* via a "विस्तरः" toggle,
> but their absence from the default view is **not** a regression.
> Engine trace completeness is verified by `tests/regression/`, not
> by the UI default.

## 3. Acceptance checklist (per Art. 10)

- [ ] Constitutional tests added under
      `tests/constitutional/test_sutra_source_citation.py`,
      `test_no_new_arm_gates.py`, `test_no_corrected_pipelines.py`.
- [ ] Existing forward/regression suite continues to pass.
- [ ] `audit_claude.md` and `audit_cursor.md` cross-referenced in
      `CONSTITUTION.md` under Art. 14.
- [ ] `.cursorrules` updated to reflect Art. 14 + Art. 13 hardening.
- [ ] Explicit written acceptance below.

## 4. Acceptance

```
Accepted by: ________________________  date: __________
```

## 5. Rollback

If implementation of any §2 test breaks more than 5 currently-passing
forward tests on the first run, this Amendment is automatically
suspended. Authors investigate and either (a) refine the test to
match true intent or (b) open `AMENDMENT_14_revision.md`.
