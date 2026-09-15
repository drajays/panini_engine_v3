# SIG artifacts (engine-generated)

This directory is **regenerated** from the live engine. Do not hand-edit JSON here.

Two graphs live here, built from different corpora and answering different
questions:

| graph | corpus | built by | good for |
|---|---|---|---|
| **curated** — `sig_*.json`, `sutra_*.json`, `global_*.json` | the gold corpora under `data/reference/` (11 corpora · 192 derivations) | `make sig` | timings, baselines, anomaly and critical-path analysis on known-good paradigms |
| **suite-wide** — `suite_sig.json` | every rule firing in the whole pytest suite (19k tests) | `make coverage` | the real interaction picture: 1,619 edges, per-sūtra outcome mix, and the BLOCKED count that measures Art. 15 |

`firing_coverage.json` is the Art. 16 ledger (which sūtras are invoked, which
move the tape); `engine/coverage.py` reads it.

**Gaps are reported, not fatal** (Art. 18). A gold file naming a driver that is
not importable is listed under `gaps` in `sig_manifest.json` and skipped; the
other corpora still ingest.

## Contents

| File | Role |
|------|------|
| `sig_*.json` (9 files) | Graphs, baselines, anomalies, statistics (legacy: **APPLIED**-path edges in `sutra_edge_stats` / `sig_transitions`). |
| `global_sutra_frequencies.json` | Per-sūtra `apply_rule` invocations, status mix, and CPU. |
| `global_sutra_edges.json` | **Chronological** A→B edges (every consecutive pair in the trace, all outcomes). |
| `global_markov_transitions.json` | Empirical transition probabilities (row-normalized from `global_sutra_edges`). |
| `coverage.json` | Sūtra registry coverage snapshot from `engine.coverage_report`. |
| `sig_manifest.json` | **Index:** UTC time, generator id, total derivations ingested, Art. 16 coverage split (registered vs implemented), corpora list, **gaps**, and the artifact filename list. |
| `suite_sig.json` | Suite-wide interaction graph: nodes with their APPLIED/SKIPPED/AUDIT/BLOCKED mix, and chronological A→B edge counts. |
| `firing_coverage.json` | Art. 16 ledger: `invoked` and `moved` sets from the whole suite. |

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
