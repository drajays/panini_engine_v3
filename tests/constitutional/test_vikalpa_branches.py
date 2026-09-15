"""
tests/constitutional/test_vikalpa_branches.py
─────────────────────────────────────────────

विभाषा — every branch is an output (ROADMAP B5).

A वा rule is one rule with two legitimate readings. A derivation that shows
only one has hidden half the grammar, and for a learner the two readings *are*
the lesson.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401

from engine.vikalpa import (
    MAX_OPTIONAL_RULES, Branch, choose, explore, optional_rules_reached, policy_choice,
)


def _lyap():
    from pipelines.agaty_gam_lyap_acah_lesson import derive_agaty_gam_lyap_acah_lesson

    return derive_agaty_gam_lyap_acah_lesson()


def test_both_readings_of_va_lyapi_are_returned():
    """6.4.38 वा ल्यपि — the same pipeline, unmodified, yields both."""
    branches = explore(_lyap)
    surfaces = {b.surface_slp1 for b in branches}
    assert surfaces == {"Agaty", "Agay"}, surfaces
    for branch in branches:
        assert branch.choices and branch.choices[0][0] == "6.4.38"
        assert "6.4.38" in branch.describe()


def test_the_pipeline_itself_was_not_asked_to_cooperate():
    """The policy is consulted by the dispatcher, so no pipeline needs editing."""
    import inspect

    from pipelines import agaty_gam_lyap_acah_lesson as module

    source = inspect.getsource(module)
    assert "vibhasha_choice" not in source


def test_a_recipe_step_still_wins_over_the_policy():
    """Precedence: recipe step, then exploration policy, then the sūtra default."""
    from pipelines.katarakatamA_vibhASa_jasi import derive_katarakatame

    with choose({"1.1.32": False}):
        state = derive_katarakatame(vibhasha_choice=True)
    assert state.flat_slp1() == "katarakatame", "the recipe's explicit choice must hold"


def test_choose_restores_the_previous_policy():
    assert policy_choice("6.4.38", True) is True
    with choose({"6.4.38": False}):
        assert policy_choice("6.4.38", True) is False
    assert policy_choice("6.4.38", True) is True


def test_optional_rules_are_read_off_the_trace():
    assert optional_rules_reached(_lyap()) == ["6.4.38"]


def test_a_derivation_with_no_optional_rule_has_exactly_one_branch():
    from pipelines.subanta import derive

    branches = explore(lambda: derive("rAma", 1, 1))
    assert len(branches) == 1 and branches[0].choices == ()


def test_the_branch_count_is_bounded():
    """2**20 silently explored paths would not be auditable."""
    assert MAX_OPTIONAL_RULES <= 6
