"""
tests/constitutional/test_vipratisedha_resolver.py
──────────────────────────────────────────────────

Constitution **Article 15** — conflict is declared, never engineered.

The resolver's layers are paribhāṣās, loaded with their text from the
vendored Paribhāṣenduśekhara slice, and every decision names the layer that
decided it and the rules it beat.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401 — fills SUTRA_REGISTRY

from engine import SUTRA_REGISTRY
from engine.paribhasha import layer, layers, not_modelled, paribhasha
from engine.resolver import Decision, record_decision, resolve, resolve_with_reason
from engine.state import State, Term


def test_the_strength_ladder_is_quoted_from_the_shekhara():
    """PŚ 38 — five terms, ascending, and we quote it rather than recall it."""
    text = paribhasha("38")
    assert text == "पूर्वपरनित्यान्तरङ्गापवादानामुत्तरोत्तरं बलीयः"
    assert layer("para").ps_num == "38"


def test_unmodelled_layers_are_declared_not_hidden():
    deferred = {item.key for item in not_modelled()}
    assert deferred == {"nitya", "antaranga"}, (
        "a layer the engine does not weigh must say so (Art. 18)"
    )


def test_every_layer_carries_its_citation():
    for item in layers().values():
        assert item.paribhasha_dev, f"{item.key} has no paribhāṣā text"
        assert "परिभाषेन्दुशेखर" in item.citation()


@pytest.mark.parametrize("apavada,utsarga", [
    ("6.1.88", "6.1.87"),     # वृद्धिरेचि over आद्गुणः
    ("6.1.101", "6.1.77"),    # अकः सवर्णे दीर्घः over इको यणचि
    ("6.1.109", "6.1.78"),    # एङः पदान्तादति over एचोऽयवायावः
])
def test_declared_apavada_wins_and_says_why(apavada, utsarga):
    assert utsarga in SUTRA_REGISTRY[apavada].apavada_of
    decision = resolve_with_reason([utsarga, apavada], State(terms=[]))
    assert decision.winner == apavada
    assert decision.layer == "apavada"
    assert decision.losers == (utsarga,)
    assert "अन्तरङ्गादप्यवादो बलवान्" in decision.reason_dev


def test_para_decides_equals_by_astadhyayi_order():
    decision = resolve_with_reason(["1.1.1", "1.1.2"], State(terms=[]))
    assert decision.winner == "1.1.2"
    assert decision.layer == "para"
    assert decision.losers == ("1.1.1",)


def test_resolve_and_resolve_with_reason_never_disagree():
    for pair in (["6.1.87", "6.1.88"], ["1.1.1", "1.1.2"], ["6.1.77", "6.1.101"]):
        assert resolve(pair, State(terms=[])) == resolve_with_reason(pair, State(terms=[])).winner


def test_a_beaten_rule_is_written_into_the_trace():
    """Art. 15: the loser appears as BLOCKED, naming the rule that beat it."""
    state = State(terms=[Term(kind="pada", varnas=[])])
    record_decision(state, resolve_with_reason(["6.1.87", "6.1.88"], state))
    step = state.trace[0]
    assert step["sutra_id"] == "6.1.87"
    assert step["status"] == "BLOCKED"
    assert "6.1.88 beat 6.1.87" in step["gate_reason"]
    assert "परिभाषेन्दुशेखर" in step["gate_reason"]


def test_sole_candidate_is_not_dressed_up_as_a_conflict():
    decision = resolve_with_reason(["6.1.88"], State(terms=[]))
    assert decision.layer == "sole-candidate" and decision.losers == ()
