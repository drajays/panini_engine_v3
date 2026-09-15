"""
tests/constitutional/test_gaps_are_outputs.py
─────────────────────────────────────────────

Constitution **Article 18** — a gap is an output.

The engine must name what is missing. This test holds the reporter to the
narrow definition that makes the list usable: a rule that is merely *offered*
and would change nothing is not a gap, and the committed worklist must stay
non-empty and typed.
"""
from __future__ import annotations

import json

import pytest

from engine.gaps import Gap, gap_from_exception, rank

WORKLIST = __import__("pathlib").Path(__file__).resolve().parents[2] / "sig" / "gaps.json"


def test_missing_data_is_a_gap_that_names_the_datum():
    gap = gap_from_exception(
        KeyError("dhātu 'SAs' not found in dhātupātha. Use upadeśa SLP1"),
        where="tinanta:SAs:laT:3:1",
    )
    assert gap is not None
    assert gap.kind == "missing_data"
    assert "SAs" in gap.subject
    assert gap.where == "tinanta:SAs:laT:3:1"


def test_an_ordinary_bug_is_not_dressed_up_as_a_gap():
    assert gap_from_exception(ZeroDivisionError("division by zero"), where="x") is None


def test_rank_orders_by_frequency():
    gaps = [
        Gap("unscheduled", "6.4.110", "would write karuvas → kuruvas", "a"),
        Gap("unscheduled", "6.4.110", "would write karuvas → kuruvas", "b"),
        Gap("unscheduled", "7.4.62", "would write gamgama → jamgama", "c"),
    ]
    ordered = rank(gaps)
    assert ordered[0]["subject"] == "6.4.110"
    assert ordered[0]["count"] == 2
    assert ordered[0]["seen_in"] == ["a", "b"]


def test_committed_worklist_is_typed_and_not_empty():
    assert WORKLIST.exists(), "run 'make gaps'"
    data = json.loads(WORKLIST.read_text(encoding="utf-8"))
    assert data["cells"] > 0 and data["worklist"]
    kinds = {item["kind"] for item in data["worklist"]}
    assert kinds <= {"unscheduled", "missing_data", "oracle_disagreement"}
    # The dry-run filter is what keeps this list usable: without it the same
    # grid reports 17,285 "gaps" instead of a few hundred.
    assert data["gaps"] < 1000, "the gap list has become noise again"


@pytest.mark.parametrize("subject", ["6.4.110", "7.4.62"])
def test_the_worklist_names_rules_the_oracle_disagreements_need(subject):
    """कृ needs 6.4.110, गम् liṭ needs 7.4.62 — the two reports corroborate."""
    data = json.loads(WORKLIST.read_text(encoding="utf-8"))
    assert any(item["subject"] == subject for item in data["worklist"])
