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

SUBANTA_CASES = [c for c in CASES if c.kind in ("subanta", "tinanta")]  # name kept; both kinds


@pytest.fixture(scope="module")
def ramah_start():
    return start_state(next(c for c in SUBANTA_CASES if c.key == "ramah"))


def test_most_of_what_the_scheduler_offers_would_change_nothing(ramah_start):
    """The pool is dominated by rules whose act is a no-op here.

    The exact counts differ between trees — the committed engine offers ~945
    candidates on this state and a scheduler-discipline change in flight cuts
    that to ~126 — so the assertion is the shape, not the number.
    """
    from engine.scheduler import enumerate_candidates

    offered = enumerate_candidates(ramah_start)
    assert offered, "the scheduler offers nothing at all — a different bug"
    usable = effective_candidates(offered, ramah_start)
    assert len(usable) < len(offered) / 2, (
        f"{len(usable)} of {len(offered)} candidates would advance the tape"
    )


def test_the_loop_starts_from_stem_plus_raw_upadesha(ramah_start):
    """रामसुँ — the next rule needed is it-saṃjñā (1.3.2 · 1.3.9), which the
    forward-only phase chain has already closed the door on."""
    assert ramah_start.flat_slp1() == "rAmasu~"


@pytest.mark.parametrize("case", SUBANTA_CASES, ids=lambda c: c.key)
def test_every_certain_subanta_derives_autonomously(case):
    """Gate C, subanta half: scheduler → resolver → apply_rule, no recipe.

    Raised 0/11 → 11/11 on 2026-10-03 (C2: tape-fingerprint vacuity filter, Adhyāya 1
    eligible in every phase, pada-merge at the Tripāḍī boundary, pratiṣedha before
    contention, 'upadeśa' and 'asiddha' resolver layers, 8.4.46/47 typed vibhāṣā,
    adhikāra scope from the records, real 7.1.18)."""
    expected = derive(case).flat_slp1()
    run = run_autonomously(start_state(case), expected, case.key, budget=80)
    assert run.outcome == "reached", f"{case.key}: {run.surface} ≠ {expected} ({run.outcome})"


def test_a_vacuous_candidate_is_not_a_candidate(ramah_start):
    """The filter that turns divergence into an honest halt."""
    from engine.scheduler import enumerate_candidates

    offered = enumerate_candidates(ramah_start)
    assert len(effective_candidates(offered, ramah_start)) < len(offered)
