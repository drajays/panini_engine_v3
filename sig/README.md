# SIG artifacts (engine-generated)

This directory is **regenerated** from the live engine. Do not hand-edit JSON here.

## Contents

| File | Role |
|------|------|
| `sig_*.json` (9 files) | Graphs, baselines, anomalies, statistics (legacy: **APPLIED**-path edges in `sutra_edge_stats` / `sig_transitions`). |
| `global_sutra_frequencies.json` | Per-sūtra `apply_rule` invocations, status mix, and CPU. |
| `global_sutra_edges.json` | **Chronological** A→B edges (every consecutive pair in the trace, all outcomes). |
| `global_markov_transitions.json` | Empirical transition probabilities (row-normalized from `global_sutra_edges`). |
| `coverage.json` | Sūtra registry coverage snapshot from `engine.coverage_report`. |
| `sig_manifest.json` | **Index:** UTC time, generator id, total derivations ingested, coverage summary, corpora list, and the full artifact filename list. |

**Corpus (default `make sig` / `regenerate_sig_artifacts`):** every `*.json` in `data/reference/subanta_gold/` (all paradigm cells; timed replay of the real `derive` trace) plus, by default, a single *jayati* *tin*anta gold path (steps 1–9) so tripāḍī / *tin*anta edges not hit by *subanta* alone appear in SIG.

## How to regenerate

From the repository root:

```bash
make sig
# or
python3 -m tools.regenerate_sig_artifacts
```

To refresh timing baselines in `sig_baseline.json` only when you intend to:

```bash
python3 -m tools.regenerate_sig_artifacts --freeze
```

(`--freeze` also updates `tests/regression/sig_applied_paths_baseline.json`; see the main README.)

Narrower runs (e.g. one `rama_pullinga.json` only, no *jayati*, custom `--out`) use `python3 -m tools.sig_benchmark` directly; the manifest still lists which files were included. Optional **multi-pipeline** ingests: `--with-samasa-demo` (dik *uttarapūrvā*), `--with-krdanta-pacaka` (*pAcaka* kṛdanta).

**Visualization:** `python3 -m tools.sig_graph_export --format mermaid --out sig/journey.mmd` (or `--format dot`) from `global_sutra_edges.json`.

## Legacy

`regenerate_sig_artifacts` is the one obvious entry; raw `python3 -m tools.sig_benchmark` is for custom `--subanta-corpus` / output paths. Use `--with-jayati` when you need *tin*anta in SIG.
