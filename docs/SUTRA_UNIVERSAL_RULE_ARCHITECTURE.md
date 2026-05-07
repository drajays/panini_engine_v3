# Universal sūtra rule architecture

This document expands **CONSTITUTION.md Article 13**. It governs how
`sutras/adhyaya_*/pada_*/sutra_*.py` (and future `engine/rules/**` helpers
that encode Pāṇinian *nimitta*) are written and refactored.

## Core principle

Every sūtra’s `cond(state)` must be satisfiable from **native linguistic
signals** already present on `State` / `Term`: varṇas and their tags,
`it_markers`, `samjna_registry`, `adhikara_stack`, pratyāhāra classes, and
**structural** `Term` tags (`dhatu`, `pratyaya`, `kngiti`, `sanadi`, …).

Recipe-only scaffolding in `state.meta` must **not** be the reason a
universal VIDHI fires (see Article 13 in `CONSTITUTION.md`).

## Forbidden patterns

### 1. Demo / recipe bypass flags inside sūtra `cond` or `act`

```python
# Disallowed for new code and for refactors touching this rule
if state.meta.get("P035_6_4_64_A_lopa_atus_arm"):
    ...
if state.meta.get("corrected_v2_P004_B_6_4_148_arm"):
    ...
```

Such keys are **pipeline wiring**, not *nimitta*. Legacy files may still
contain them until migrated; do not copy the pattern into new sūtras.

### 2. Single-root `upadesha_slp1` equality as the primary trigger

```python
# Disallowed — narrows a general rule to one demo
if dhatu.meta.get("upadesha_slp1") == "gAN":
    ...
```

**Allowed:** a **module-level** `frozenset` (or data-driven set) that
mirrors an explicit **gaṇa / dhātu-pāṭha** enumeration **named in the sūtra**
or in engine-backed kosha data loaded once at import — and membership
tests against a **normalized** base string, not ad hoc literals scattered
in `cond`.

### 3. Demo- or form-specific helper names in sūtra modules

Prefer names that describe the **linguistic operation**:
`_find_ti_start_index`, `_is_anidit`, `_kngit_sarvadhatuka_follows`, etc.

### 4. Varṇa-sequence fingerprinting of “which dhātu”

Do not identify √X by a hard-coded surface tail. Prefer phonological
predicates the sūtra actually uses (last vowel series, cluster shape,
*upadhā*, …).

### 5. Pratyaya identity as a stand-in for grammatical class

```python
# Disallowed as the *primary* gate for a broad sūtra
if pratyaya.meta.get("upadesha_slp1") == "atus":
    ...
```

**Allowed:** when the **sūtra’s own wording** names one pratyaya or a
closed paradigmatic set (e.g. a specific *sup* morpheme), or when the
engine represents that class with **tags** (`kngiti`, `ardhadhatuka`,
…). **CONSTITUTION Article 2** already permits structural checks such as
`upadesha_slp1 == "Ne"` for *sup* rows where the rule is **defined** on
that morpheme class — use judgment: prefer tags when they carry the same
information.

## Required patterns

### Condition detection

- **Sthānin / locus:** varṇa indices, `_find_operative_a()`, TI boundary
  helpers consistent with **1.1.64**, etc.
- **Nimitta:** `Term.tags`, `it_markers`, pratyāhāra membership.
- **Adhikāra:** `adhikara_in_effect(...)` from `engine/gates.py` where
  applicable.

### Saṃjñā and registry

Use `state.samjna_registry` and `Term.meta` / `Term.tags` only for meanings
the śāstra assigns, not for “which pytest row”.

### Module-level constants

Enumerations given by the sūtra text or by kosha data:

```python
_EXPLICIT_UPADESHA_BASES: frozenset[str] = frozenset({...})  # at import
```

### Idempotency

One completion flag per **sūtra file**, keyed by **sūtra id**, on the
**Term** (or registry) that underwent the operation:

```python
if term.meta.get("6_4_24_upadha_lopa_done"):
    ...
```

Avoid unrelated `…_lut_tasi_done`-style names unless that sūtra alone owns
the operation.

### Shape of implementation

Reference style: `sutras/adhyaya_6/pada_4/sutra_6_4_71.py` — single `_find`,
`cond` = `_find is not None`, `act` reuses `_find`.

## Pipelines (Article 7)

`pipelines/*.py` schedule `apply_rule` only. They may set `state.meta` for
**ordering** or **adhikāra-adjacent** book-keeping only where CONSTITUTION
already allows — but if a sūtra’s `cond` **requires** a meta arm to ever
be true, that is technical debt: extend **tags / registry / prior rules**
until the sūtra can see the *nimitta* structurally.

## Quick checklist (before committing a touched sūtra)

- [ ] No new `state.meta.get("…_arm")` / `corrected_v2_*` in `cond`/`act`.
- [ ] No `upadesha_slp1 == "one_off_root"` as the sole trigger unless the
      sūtra itself is root-selective and the set is module-level data.
- [ ] Helper names describe operations, not demos.
- [ ] `cond` uses tags, it markers, saṃjñā, adhikāra, phonological shape.
- [ ] Single `_find` → `cond` / `act` chain; idempotency key =
      `{sutra_id}_…_done` on the affected term.
