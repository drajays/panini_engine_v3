#!/usr/bin/env python3
"""
tools/sig_benchmark.py — Run paradigm cells, collect SIG, write JSON.
───────────────────────────────────────────────────────────────────────

Usage:
    python -m tools.sig_benchmark                  # uses rama gold as input set
    python -m tools.sig_benchmark --out sig/
    python -m tools.sig_benchmark --freeze         # freeze as new baseline

Modes:
    (default)  Collect SIG, diff vs existing sig/sig_baseline.json
               (if present), exit code 0 iff no CRITICAL anomalies.
    --freeze   Overwrite sig/sig_baseline.json with this run's timings.

This is the v3.1 answer to v2's benchmark.  We don't compare schedulers
(we have one scheduler); we compare THIS RUN to the LAST KNOWN GOOD run.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import sutras  # noqa: F401 — trigger registry fill
from engine          import SIGCollector, SUTRA_REGISTRY, coverage_report
from engine.sig      import apply_rule_timed
from pipelines.subanta import build_initial_state


# The derivation recipe for रRAMA subanta, one step per apply_rule.
# Mirrors pipelines/subanta.py but uses apply_rule_timed so SIG gets
# per-sūtra timings.
_RECIPE = [
    "1.4.14", "4.1.1", "1.1.1", "1.1.2", "1.1.3", "1.1.7", "1.1.8", "1.1.9", "1.1.10", "1.1.11", "1.1.12", "1.1.13", "1.1.14", "1.1.100", "1.1.15", "1.1.16", "1.1.17", "1.1.18", "1.1.19", "1.1.20", "1.1.21", "1.1.22", "1.1.23", "1.1.24",
    "4.1.2",
    "1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8", "1.3.9",
    "6.4.1",
    "6.1.69",
    "7.1.12", "7.1.13",
    "7.1.9",                                     # v3.2: ato bhisa ais
    "7.1.54", "1.3.9",
    "7.3.103", "7.3.102",                        # bahuvacane jhalyet (before supi ca)
    "6.4.148",
    "6.1.102", "6.1.103",                        # v3.2: jas/Sas substitutions
    "6.1.78", "6.1.107", "6.1.87", "6.1.88", "6.1.101",
    "8.2.1", "8.2.66", "8.3.15", "8.3.59", "8.4.2",
]


def _derive_with_timing(stem: str, v: int, vv: int, col_times):
    s = build_initial_state(stem, v, vv)
    for sid in _RECIPE:
        s = apply_rule_timed(sid, s, col_times)
    return s


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=_ROOT / "sig",
                    help="output directory for SIG JSON files")
    ap.add_argument("--freeze", action="store_true",
                    help="overwrite sig_baseline.json with this run's timings")
    ap.add_argument("--stem", default="rAma", help="stem to derive (SLP1)")
    args = ap.parse_args(argv)

    # Load prior baseline (if any).
    prior_baseline_path = args.out / "sig_baseline.json"
    prior_baseline = None
    if prior_baseline_path.exists() and not args.freeze:
        prior_baseline = json.loads(
            prior_baseline_path.read_text(encoding="utf-8")
        )

    col = SIGCollector()

    # Run all 24 cells.
    for v in range(1, 9):
        for vv in range(1, 4):
            cell = f"{args.stem}:{v}-{vv}"
            per_step_times = {}
            state = _derive_with_timing(args.stem, v, vv, per_step_times)
            col.ingest(cell, state.trace, per_step_timing_ns=per_step_times)

    # Dump all nine JSON files.
    files = col.dump_all(args.out, prior_baseline=prior_baseline)

    # Dump coverage.json too.
    cov = coverage_report(SUTRA_REGISTRY)
    (args.out / "coverage.json").write_text(
        json.dumps(cov, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    files["coverage.json"] = args.out / "coverage.json"

    # On --freeze, also write the applied-paths baseline that
    # tests/regression/test_sig_baseline.py reads.  This is what makes
    # SIG into a true truth-teller: surface-correct but path-changed
    # is a caught regression.
    #
    # We use pipelines.subanta.derive (the REAL pipeline) here rather
    # than _derive_with_timing + _RECIPE so the baseline matches what
    # the test module actually invokes.  They would otherwise drift.
    if args.freeze:
        from engine.sig       import extract_applied_path
        from pipelines.subanta import derive as real_derive
        applied_paths = {}
        for v in range(1, 9):
            for vv in range(1, 4):
                cell = f"{v}-{vv}"
                state = real_derive(args.stem, v, vv)
                applied_paths[cell] = {
                    "applied_path": extract_applied_path(state.trace),
                }
        baseline_path = (_ROOT / "tests" / "regression" /
                         "sig_applied_paths_baseline.json")
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        baseline_path.write_text(
            json.dumps(applied_paths, ensure_ascii=False,
                       indent=2, sort_keys=True),
            encoding="utf-8",
        )
        print(f"  ✓ applied-paths baseline frozen at {baseline_path}")

    # Exit-code policy: fail on CRITICAL anomalies (regression oracle).
    anomalies = json.loads(
        (args.out / "sig_anomalies.json").read_text(encoding="utf-8")
    )
    critical = [a for a in anomalies.get("anomalies", [])
                if a.get("severity") == "CRITICAL"]

    print(f"\n{'═' * 60}")
    print(f"  SIG benchmark complete  ({col.test_count} derivations)")
    print(f"{'═' * 60}")
    print(f"  Wrote {len(files)} files to {args.out}/")
    for name in sorted(files):
        print(f"    {name}")
    print(f"\n  Coverage      : {cov['implemented']}/{cov['total']} "
          f"({cov['coverage_pct']}%)")
    print(f"  Anomalies     : {len(anomalies.get('anomalies', []))}"
          f" ({len(critical)} CRITICAL)")
    if args.freeze:
        print(f"\n  ✓ baseline frozen at {prior_baseline_path}")
        return 0
    if critical:
        print("\n  ✗ CRITICAL regressions vs baseline — see sig_anomalies.json")
        return 2
    print("\n  ✓ no critical regressions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
