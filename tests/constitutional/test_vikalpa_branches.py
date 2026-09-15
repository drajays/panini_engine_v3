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


def _katara_state():
    """कतर + कतम + जस्, the tape 1.1.32 विभाषा जसि asks its question about."""
    from pipelines.katarakatamA_vibhASa_jasi import (
        _mk_member, _mk_sup, _structural_merge_dvandva,
    )
    from engine import apply_rule

    state = _structural_merge_dvandva(_mk_member("katara"), _mk_member("katama"))
    state.terms.append(_mk_sup("jas"))
    state = apply_rule("6.4.1", state)
    return apply_rule("1.1.31", state)


def test_the_dispatcher_takes_either_reading_on_request():
    """No pipeline is asked to cooperate: the policy is read by the dispatcher.

    1.1.32 विभाषा जसि either restores sarvanāma-hood for the dvandva or does
    not, and the engine must be able to walk both without the calling code
    being written to offer the choice.
    """
    from engine import apply_rule
    from sutras.adhyaya_1.pada_1.sutra_1_1_32 import SUTRA  # noqa: F401

    taken = apply_rule("1.1.32", _katara_state())
    with choose({"1.1.32": False}):
        declined = apply_rule("1.1.32", _katara_state())

    def status(state):
        return [s["status"] for s in state.trace if s["sutra_id"] == "1.1.32"][-1]

    assert status(taken) == "APPLIED"
    assert status(declined) != "APPLIED", (
        "the policy did not reach the dispatcher — both readings came out the same"
    )


def test_a_declined_option_is_recorded_as_a_fork_not_forgotten():
    from engine import apply_rule

    with choose({"1.1.32": False}):
        state = apply_rule("1.1.32", _katara_state())
    assert any(
        (fork.get("sutra_id") if isinstance(fork, dict) else None) == "1.1.32"
        for fork in state.vibhasha_forks
    ), state.vibhasha_forks


@pytest.mark.skipif(
    not optional_rules_reached(_lyap()),
    reason="this pipeline does not reach 6.4.38 in this tree",
)
def test_both_readings_of_va_lyapi_are_returned():
    """6.4.38 वा ल्यपि — the same pipeline, unmodified, yields both."""
    branches = explore(_lyap)
    surfaces = {b.surface_slp1 for b in branches}
    assert surfaces == {"Agaty", "Agay"}, surfaces
    for branch in branches:
        assert branch.choices and branch.choices[0][0] == "6.4.38"


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
    from engine import apply_rule

    state = apply_rule("1.1.32", _katara_state())
    assert optional_rules_reached(state) == ["1.1.32"]


def test_a_derivation_with_no_optional_rule_has_exactly_one_branch():
    from pipelines.subanta import derive

    branches = explore(lambda: derive("rAma", 1, 1))
    assert len(branches) == 1 and branches[0].choices == ()


def test_the_branch_count_is_bounded():
    """2**20 silently explored paths would not be auditable."""
    assert MAX_OPTIONAL_RULES <= 6
