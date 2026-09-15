"""
tests/regression/test_autonomy_baseline.py
──────────────────────────────────────────

Phase C's yardstick: how far the engine derives with **no recipe** — the
scheduler proposing, the resolver choosing, `apply_rule` applying.

Today the answer is *nowhere*, for one measured reason, and this test pins
both the number and the reason so that progress is visible and regress is
loud.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401

from tools.autonomy_report import effective_candidates, run_autonomously, start_state
from tools.show_prakriya import CASES, derive

SUBANTA_CASES = [c for c in CASES if c.kind == "subanta"]


@pytest.fixture(scope="module")
def ramah_start():
    return start_state(next(c for c in SUBANTA_CASES if c.key == "ramah"))


def test_the_loop_is_offered_candidates_but_none_of_them_advance(ramah_start):
    """126 offered, 0 effective — the pool is full of rules that do nothing here."""
    from engine.scheduler import enumerate_candidates

    offered = enumerate_candidates(ramah_start)
    assert offered, "the scheduler offers nothing at all — a different bug"
    assert effective_candidates(offered, ramah_start) == [], (
        "a candidate now advances रामसुँ — the phase model may have been fixed; "
        "update this test and the C1 row in ROADMAP.md"
    )


def test_the_form_it_is_stuck_on_is_stem_plus_raw_upadesha(ramah_start):
    """रामसुँ: the next rule needed is it-saṃjñā (1.3.2 · 1.3.9), which the
    forward-only phase chain has already closed the door on."""
    assert ramah_start.flat_slp1() == "rAmasu"


@pytest.mark.parametrize("case", SUBANTA_CASES, ids=lambda c: c.key)
def test_every_certain_subanta_halts_at_the_same_wall(case):
    expected = derive(case).flat_slp1()
    run = run_autonomously(start_state(case), expected, case.key, budget=8)
    assert run.outcome in {"halted", "reached"}, run.outcome
    if run.outcome == "reached":
        pytest.fail(f"{case.key} now derives autonomously — raise the baseline")


def test_a_vacuous_candidate_is_not_a_candidate(ramah_start):
    """The filter that turns divergence into an honest halt."""
    from engine.scheduler import enumerate_candidates

    offered = enumerate_candidates(ramah_start)
    assert len(effective_candidates(offered, ramah_start)) < len(offered)
