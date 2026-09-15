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

# Floors describe the *committed* tree, since that is what a clean checkout
# runs: 306/390 = 78.5 % on 2026-09-15. The working tree is ahead of this
# (417/417 comparable, 81.1 %) because a large arm-removal change is still
# uncommitted. Raise both as work lands; never lower either to pass.
AGREEMENT_FLOOR = 0.78
COMPARABLE_FLOOR = 390


@pytest.fixture(scope="module")
def report():
    return run()


def test_oracle_is_committed():
    assert ORACLE_PATH.exists(), "bench/oracle/vidyut.csv missing"
    assert len(load_oracle()) == 417


def test_every_cell_stays_comparable(report):
    """A cell we can no longer derive hides a gap — the count may only rise.

    The target is all 417; the committed tree reaches 390 and the working tree
    already reaches 417.
    """
    assert report["we_derived"] >= COMPARABLE_FLOOR
    assert report["comparable"] >= COMPARABLE_FLOOR


def test_agreement_does_not_fall(report):
    assert report["agreement"] >= AGREEMENT_FLOOR, (
        f"agreement fell to {report['agreement']:.1%}; "
        f"first disagreements: {[d['key'] for d in report['disagreements'][:5]]}"
    )


def test_subanta_agrees_completely(report):
    """All 192 nominal cells matched on 2026-09-15; that is a floor, not a fluke."""
    nominal = [d for d in report["disagreements"] if d["key"].startswith("subanta")]
    assert nominal == [], nominal[:5]
