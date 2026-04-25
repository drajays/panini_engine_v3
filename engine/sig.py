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
  global_sutra_frequencies.json — all apply_rule invocations + time per sūtra
  global_sutra_edges.json      — chronological A→B edge weights
  global_markov_transitions.json — P(B|A) from chrono edges

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

from engine.trace import extract_chronological_sutra_sequence


_APPLIED_STATUS    = "APPLIED"
_APPLIED_VACUOUS   = "APPLIED_VACUOUS"
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
        st = step.get("status")
        if st not in (_APPLIED_STATUS, _APPLIED_VACUOUS):
            continue
        sid = step.get("sutra_id", "")
        if not sid or sid.startswith("__"):
            continue
        path.append(sid)
    return path


def extract_edges(applied_path: List[str]) -> List[Tuple[str, str]]:
    return list(zip(applied_path, applied_path[1:]))


def replay_subanta_trace(
    stem_slp1 : str,
    vibhakti  : int,
    vacana    : int,
    reference_trace: List[Dict[str, Any]],
    *,
    linga     : str = "pulliṅga",
    per_step_times: Optional[Dict[str, List[int]]] = None,
) -> Any:
    """
    Deterministically re-execute the subanta *apply_rule* sequence that is
    recorded in ``reference_trace`` (e.g. from ``pipelines.subanta.derive``),
    so wall times can be measured without the scheduler. Structural ``__MERGE__``
    is replayed with ``pipelines.subanta``'s pada merge. Used for SIG: every
    scheduled sūtra — including *SKIPPED* / *BLOCKED* rows that still ran
    ``cond`` / gates — is timed when ``per_step_times`` is passed.
    """
    from pipelines.subanta import build_initial_state, _pada_merge

    s = build_initial_state(stem_slp1, vibhakti, vacana, linga)
    for step in reference_trace:
        sid = step.get("sutra_id", "")
        if sid == "__MERGE__":
            _pada_merge(s)
        elif sid and not sid.startswith("__"):
            if per_step_times is not None:
                s = apply_rule_timed(sid, s, per_step_times)
            else:
                from engine.dispatcher import apply_rule
                s = apply_rule(sid, s)
    return s


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
        # fire_stats[sid] = {"APPLIED": n, "AUDIT": n, "SKIPPED": n, "BLOCKED": n,
        #                    "total_time_ns": int, "samples_ns": [int, ...]}
        self.fire_stats : Dict[str, Dict[str, Any]] = defaultdict(
            lambda: {"APPLIED": 0, "AUDIT": 0, "SKIPPED": 0, "BLOCKED": 0,
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
        # Per-derivation CPU (sum of timed steps), when ingest gets timings.
        self.cell_total_time_ns: Dict[str, int] = {}
        # Every ``apply_rule`` in order (A→B), for global Markov / mermaid
        self.chrono_edge_stats: Dict[Tuple[str, str], Dict[str, Any]] = defaultdict(
            lambda: {"count": 0, "paradigms": set()}
        )
        self.apply_invocation_count: Dict[str, int] = defaultdict(int)

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
            self.apply_invocation_count[sid] += 1
            status = step.get("status", _APPLIED_STATUS)
            if status == _APPLIED_VACUOUS:
                self.fire_stats[sid]["APPLIED"] += 1
            elif status in ("APPLIED", "AUDIT", "SKIPPED", "BLOCKED"):
                self.fire_stats[sid][status] += 1

        chrono_seq = extract_chronological_sutra_sequence(trace)
        for a, b in zip(chrono_seq, chrono_seq[1:]):
            e = self.chrono_edge_stats[(a, b)]
            e["count"] += 1
            e["paradigms"].add(cell_id)

        if per_step_timing_ns:
            cell_ns = 0
            for times in per_step_timing_ns.values():
                cell_ns += sum(times)
            self.cell_total_time_ns[cell_id] = cell_ns
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
        """v2 schema + ranked_by_cpu (includes zero-APPLIED if timed)."""
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

        # Rules that consumed CPU in timed replay but did not *apply* a vidhi
        # (SKIPPED / BLOCKED / vacuous) — “zero-fire but high-cost” telemetry.
        cpu_ranked = [
            {
                "id"              : sid,
                "applied"         : stats["APPLIED"],
                "skipped"         : stats.get("SKIPPED", 0),
                "blocked"         : stats.get("BLOCKED", 0),
                "total_time_ns"   : stats["total_time_ns"],
            }
            for sid, stats in self.fire_stats.items()
            if stats["total_time_ns"] > 0
        ]
        cpu_ranked.sort(
            key=lambda r: (-r["total_time_ns"], -r["applied"], r["id"])
        )

        zero_apply_hot = [
            {**r, "note": "evaluated in recipe but never APPLIED; still costs CPU."}
            for r in cpu_ranked
            if r["applied"] == 0 and r["total_time_ns"] > 0
        ]

        return {
            "ranked_by_count"        : ranked,
            "ranked_by_total_cpu_ns" : cpu_ranked,
            "zero_fire_cpu_hot"      : zero_apply_hot,
        }

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
        # Non-APPLIED (in trace) but still cost wall time in timed replay
        no_apply: List[Dict[str, Any]] = []
        for sid, stats in self.fire_stats.items():
            fc = stats["APPLIED"]
            tot = stats["total_time_ns"]
            if fc or not tot:
                continue
            no_apply.append({
                "sutra_id"     : sid,
                "total_time_ns": tot,
                "skipped"      : stats.get("SKIPPED", 0),
                "blocked"      : stats.get("BLOCKED", 0),
            })
        no_apply.sort(key=lambda r: -r["total_time_ns"])
        return {
            "by_total_time"         : by_tot,
            "spiking_rules"         : spiking,
            "by_total_time_zero_fire": no_apply[:20],
        }

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

    def global_sutra_frequencies(self) -> Dict[str, Any]:
        """All ``apply_rule`` invocations and CPU per sūtra (cross-pipeline)."""
        all_ids = sorted(
            set(self.apply_invocation_count) | set(self.fire_stats), key=str
        )
        rows: List[Dict[str, Any]] = []
        for sid in all_ids:
            inv = int(self.apply_invocation_count.get(sid, 0))
            fs = self.fire_stats.get(sid, {})
            rows.append({
                "sutra_id"                 : sid,
                "apply_rule_invocations"     : inv,
                "APPLIED"                  : int(fs.get("APPLIED", 0)),
                "SKIPPED"                  : int(fs.get("SKIPPED", 0)),
                "BLOCKED"                  : int(fs.get("BLOCKED", 0)),
                "total_time_ns"            : int(fs.get("total_time_ns", 0)),
            })
        rows.sort(key=lambda r: (-r["apply_rule_invocations"], r["sutra_id"]))
        return {
            "description": (
                "Per sūtra: how often ``apply_rule`` visited it, status breakdown, "
                "and accumulated wall time (from timed replays if provided)."
            ),
            "sutras": rows,
        }

    def global_sutra_edges(self) -> Dict[str, Any]:
        """Chronological A → B (every pair of consecutive ``apply_rule`` calls)."""
        edges = [
            {
                "source"      : s,
                "target"      : d,
                "weight"      : e["count"],
                "derivations" : sorted(e["paradigms"]),
            }
            for (s, d), e in self.chrono_edge_stats.items()
        ]
        edges.sort(key=lambda r: (-r["weight"], r["source"], r["target"]))
        return {
            "description": (
                "Global directed edges from the full sūtra invocation order "
                "(*subanta* / *tin*anta* / *samāsa* / … combined in ``ingest``)."
            ),
            "edges": edges,
        }

    def global_markov_transitions(self) -> Dict[str, Any]:
        """P(target | source) = weight / row_total over chronological edges."""
        row_tot: Dict[str, int] = defaultdict(int)
        for (s, _d), e in self.chrono_edge_stats.items():
            row_tot[s] += e["count"]
        matrix: Dict[str, Dict[str, float]] = {}
        for (s, d), e in self.chrono_edge_stats.items():
            tot = row_tot.get(s, 0)
            if not tot:
                continue
            matrix.setdefault(s, {})[d] = round(e["count"] / tot, 6)
        flat: List[Dict[str, Any]] = []
        for (s, d), e in self.chrono_edge_stats.items():
            tot = row_tot.get(s, 0)
            p = (e["count"] / tot) if tot else 0.0
            flat.append({
                "from"            : s,
                "to"              : d,
                "count"           : e["count"],
                "P_to_given_from" : round(p, 6),
                "row_total"       : tot,
            })
        flat.sort(key=lambda r: (-r["count"], r["from"], r["to"]))
        return {
            "description": (
                "Row-stochastic view of the empirical transition graph "
                "(*from* = conditioning sūtra)."
            ),
            "row_totals" : {k: row_tot[k] for k in sorted(row_tot)},
            "matrix"     : {k: dict(v) for k, v in sorted(matrix.items())},
            "transitions": flat,
        }

    def _cascade_slow_cells(self) -> List[Dict[str, Any]]:
        """Flag derivations much slower than cohort median (pipeline-wide drag)."""
        tmap = self.cell_total_time_ns
        if not tmap or len(tmap) < 3:
            return []
        times = sorted(tmap.values())
        med = times[len(times) // 2]
        if not med:
            return []
        out: List[Dict[str, Any]] = []
        for cid, ns in tmap.items():
            ratio = ns / med
            if ratio >= 2.5:
                out.append({
                    "cell_id"     : cid,
                    "total_ns"    : ns,
                    "median_ns"   : med,
                    "vs_median"   : round(ratio, 2),
                    "severity"    : "CRITICAL" if ratio >= 4.0 else "WARN",
                })
        out.sort(key=lambda r: -r["vs_median"])
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

        times = list(self.cell_total_time_ns.values())
        cell_profile: Dict[str, Any] = {
            "derivations_timed": len(self.cell_total_time_ns),
        }
        if times:
            times_sorted = sorted(times)
            cell_profile["median_total_ns"] = times_sorted[len(times_sorted) // 2]
            cell_profile["max_total_ns"]    = max(times)
            cell_profile["min_total_ns"]    = min(times)
        return {
            "run_test_count"  : self.test_count,
            "anomalies"       : anomalies,
            "cell_cpu_profile": cell_profile,
            "cascade_slow_cells": self._cascade_slow_cells(),
        }

    # ── Dump orchestrator ──────────────────────────────────────────

    def dump_all(self, out_dir: Path,
                 prior_baseline: Optional[Dict[str, Any]] = None) -> Dict[str, Path]:
        """
        Write legacy SIG JSONs plus three **global** telemetry files under ``out_dir``.
        Returns ``{logical_name → filepath}``.  Creates ``out_dir`` if absent.
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
        _write("global_sutra_frequencies.json", self.global_sutra_frequencies())
        _write("global_sutra_edges.json",     self.global_sutra_edges())
        _write("global_markov_transitions.json", self.global_markov_transitions())

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
