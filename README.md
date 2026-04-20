# Pāṇini Engine v3.2

**A glass-box, rule-based derivation engine for Pāṇini's Aṣṭādhyāyī.**

## Status

```
  Sūtras implemented   : 32 / 32       (100%, no stubs)
  Rāma paradigm cells  : 20 / 24       (83% match against classical gold)
  All 10 SutraTypes    : ✓ represented
  Tests                : 328 passing, 4 xfailed (remaining 4 gold cells)
  SIG truth-teller     : active (9 JSON artifacts + path-regression oracle)
```

## The 20 green cells

```
      एकवचन           द्विवचन           बहुवचन
1.  रामः       ✓    रामौ       ✓    रामाः      ✗   (jas-cluster)
2.  रामम्      ✓    रामौ       ✓    रामान्     ✗   (Sas-cluster)
3.  रामेण      ✓    रामाभ्याम् ✓    रामैः       ✗   (Bis-cluster)
4.  रामाय      ✓    रामाभ्याम् ✓    रामेभ्यः   ✓
5.  रामात्     ✓    रामाभ्याम् ✓    रामेभ्यः   ✓
6.  रामस्य     ✓    रामयोः    ✓    रामाणाम्   ✓
7.  रामे       ✓    रामयोः    ✓    रामेषु     ✓
8.  राम        ✓    रामौ       ✓    रामाः      ✗   (jas-cluster)
```

## Architecture

Locked in v3.0 constitution; never amended:

- **10-fold SutraType** (SAMJNA · PARIBHASHA · VIDHI · NIYAMA · ATIDESHA ·
  ADHIKARA · PRATISHEDHA · ANUVADA · VIBHASHA · NIPATANA)
- **One-executor-per-type** dispatcher with R1/R2/R3 invariants
- **Aṣṭādhyāyī-kram** strict file layout (no Kaumudī ordering)
- **Data/reference firewall** — gold corpus is test-only
- **Anuvṛtti baked in** — no runtime anuvṛtti layer
- **cond(state)** forbidden from reading paradigm coordinates
  (vibhakti, vacana, puruṣa, lakāra) — enforced by AST tests

v3.1 amendments (centralized & auditable):

- `R1_EXEMPT` and `NIPATANA_FROZEN` frozensets
- Three-phase model (angakarya → sandhi → tripadi) with `PhaseError`
- `run_to_fixed_point()` bounded sweep with `FixedPointError`
- `BLOCKED` vs `SKIPPED` trace distinction
- `make_stub()` + `coverage_report()`
- `RecipeConflictError` for dual-claim positions
- Full SIG truth-teller (9 v2-compatible JSONs + path-regression oracle)

## Install and run

```bash
unzip panini_engine_v3.zip
cd panini_engine_v3
pip install -r requirements.txt

# Run the full test suite.
python -m pytest

# Regenerate the 9 SIG artifacts + truth report.
python -m tools.sig_benchmark
python -m tools.sutra_sig_report

# List all sūtras by type.
python -m tools.list_sutras_by_type

# Validate all 24 cells against the gold corpus.
python -m tools.validate_engine_against_source
```

## What remains for v3.3

The 4 red cells need `jas` / `Sas` / `Bis` cluster rules. These
collectively unlock cells 1-3, 2-3, 3-3, 8-3 — should land in one
focused session.

## The truth-teller in action

When you add a sūtra that changes a cell's derivation path (even if the
surface form still matches gold), the SIG regression test fails loudly:

```
FAILED tests/regression/test_sig_baseline.py::test_applied_path_matches_baseline[7-3]
  SIG PATH REGRESSION on cell 7-3:
    baseline : ['1.4.14', ..., '7.3.103', '8.2.1']
    current  : ['1.4.14', ..., '7.3.103', '8.2.1', '8.3.59']
  Surface equality may still pass, but the derivation path changed.
```

This caught every real regression during this build. If the change is
intentional, refreeze: `python -m tools.sig_benchmark --freeze`.

## Directory layout

```
panini_engine_v3/
├── CONSTITUTION.md          ← the 10 Articles (supreme law)
├── engine/                  ← fixed core (14 modules)
├── phonology/               ← pure phoneme layer (6 modules)
├── sutras/                  ← content layer (32 sūtras, Aṣṭādhyāyī-kram)
├── pipelines/               ← subanta recipe (tinanta stub)
├── data/
│   ├── inputs/              ← 8 JSONs (Śiva, sup, tiṅ, dhātu, ...)
│   └── reference/           ← GOLD corpus (firewall protected)
├── tests/                   ← 328 tests (constitutional, unit, forward,
│                              backward, regression)
├── tools/                   ← sig_benchmark, sig_report, listings, etc.
├── sig/                     ← 9 SIG artifacts (regenerated on demand)
└── webui/                   ← Flask + HTML scaffold (resume later)
```
