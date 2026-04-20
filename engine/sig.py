"""
engine/sig.py — Sūtra Interaction Graph (truth-teller).
─────────────────────────────────────────────────────────

CONSTITUTION v3.1 amendment (promoted from DEFERRED D3).

Design goal: the SIG is a *truth oracle*.  It catches regressions that
surface-equality misses — a cell may produce the correct form while
taking a different sūtra path than the baseline, which is silently
wrong.  The SIG also catches perf drift (one sūtra suddenly 6× slower),
hub-rule over-reach (one rule acting as a broadcast point to too many
others), and missing / added edges vs a frozen baseline.

v3.1 emits the same nine JSON files v2 produced, using v2's schemas so
tools/sutra_sig_report.py works identically across engine versions:

  sutra_fire_stats.json         — ranked_by_count + total_time_ns
  sutra_edge_stats.json         — top_edges
  sutra_interaction_graph.json  — metadata + nodes + edges
  sig_baseline.json             — per-sūtra timing history (rolling mean)
  sig_critical_path.json        — by_total_time + spiking_rules
  sig_transitions.json          — matrix + high_confidence couplings
  sig_anomalies.json            — slowdowns vs baseline (z-score)
  sig_linguistic.json           — hub_rules with in/out degree
  sutra_next_candidates.json    — k-nearest next sūtras per node

Anomaly detection uses a MIN_SAMPLES floor to avoid flapping on small
corpora.  Z-score threshold is 3.0 for CRITICAL.
"""
from __future__ import annotations

import json
import math
import time
from collections import Counter, defaultdict
from pathlib     import Path
from typing      import Any, Dict, List, Optional, Tuple


_APPLIED_STATUS    = "APPLIED"
_MIN_SAMPLES       = 3          # below this, skip anomaly detection
_CRITICAL_Z        = 3.0
_WARN_Z            = 2.0
_HIGH_CONF_P       = 0.80       # P(B|A) threshold for "high confidence" edge
_HUB_OUT_DEGREE    = 10         # broadcast hub threshold
_HUB_IN_DEGREE     = 10         # sink hub threshold


# ─────────────────────────────────────────────────────────────────
# Trace helpers — pure functions, no engine imports.
# ─────────────────────────────────────────────────────────────────

def extract_applied_path(trace: List[Dict[str, Any]]) -> List[str]:
    """Ordered list of sūtra_ids that APPLIED (skips structural / blocked / skipped)."""
    path: List[str] = []
    for step in trace:
        if step.get("status") != _APPLIED_STATUS:
            continue
        sid = step.get("sutra_id", "")
        if not sid or sid.startswith("__"):
            continue
        path.append(sid)
    return path


def extract_edges(applied_path: List[str]) -> List[Tuple[str, str]]:
    return list(zip(applied_path, applied_path[1:]))


# ─────────────────────────────────────────────────────────────────
# SIGCollector — state for many derivations.
# ─────────────────────────────────────────────────────────────────

