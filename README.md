# Pāṇini Engine v3.3

**A glass-box, rule-based derivation engine for Pāṇini's Aṣṭādhyāyī.**

## Status

```
  Sūtras implemented   : 35 / 35       (100%, no stubs)
  Rāma paradigm cells  : 24 / 24       (FULL classical match)
  All 10 SutraTypes    : ✓ represented
  Tests                : 341 passing, 0 xfailed, 0 failed
  SIG truth-teller     : active (9 core JSONs + coverage + manifest + path-regression oracle)
```

## The complete rāma paradigm — all 24 cells green

```
           एकवचन           द्विवचन           बहुवचन
प्रथमा    रामः       ✓   रामौ       ✓   रामाः      ✓
द्वितीया  रामम्      ✓   रामौ       ✓   रामान्     ✓
तृतीया    रामेण      ✓   रामाभ्याम् ✓   रामैः      ✓
चतुर्थी   रामाय      ✓   रामाभ्याम् ✓   रामेभ्यः   ✓
पञ्चमी    रामात्     ✓   रामाभ्याम् ✓   रामेभ्यः   ✓
षष्ठी     रामस्य     ✓   रामयोः    ✓   रामाणाम्   ✓
सप्तमी    रामे       ✓   रामयोः    ✓   रामेषु     ✓
सम्बोधन   राम        ✓   रामौ       ✓   रामाः      ✓
```

## Architecture (locked in v3.0; never amended)

- **10-fold SutraType** (SAMJNA · PARIBHASHA · VIDHI · NIYAMA · ATIDESHA ·
  ADHIKARA · PRATISHEDHA · ANUVADA · VIBHASHA · NIPATANA)
- **One-executor-per-type** dispatcher with R1/R2/R3 invariants
- **Aṣṭādhyāyī-kram** strict file layout (no Kaumudī ordering)
- **Data/reference firewall** — gold corpus is test-only
- **Anuvṛtti baked in** — no runtime anuvṛtti layer
- **cond(state)** forbidden from reading paradigm coordinates
  (vibhakti, vacana, puruṣa, lakāra) — enforced by AST tests

## v3.1 amendments (centralized and auditable)

- `R1_EXEMPT` and `NIPATANA_FROZEN` frozensets
- Three-phase model (angakarya → sandhi → tripadi) with `PhaseError`
- `run_to_fixed_point()` bounded sweep with `FixedPointError`
- `BLOCKED` vs `SKIPPED` trace distinction
- `make_stub()` + `coverage_report()`
- `RecipeConflictError` for dual-claim positions
- Full SIG truth-teller (9 v2-compatible JSONs + `coverage.json` + `sig_manifest.json` + path-regression oracle)

## The 35 sūtras (by SutraType)

```
  SAMJNA       (5):  1.1.2 · 1.3.2 · 1.3.3 · 1.3.8 · 1.4.14
  PARIBHASHA   (1):  1.1.56
  NIYAMA       (1):  1.1.47
  ATIDESHA     (1):  1.2.1
  ADHIKARA     (3):  4.1.2 · 6.4.1 · 8.2.1
  PRATISHEDHA  (1):  1.1.6
  ANUVADA      (1):  4.1.1
  VIBHASHA     (1):  8.4.44
  NIPATANA     (1):  6.3.109
  VIDHI       (21):  1.3.9 · 6.1.69 · 6.1.78 · 6.1.87 · 6.1.88 ·
                     6.1.101 · 6.1.102 · 6.1.103 · 6.1.107 ·
                     6.4.148 · 7.1.9 · 7.1.12 · 7.1.13 · 7.1.54 ·
                     7.3.102 · 7.3.103 · 8.2.66 · 8.3.15 · 8.3.59 ·
                     8.4.2
```

## Install and run

