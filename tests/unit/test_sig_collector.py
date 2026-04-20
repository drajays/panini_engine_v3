"""
tests/unit/test_sig_collector.py
──────────────────────────────────

Tests for the SIG truth-teller (v3.1 amendment).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from engine            import SIGCollector
from engine.sig        import extract_applied_path, extract_edges


def _applied(sid, before="a", after="b"):
    return {
        "sutra_id"    : sid,
        "sutra_type"  : "VIDHI",
        "status"      : "APPLIED",
        "form_before" : before,
        "form_after"  : after,
        "why_dev"     : "परीक्षा",
    }


def _blocked(sid):
    return {
        "sutra_id"    : sid,
        "status"      : "BLOCKED",
        "gate_reason" : "PRATISHEDHA-BLOCKED",
    }


def _structural(sid):
    return {"sutra_id": sid, "status": "APPLIED"}


def test_extract_applied_path_skips_structural_and_blocked():
    trace = [
        _applied("1.1.2"),
        _blocked("6.1.87"),
        _structural("__MERGE__"),
        _applied("1.3.9"),
        _structural("__PHASE__"),
    ]
    assert extract_applied_path(trace) == ["1.1.2", "1.3.9"]


def test_extract_edges():
    assert extract_edges(["A", "B", "C"]) == [("A", "B"), ("B", "C")]
    assert extract_edges(["A"]) == []
    assert extract_edges([]) == []


def test_collector_ingests_fire_stats():
    col = SIGCollector()
    col.ingest("cell1", [_applied("1.1.2"), _applied("1.3.9"),
                         _blocked("6.1.87")])
    stats = col.sutra_fire_stats()
    ids = [r["id"] for r in stats["ranked_by_count"]]
    assert "1.1.2" in ids
    assert "1.3.9" in ids
    # 1.1.2 and 1.3.9 fired; 6.1.87 didn't (only blocked).
    fire_of = {r["id"]: r["fire_count"] for r in stats["ranked_by_count"]}
    assert fire_of["1.1.2"] == 1
    assert fire_of["1.3.9"] == 1
    assert "6.1.87" not in fire_of


def test_collector_builds_edges():
    col = SIGCollector()
    col.ingest("cell1", [_applied("A"), _applied("B"), _applied("C")])
    col.ingest("cell2", [_applied("A"), _applied("B")])
    edges = col.sutra_edge_stats()["top_edges"]
    weight_of = {(e["source"], e["target"]): e["weight"] for e in edges}
    assert weight_of[("A", "B")] == 2
    assert weight_of[("B", "C")] == 1


def test_transitions_high_confidence():
    col = SIGCollector()
    # A → B occurs 5×, A → C occurs 0×.  P(B|A) = 1.0 → high confidence.
    for _ in range(5):
        col.ingest("c", [_applied("A"), _applied("B")])
    tr = col.sig_transitions()
    hi = tr["high_confidence"]
    assert len(hi) >= 1
    ab = [e for e in hi if e["from"] == "A" and e["to"] == "B"]
    assert ab and ab[0]["probability"] == 1.0


def test_dump_all_writes_nine_files(tmp_path: Path):
    col = SIGCollector()
    col.ingest("c", [_applied("A"), _applied("B")])
    files = col.dump_all(tmp_path)
    expected = {
        "sutra_fire_stats.json",
        "sutra_edge_stats.json",
        "sutra_interaction_graph.json",
        "sig_critical_path.json",
        "sig_transitions.json",
        "sig_linguistic.json",
        "sutra_next_candidates.json",
        "sig_baseline.json",
        "sig_anomalies.json",
    }
    assert expected.issubset(set(files.keys()))
    for name in expected:
        assert (tmp_path / name).exists()


def test_baseline_diff_detects_nothing_on_first_run(tmp_path: Path):
    col = SIGCollector()
    col.ingest("c", [_applied("A"), _applied("B")])
    # First run: no prior baseline → no anomalies regardless of timing.
    col.dump_all(tmp_path)
    import json
    anomalies = json.loads((tmp_path / "sig_anomalies.json").read_text())
    assert anomalies["anomalies"] == []
