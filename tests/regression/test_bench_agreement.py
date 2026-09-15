"""
tests/regression/test_bench_agreement.py
────────────────────────────────────────

CONSTITUTION Art. 19 — we do not grade our own homework.

The committed Vidyut oracle (`bench/oracle/vidyut.csv`, MIT) pins agreement on
417 cells. The number may rise; it may not fall silently. A disagreement is a
work item, never a verdict — but a *new* disagreement must be seen.

Vidyut is not installed for this test: it reads the committed CSV.
"""
from __future__ import annotations

import pytest

from bench.run import ORACLE_PATH, load_oracle, run

# 2026-09-15: 338/417. Raise this as gaps close; never lower it to pass.
AGREEMENT_FLOOR = 0.81


@pytest.fixture(scope="module")
def report():
    return run()


def test_oracle_is_committed():
    assert ORACLE_PATH.exists(), "bench/oracle/vidyut.csv missing"
    assert len(load_oracle()) == 417


def test_every_cell_is_comparable(report):
    """Both engines must answer every cell — an unanswerable cell hides a gap."""
    assert report["we_derived"] == report["cells"]
    assert report["comparable"] == report["cells"]


def test_agreement_does_not_fall(report):
    assert report["agreement"] >= AGREEMENT_FLOOR, (
        f"agreement fell to {report['agreement']:.1%}; "
        f"first disagreements: {[d['key'] for d in report['disagreements'][:5]]}"
    )


def test_subanta_agrees_completely(report):
    """All 192 nominal cells matched on 2026-09-15; that is a floor, not a fluke."""
    nominal = [d for d in report["disagreements"] if d["key"].startswith("subanta")]
    assert nominal == [], nominal[:5]