```bash
unzip panini_engine_v3.zip
cd panini_engine_v3
pip install -r requirements.txt

# Run the full test suite.
python -m pytest                              # 341 passed

# Regenerate the full `sig/` tree (all `subanta_gold/*.json` + optional *jayati* + coverage + manifest).
make sig
# or:  python3 -m tools.regenerate_sig_artifacts
python -m tools.sutra_sig_report

# List all sūtras by type.
python -m tools.list_sutras_by_type

# Validate all subanta + relevant tinanta gold (auto-discovered under `data/reference/`).
python -m tools.validate_engine_against_source
```

## The truth-teller in action

When you add a sūtra that changes a cell's derivation path (even if the
surface form still matches gold), the SIG regression test fails loudly.
If the change is intentional, refreeze (updates `sig/sig_baseline.json` and the applied-paths baseline in `tests/`):

```bash
python3 -m tools.regenerate_sig_artifacts --freeze
```

## Directory layout

```
panini_engine_v3/
├── CONSTITUTION.md          ← the 10 Articles (supreme law)
├── engine/                  ← fixed core (14 modules)
├── phonology/               ← pure phoneme layer (6 modules)
├── sutras/                  ← content layer (35 sūtras, Aṣṭādhyāyī-kram)
├── pipelines/               ← subanta recipe (tinanta stub)
├── data/
│   ├── inputs/              ← 8 JSONs (Śiva, sup, tiṅ, dhātu, ...)
│   └── reference/           ← gold corpus (firewall protected)
├── tests/                   ← 341 tests (constitutional, unit, forward,
│                              backward, regression)
├── tools/                   ← sig_benchmark, sig_report, listings, etc.
├── sig/                     ← engine JSONs + `coverage.json` + `sig_manifest.json` (see `sig/README.md`)
├── webui/                   ← active Flask web UI (./run_web.sh)
├── xxweb/                   ← DEPRECATED FastAPI prototype (reference only)
└── xxstreamlit_app/         ← DEPRECATED Streamlit UI (reference only)
```

Launch the web UI:

```bash
./run_web.sh          # http://127.0.0.1:5050/
```

## HTTP API

Rule application as a service.  Every response carries the ordered chain of
sūtras the engine actually applied — the surface form is a by-product of the
derivation, never a table lookup.

```bash
pip install -r requirements-api.txt
make api                       # http://127.0.0.1:8000  · docs at /docs
```

| method | path | what it derives |
|--------|------|-----------------|
| GET  | `/v1/health` | registry size + coverage report |
| GET  | `/v1/sutras`, `/v1/sutras/{id}` | sūtra text, padaccheda, anuvṛtti, blocks |
| POST | `/v1/subanta` | one nominal cell (stem · vibhakti · vacana · liṅga) |
| GET  | `/v1/subanta/paradigm` | all 24 cells |
| POST | `/v1/tinanta` | one verbal cell (dhātu · lakāra · prayoga · puruṣa · vacana) |
| GET  | `/v1/tinanta/paradigm` | all 9 cells of one lakāra |
| POST | `/v1/krdanta` | tṛc / ṇvul derivates |
| GET  | `/v1/dhatu`, `/v1/dhatu/{id}` | dhātupāṭha search and lookup |
| GET  | `/v1/translit` | SLP1 → Devanāgarī |

```bash
curl -X POST localhost:8000/v1/subanta \
     -H 'content-type: application/json' \
     -d '{"stem":"hari","vibhakti":3,"vacana":1}'
# → surface हरिणा, plus all 125 trace steps with status and why_dev
```

Every derivation response has the same shape:

```jsonc
{
  "input":   { "stem": "hari", "vibhakti": 3, "vacana": 1, "linga": "pulliṅga" },
  "surface": { "slp1": "hariRA", "dev": "हरिणा" },
  "applied_path": ["1.1.1", "1.1.2", "..."],       // sūtras that fired, in order
  "steps":   [ { "n": 1, "sutra_id": "1.4.14", "status": "APPLIED",
                 "before": {"slp1": "hari", "dev": "हरि"},
                 "after":  {"slp1": "hari", "dev": "हरि"},
                 "why_dev": "..." } ],
  "stats":   { "total": 125, "applied": 21, "audit": 19, "blocked": 0, "skipped": 85 }
}
```

### प्रक्रिया-संशोधनम् — see and correct a prakriyā in one view

`make api` also serves a review page at **`/review`**: derive any subanta,
tiṅanta or kṛdanta form, then flag the exact step where the derivation goes
wrong — expected form, expected sūtra, free note.  Corrections append to
`data/reviews/corrections.jsonl`, one JSON object per line, so they are
greppable, diffable, committable, and ready to become test cases.

```bash
make api                                   # → http://127.0.0.1:8000/review
PANINI_REVIEW_DIR=/mnt/data make api       # write corrections elsewhere
```

| method | path | |
|--------|------|--|
| GET | `/v1/reviews?target=` | open corrections, all or for one derivation |
| POST | `/v1/reviews` | file one (step_n `null` = the final form is wrong) |
| DELETE | `/v1/reviews/{id}` | withdraw one |

The page writes to the local filesystem, so run it locally where the file
lands in the repo.  A hosted container has an ephemeral disk — corrections
made there vanish on restart unless you mount a volume.

The engine needs no third-party package at runtime (no pandas, no Flask):
`Dockerfile` builds a ~40 MB image, imports in ~0.6 s, and answers a
derivation in ~15 ms.  No database, no session state — every request is a
fresh derivation, so the API scales by caching, not by storage.

## What's next (v3.4+)

The complete masculine a-stem paradigm is landed.  Natural next steps:

1. **Other stem types** — i-stem (हरि), u-stem (गुरु), ā-stem feminine (लता),
   ī-stem (नदी), ṛ-stem (पितृ).  Each needs 5–15 additional sūtras; the
   architecture supports them without any core changes.
2. **Tinanta pipeline** — activate `pipelines/tinanta.py` for verb
   conjugation. Needs ~30 additional sūtras across adhyāyas 3 and 6–8.
3. **Kṛdanta + Taddhita** — derivational morphology. Recipe-driven, same
   dispatcher.
4. **Extend webui/** — add new prayoga classes and stem types to the live UI.
