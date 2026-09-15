"""
tests/regression/test_certain_prakriyas.py
──────────────────────────────────────────

The forms we are certain of, and the warrant for each certainty.

`python3 -m tools.show_prakriya <case>` prints any of them step by step with
the sūtra that did the work; this test is the same set as a gate, so a change
that breaks one is a failure rather than a surprise on screen.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401

from tools.show_prakriya import CASES, derive, oracle_forms


@pytest.mark.parametrize("case", CASES, ids=lambda c: c.key)
def test_the_certain_form_still_derives(case):
    assert derive(case).flat_dev() == case.expect_dev, case.warrant


@pytest.mark.parametrize("case", CASES, ids=lambda c: c.key)
def test_the_oracle_still_agrees_where_it_has_an_opinion(case):
    """Art. 19: certainty that rests on agreement must keep resting on it."""
    theirs = oracle_forms(case.cell_key)
    if not theirs:
        pytest.skip("no oracle row for this cell")
    assert derive(case).flat_slp1() in theirs


def test_every_case_states_its_warrant():
    for case in CASES:
        assert len(case.warrant) > 20, f"{case.key} has no warrant"