class SIGCollector:
    """
    Accumulate fire / edge / timing stats across many derivations.

    Typical usage:
        col = SIGCollector()
        for cell_id in cells:
            state = derive(...)
            col.ingest(cell_id, state.trace)
        col.dump_all(Path("sig/"))
    """

    def __init__(self) -> None:
        # fire_stats[sid] = {"APPLIED": n, "SKIPPED": n, "BLOCKED": n,
        #                    "total_time_ns": int, "samples_ns": [int, ...]}
        self.fire_stats : Dict[str, Dict[str, Any]] = defaultdict(
            lambda: {"APPLIED": 0, "SKIPPED": 0, "BLOCKED": 0,
                     "total_time_ns": 0, "samples_ns": []}
        )
        # edge_stats[(src, dst)] = {"count": n, "paradigms": set}
        self.edge_stats : Dict[Tuple[str, str], Dict[str, Any]] = defaultdict(
            lambda: {"count": 0, "paradigms": set()}
        )
        # Per-cell applied paths (for critical-path & next-candidates).
        self._cell_paths: Dict[str, Counter] = defaultdict(Counter)
        self.paths      : Dict[str, List[str]] = {}
        # Run metadata.
        self.test_count : int = 0

    # ── Ingest ─────────────────────────────────────────────────────

    def ingest(
        self,
        cell_id : str,
        trace   : List[Dict[str, Any]],
        per_step_timing_ns : Optional[Dict[str, List[int]]] = None,
    ) -> None:
        """
        Digest one derivation's trace.  `per_step_timing_ns` is an optional
        {sutra_id: [ns, ns, ...]} map measured by the caller — see
        apply_rule_timed() in this module.
        """
        self.test_count += 1
        for step in trace:
            sid = step.get("sutra_id", "")
            if not sid or sid.startswith("__"):
                continue
            status = step.get("status", _APPLIED_STATUS)
            if status in ("APPLIED", "SKIPPED", "BLOCKED"):
                self.fire_stats[sid][status] += 1

        if per_step_timing_ns:
            for sid, times in per_step_timing_ns.items():
                self.fire_stats[sid]["samples_ns"].extend(times)
                self.fire_stats[sid]["total_time_ns"] += sum(times)

        applied = extract_applied_path(trace)
        self.paths[cell_id] = applied
        self._cell_paths[cell_id][tuple(applied)] += 1
        for src, dst in extract_edges(applied):
            e = self.edge_stats[(src, dst)]
            e["count"] += 1
            e["paradigms"].add(cell_id)

    # ── Dump: individual files ─────────────────────────────────────

    def sutra_fire_stats(self) -> Dict[str, Any]:
        """v2 schema: { ranked_by_count: [ {id, fire_count, total_time_ns}, ... ] }"""
        ranked = [
            {
                "id"            : sid,
                "fire_count"    : stats["APPLIED"],
                "total_time_ns" : stats["total_time_ns"],
            }
            for sid, stats in self.fire_stats.items()
            if stats["APPLIED"] > 0
        ]
        ranked.sort(key=lambda r: (-r["fire_count"], -r["total_time_ns"], r["id"]))
        return {"ranked_by_count": ranked}

    def sutra_edge_stats(self) -> Dict[str, Any]:
        """v2 schema: { top_edges: [ {source, target, weight}, ... ] }"""
        top = [
            {"source": s, "target": d, "weight": e["count"]}
            for (s, d), e in self.edge_stats.items()
        ]
        top.sort(key=lambda r: (-r["weight"], r["source"], r["target"]))
        return {"top_edges": top}

    def sutra_interaction_graph(self) -> Dict[str, Any]:
        """v2 schema: { metadata, nodes:[{id,fire_count,total_time_ns,avg_time_ns}],
                        edges:[{source,target,weight,paradigms}] }"""
        nodes = []
        for sid, stats in self.fire_stats.items():
            fc = stats["APPLIED"]
            tot = stats["total_time_ns"]
            nodes.append({
                "id"            : sid,
                "fire_count"    : fc,
                "total_time_ns" : tot,
                "avg_time_ns"   : int(tot / fc) if fc else 0,
            })
        nodes.sort(key=lambda n: (-n["fire_count"], n["id"]))
        edges = []
        for (s, d), e in self.edge_stats.items():
            edges.append({
                "source"    : s,
                "target"    : d,
                "weight"    : e["count"],
                "paradigms" : sorted(e["paradigms"]),
            })
        edges.sort(key=lambda r: (-r["weight"], r["source"], r["target"]))
        return {
            "metadata": {
                "generated_by": "SIG",
                "version"     : "3.1",
                "test_count"  : self.test_count,
            },
            "nodes": nodes,
            "edges": edges,
        }

    def sig_critical_path(self) -> Dict[str, Any]:
        """Ranks sūtras by total time; flags spiking ones (p95 >> median)."""
        by_tot: List[Dict[str, Any]] = []
        spiking: List[Dict[str, Any]] = []

        # Overall engine time for pct calculation.
        total_engine_ns = sum(s["total_time_ns"] for s in self.fire_stats.values())

        for sid, stats in self.fire_stats.items():
            samples = stats["samples_ns"]
            fc      = stats["APPLIED"]
            if fc == 0:
                continue
            tot_ns  = stats["total_time_ns"]
            avg_ns  = tot_ns / fc if fc else 0.0
            if samples:
                samples_sorted = sorted(samples)
                median = samples_sorted[len(samples_sorted) // 2]
                p95idx = max(0, int(0.95 * (len(samples_sorted) - 1)))
                p95    = samples_sorted[p95idx]
                is_spiking = (p95 > 3 * median) if median else False
            else:
                median, p95, is_spiking = int(avg_ns), int(avg_ns), False
            row = {
                "sutra_id"                  : sid,
                "fire_count"                : fc,
                "total_time_ns"             : tot_ns,
                "avg_time_ns"               : round(avg_ns, 1),
                "median_time_ns"            : float(median),
                "p95_time_ns"               : float(p95),
                "is_spiking"                : is_spiking,
                "pct_of_total_engine_time"  : (
                    round(100.0 * tot_ns / total_engine_ns, 2)
                    if total_engine_ns else 0.0
                ),
            }
            by_tot.append(row)
            if is_spiking:
                spiking.append(row)
        by_tot.sort(key=lambda r: -r["total_time_ns"])
        spiking.sort(key=lambda r: -r["p95_time_ns"])
        return {"by_total_time": by_tot, "spiking_rules": spiking}

    def sig_transitions(self, k: int = 8, min_p: float = 0.05) -> Dict[str, Any]:
        """
        matrix[src][dst] = count; high_confidence = edges where P(dst|src) >= threshold.
        """
        matrix: Dict[str, Dict[str, int]] = defaultdict(dict)
        row_totals: Dict[str, int] = defaultdict(int)
        for (s, d), e in self.edge_stats.items():
            matrix[s][d] = e["count"]
            row_totals[s] += e["count"]

        high_conf: List[Dict[str, Any]] = []
        for src, outs in matrix.items():
            tot = row_totals[src]
            if tot == 0:
                continue
            for dst, cnt in outs.items():
                p = cnt / tot
                if p >= _HIGH_CONF_P:
                    high_conf.append({
                        "from"        : src,
                        "to"          : dst,
                        "count"       : cnt,
                        "probability" : round(p, 3),
                    })
        high_conf.sort(key=lambda r: -r["probability"])
        return {
            "k"                : k,
            "min_transition_p" : min_p,
            "matrix"           : {s: dict(d) for s, d in matrix.items()},
            "high_confidence"  : high_conf,
        }

    def sig_linguistic(self) -> Dict[str, Any]:
        """Hub detection: rules with unusually high in- or out-degree."""
        in_deg: Dict[str, int]  = defaultdict(int)
        out_deg: Dict[str, int] = defaultdict(int)
        for (s, d), e in self.edge_stats.items():
            in_deg[d]  += 1
            out_deg[s] += 1

        hubs: List[Dict[str, Any]] = []
        seen = set()
        for sid in set(list(in_deg.keys()) + list(out_deg.keys())):
            out_d = out_deg.get(sid, 0)
            in_d  = in_deg.get(sid, 0)
            fc    = self.fire_stats.get(sid, {"APPLIED": 0})["APPLIED"]
            hub_type = None
            if out_d >= _HUB_OUT_DEGREE:
                hub_type = "broadcast"
            elif in_d >= _HUB_IN_DEGREE:
                hub_type = "sink"
            if hub_type:
                hubs.append({
                    "sutra_id"   : sid,
                    "in_degree"  : in_d,
                    "out_degree" : out_d,
                    "fire_count" : fc,
                    "hub_type"   : hub_type,
                })
                seen.add(sid)
        hubs.sort(key=lambda r: -(r["out_degree"] + r["in_degree"]))
        return {"hub_rules": hubs}

    def sutra_next_candidates(self, k: int = 8) -> Dict[str, Any]:
        """For each node, the top-k most frequent next sūtras."""
        by_src: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        for (s, d), e in self.edge_stats.items():
            by_src[s].append((d, e["count"]))
        cands: Dict[str, List[str]] = {}
        for s, pairs in by_src.items():
            pairs.sort(key=lambda p: -p[1])
            cands[s] = [d for d, _ in pairs[:k]]
        return {"k": k, "candidates": cands}

    # ── Baseline & anomalies ───────────────────────────────────────

    def sig_baseline(self, prior: Optional[Dict[str, Any]] = None,
                     history_depth: int = 20) -> Dict[str, Any]:
        """
        Rolling per-sūtra timing baseline.  Each sūtra carries a
        history_ns list of its recent avg times; new runs prepend.
        Matches v2's shape: { sid: {history_ns: [...], mean, std} }.
        """
        prior = prior or {}
        out: Dict[str, Any] = {}
        for sid, stats in self.fire_stats.items():
            fc = stats["APPLIED"]
            if fc == 0:
                continue
            avg_ns = stats["total_time_ns"] / fc
            entry = prior.get(sid, {"history_ns": []})
            history = [avg_ns] + list(entry.get("history_ns", []))
            history = history[:history_depth]
            mean = sum(history) / len(history)
            var  = sum((x - mean) ** 2 for x in history) / len(history)
            std  = math.sqrt(var)
            out[sid] = {
                "history_ns" : history,
                "mean"       : mean,
                "std"        : std,
            }
        return out

    def sig_anomalies(self, baseline: Dict[str, Any]) -> Dict[str, Any]:
        """
        Flag sūtras whose current avg deviates from baseline by
        z-score >= _WARN_Z (z >= _CRITICAL_Z is CRITICAL).
        """
        anomalies: List[Dict[str, Any]] = []
        for sid, stats in self.fire_stats.items():
            fc = stats["APPLIED"]
            if fc == 0:
                continue
            base = baseline.get(sid)
            if not base:
                continue
            hist = base.get("history_ns", [])
            if len(hist) < _MIN_SAMPLES:
                continue
            mean = base.get("mean", 0.0)
            std  = base.get("std", 0.0)
            if std == 0:
                continue
            cur_avg = stats["total_time_ns"] / fc
            z       = (cur_avg - mean) / std
            if abs(z) < _WARN_Z:
                continue
            severity = "CRITICAL" if abs(z) >= _CRITICAL_Z else "WARN"
            slowdown = cur_avg / mean if mean else 0.0
            anomalies.append({
                "sutra_id"        : sid,
                "current_avg_ns"  : round(cur_avg, 1),
                "baseline_mean_ns": round(mean, 1),
                "z_score"         : round(z, 2),
                "slowdown_factor" : round(slowdown, 2),
                "severity"        : severity,
            })
        anomalies.sort(key=lambda r: -abs(r["z_score"]))
        return {
            "run_test_count" : self.test_count,
            "anomalies"      : anomalies,
        }

    # ── Dump orchestrator ──────────────────────────────────────────

    def dump_all(self, out_dir: Path,
                 prior_baseline: Optional[Dict[str, Any]] = None) -> Dict[str, Path]:
        """
        Write all nine JSON files under `out_dir`.  Returns a map
        {logical_name → filepath}.  Creates out_dir if absent.
        """
        out_dir.mkdir(parents=True, exist_ok=True)
        files: Dict[str, Path] = {}

        def _write(name: str, data: Any) -> None:
            p = out_dir / name
            p.write_text(json.dumps(data, ensure_ascii=False, indent=2,
                                    sort_keys=True), encoding="utf-8")
            files[name] = p

        _write("sutra_fire_stats.json",        self.sutra_fire_stats())
        _write("sutra_edge_stats.json",        self.sutra_edge_stats())
        _write("sutra_interaction_graph.json", self.sutra_interaction_graph())
        _write("sig_critical_path.json",       self.sig_critical_path())
        _write("sig_transitions.json",         self.sig_transitions())
        _write("sig_linguistic.json",          self.sig_linguistic())
        _write("sutra_next_candidates.json",   self.sutra_next_candidates())

        baseline = self.sig_baseline(prior_baseline)
        _write("sig_baseline.json",            baseline)
        _write("sig_anomalies.json",           self.sig_anomalies(
            prior_baseline or {}
        ))

        return files


# ─────────────────────────────────────────────────────────────────
# Timed apply wrapper — optional helper for SIG benchmarking.
# ─────────────────────────────────────────────────────────────────

def apply_rule_timed(sutra_id: str, state, per_step_times: Dict[str, List[int]]):
    """
    Thin timing wrapper around engine.apply_rule.  Measures wall time
    in ns and appends to `per_step_times[sutra_id]`.  Returns the new
    state exactly as apply_rule does.

    Why not patch apply_rule itself: the dispatcher must stay pure
    per CONSTITUTION Article 5.  Timing is observer-only and lives
    in the SIG layer.
    """
    from engine.dispatcher import apply_rule  # local — avoid cycle
    t0 = time.perf_counter_ns()
    new_state = apply_rule(sutra_id, state)
    elapsed = time.perf_counter_ns() - t0
    per_step_times.setdefault(sutra_id, []).append(elapsed)
    return new_state
