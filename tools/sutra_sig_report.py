#!/usr/bin/env python3
"""
tools/sutra_sig_report.py — Truth-teller summary of SIG artifacts.
────────────────────────────────────────────────────────────────────

Reads the nine JSON files produced by engine.sig.SIGCollector.dump_all()
and prints a compact human-readable audit.  Useful after every test run:

    python -m tools.sig_benchmark        # produces ./sig/*.json
    python -m tools.sutra_sig_report     # reads ./sig/*.json and summarizes

Adapted from v2's report.  v3 writes to ./sig/ instead of ./artifacts/.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def _load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None


def _section(title: str) -> None:
    print(f"\n§ {title}")
    print("─" * 72)


def _print_fire_stats(d):
    if not d:
        print("  [sutra_fire_stats.json not found]")
        return
    top = d.get("ranked_by_count", [])[:15]
    for r in top:
        print(f"  {r['id']:<12}  fire={r['fire_count']:>5}  "
              f"total_ns={r['total_time_ns']:>12}")
    zf = d.get("zero_fire_cpu_hot", [])[:8]
    if zf:
        print("  Zero-APPLIED but CPU-hot (evaluated, skipped/blocked):")
        for r in zf:
            print(f"    {r['id']:<12}  total_ns={r['total_time_ns']:>12}  "
                  f"sk={r.get('skipped',0)}  bl={r.get('blocked',0)}")


def _print_edge_stats(d):
    if not d:
        print("  [sutra_edge_stats.json not found]")
        return
    for e in d.get("top_edges", [])[:15]:
        print(f"  {e['source']:<12} → {e['target']:<12}  weight={e['weight']}")


def _print_transitions(d):
    if not d:
        print("  [sig_transitions.json not found]")
        return
    hi = d.get("high_confidence", [])[:15]
    if not hi:
        print("  (no high-confidence couplings yet)")
        return
    for h in hi:
        print(f"  {h['from']:<12} → {h['to']:<12}  P={h['probability']:.2f}  "
              f"n={h['count']}")


def _print_critical(d):
    if not d:
        print("  [sig_critical_path.json not found]")
        return
    for r in d.get("by_total_time", [])[:10]:
        print(f"  {r['sutra_id']:<12}  total_ns={r['total_time_ns']:>12}  "
              f"%total={r['pct_of_total_engine_time']:>5.1f}")
    zf = d.get("by_total_time_zero_fire", [])
    if zf:
        print("  High CPU, zero APPLIED (timed-eval cost on skips/blocks):")
        for r in zf[:5]:
            print(f"    {r['sutra_id']:<12}  total_ns={r['total_time_ns']:>12}")
    spikes = d.get("spiking_rules", [])
    if spikes:
        print("  Spiking (p95 > 3× median):")
        for r in spikes[:5]:
            print(f"    {r['sutra_id']:<12}  p95={r['p95_time_ns']}  "
                  f"median={r['median_time_ns']}")


def _print_anomalies(d):
    if not d:
        print("  [sig_anomalies.json not found]")
        return
    n = len(d.get("anomalies", []))
    if n == 0:
        print("  ✓ no anomalies (all sūtras within baseline tolerance)")
        return
    print(f"  {n} anomalies out of {d.get('run_test_count',0)} test runs:")
    for a in d["anomalies"][:10]:
        print(f"    [{a['severity']:<8}] {a['sutra_id']:<12}  "
              f"z={a['z_score']:+6.2f}  slowdown={a['slowdown_factor']:.2f}×")
    prof = d.get("cell_cpu_profile") or {}
    if prof.get("derivations_timed"):
        print("  Per-derivation wall time (sum of timed apply_rule steps):")
        print(f"    derivations_timed={prof['derivations_timed']!r}  "
              f"median_total_ns={prof.get('median_total_ns')!r}  "
              f"max={prof.get('max_total_ns')!r}")
    casc = d.get("cascade_slow_cells") or []
    if casc:
        print("  Pipeline cascade (cells >> median CPU):")
        for c in casc[:6]:
            print(f"    [{c['severity']:<8}] {c['cell_id']!r}  "
                  f"vs_median={c['vs_median']:.2f}×")


def _print_hubs(d):
    if not d:
        print("  [sig_linguistic.json not found]")
        return
    hubs = d.get("hub_rules", [])
    if not hubs:
        print("  (no hub rules detected yet)")
        return
    for h in hubs[:10]:
        print(f"  [{h['hub_type']:<9}] {h['sutra_id']:<12}  "
              f"in={h['in_degree']:>3}  out={h['out_degree']:>3}  "
              f"fires={h['fire_count']}")


def _print_coverage(d):
    if not d:
        print("  [coverage.json not found]")
        return
    print(f"  Total sūtras  : {d['total']}")
    print(f"  Implemented   : {d['implemented']} ({d['coverage_pct']}%)")
    print(f"  Stubs         : {d['stubs']}")
    for tname, stats in sorted(d.get("by_type", {}).items()):
        print(f"    {tname:<14} impl={stats['implemented']:>3} / "
              f"{stats['total']:>3}  ({stats['coverage_pct']:>5.1f}%)")


def main(argv=None) -> int:
    root = Path(argv[1]) if argv and len(argv) > 1 else Path("sig")

    print("═" * 72)
    print(f"  PĀṆINI ENGINE v3 — SIG TRUTH REPORT  ({root})")
    print("═" * 72)

    _section("§1  FIRE STATS (ranked by count)")
    _print_fire_stats(_load(root / "sutra_fire_stats.json"))

    _section("§2  EDGE STATS (top transitions by weight)")
    _print_edge_stats(_load(root / "sutra_edge_stats.json"))

    _section("§3  HIGH-CONFIDENCE COUPLINGS (P ≥ 0.80)")
    _print_transitions(_load(root / "sig_transitions.json"))

    _section("§4  CRITICAL PATH (by total engine time)")
    _print_critical(_load(root / "sig_critical_path.json"))

    _section("§5  ANOMALIES vs BASELINE (z ≥ 2.0)")
    _print_anomalies(_load(root / "sig_anomalies.json"))

    _section("§6  HUB RULES (broadcast / sink)")
    _print_hubs(_load(root / "sig_linguistic.json"))

    _section("§7  COVERAGE")
    _print_coverage(_load(root / "coverage.json"))

    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
