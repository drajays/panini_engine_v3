"""
tests/constitutional/test_vipratisedha_resolver.py
──────────────────────────────────────────────────

Constitution **Article 21** — Ladder 1 (vipratipatti).
Constitution **Article 22** — granthas: only the Paribhāṣenduśekhara decides
at runtime; Laghuśabdenduśekhara is quoted, not executed.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401 — fills SUTRA_REGISTRY

from engine import SUTRA_REGISTRY
from engine.paribhasha import (
    all_paribhashas,
    grantha_catalog,
    laghu_excerpt,
    layer,
    layers,
    not_modelled,
    paribhasha,
    runtime_granthas,
)
from engine.resolver import (
    DECISION_LAYERS,
    Decision,
    record_decision,
    resolve,
    resolve_with_reason,
)
from engine.state import State, Term
from engine.sutra_type import SutraType


def test_the_strength_ladder_is_quoted_from_the_shekhara():
    """PŚ 38 — five terms, ascending, and we quote it rather than recall it."""
    text = paribhasha("38")
    assert text == "पूर्वपरनित्यान्तरङ्गापवादानामुत्तरोत्तरं बलीयः"
    assert layer("para").ps_num == "38"


def test_full_shekhara_patha_is_loaded_from_ashtadhyayi_data():
    """Art. 21: the runtime book is the 133-paribhāṣā pāṭha, not a hand slice."""
    patha = all_paribhashas()
    assert len(patha) == 133
    assert patha["50"] == "असिद्धं बहिरङ्गमन्तरङ्गे"
    assert patha["57"] == "अन्तरङ्गादप्यवादो बलवान्"
    assert layer("antaranga").ps_num == "50"
    assert "असिद्धं बहिरङ्गमन्तरङ्गे" in layer("antaranga").citation()


def test_source_databases_are_named():
    cat = grantha_catalog()
    urls = {d["url"] for d in cat["databases"]}
    assert "https://github.com/ashtadhyayi-com/data" in urls
    assert any("rkmvu.ac.in" in u and "Grammar" in u for u in urls)
    ash = next(d for d in cat["databases"] if d["id"] == "ashtadhyayi-com-data")
    assert ash["paths"]["paribhashendushekhar"] == "paribhashendushekhar/data.txt"
    rkm = next(d for d in cat["databases"] if d["id"] == "rkmvu-grammar-site")
    assert rkm["runtime"] is False
    assert runtime_granthas() == ["paribhashendushekhar"]
    cat = grantha_catalog()
    for g in cat["arthika_granthas"] + cat["sk_tika_granthas"]:
        assert g["runtime"] is False
    # LŚ is quoted for 1.1.44 (vikalpa), never executed as a winner
    excerpt = laghu_excerpt("1.1.44")
    assert "न वेति विभाषा" in excerpt
    assert layer("vikalpa").sutra_id == "1.1.44"


def test_unmodelled_layers_are_declared_not_hidden():
    deferred = {item.key for item in not_modelled()}
    assert deferred == {"nitya", "antaranga"}, (
        "a layer the engine does not weigh must say so (Art. 18)"
    )


def test_every_layer_carries_its_citation():
    for item in layers().values():
        cite = item.citation()
        assert item.paribhasha_dev or item.note, f"{item.key} has no text"
        assert (
            "परिभाषेन्दुशेखर" in cite
            or "अष्टाध्यायी" in cite
            or "Art. 21" in cite
        ), f"{item.key}: {cite}"


def test_decision_layer_is_never_an_unnamed_heuristic():
    """Art. 21: no Decision.layer string outside the śāstra / amendment set."""
    assert "soi" not in DECISION_LAYERS
    decision = resolve_with_reason(["1.1.1", "1.1.2"], State(terms=[]))
    assert decision.layer in DECISION_LAYERS
    assert decision.layer == "para"


def test_soi_cannot_beat_para():
    """A higher specificity score on an earlier sūtra must not win (Art. 21)."""
    decision = resolve_with_reason(
        ["1.1.1", "1.1.2"],
        State(terms=[]),
        specificity={"1.1.1": lambda st: 99, "1.1.2": lambda st: 0},
    )
    assert decision.winner == "1.1.2"
    assert decision.layer == "para"
    assert decision.soi_proposal == "1.1.1"
    state = State(terms=[Term(kind="pada", varnas=[])])
    record_decision(state, decision)
    kinds = {g["kind"] for g in state.meta["art18_gaps"]}
    assert "undeclared_apavada_candidate" in kinds
    assert "unmodelled_layer" in kinds


@pytest.mark.parametrize("apavada,utsarga", [
    ("6.1.88", "6.1.87"),     # वृद्धिरेचि over आद्गुणः
    ("6.1.101", "6.1.77"),    # अकः सवर्णे दीर्घः over इको यणचि
    ("6.1.109", "6.1.78"),    # एङः पदान्तादति over एचोऽयवायावः
    ("3.1.77", "3.1.68"),     # तुदादि शः over कर्तरि शप् (declared, was SOI)
])
def test_declared_apavada_wins_and_says_why(apavada, utsarga):
    assert utsarga in SUTRA_REGISTRY[apavada].apavada_of
    decision = resolve_with_reason([utsarga, apavada], State(terms=[]))
    assert decision.winner == apavada
    assert decision.layer == "apavada"
    assert decision.losers == (utsarga,)
    assert "अन्तरङ्गादप्यवादो बलवान्" in decision.reason_dev


def test_gana_vikarana_apavadas_are_declared():
    for sid in ("3.1.69", "3.1.73", "3.1.77", "3.1.78", "3.1.79", "3.1.81"):
        assert "3.1.68" in SUTRA_REGISTRY[sid].apavada_of, sid


def test_para_decides_equals_by_astadhyayi_order():
    decision = resolve_with_reason(["1.1.1", "1.1.2"], State(terms=[]))
    assert decision.winner == "1.1.2"
    assert decision.layer == "para"
    assert decision.losers == ("1.1.1",)
    assert "nitya" in decision.skipped_unmodelled
    assert "antaranga" in decision.skipped_unmodelled


def test_vibhasha_tie_is_forked_not_picked_by_para():
    """A live विभाषा among candidates is a stop condition (Art. 21)."""
    vibh = [
        sid for sid, rec in SUTRA_REGISTRY.items()
        if rec.sutra_type is SutraType.VIBHASHA
    ]
    assert vibh, "need at least one registered VIBHASHA"
    vibh_id = sorted(vibh, key=lambda s: tuple(int(p) for p in s.split(".")))[0]
    decision = resolve_with_reason(["1.1.1", vibh_id], State(terms=[]))
    assert decision.layer == "vikalpa"
    assert decision.winner == vibh_id
    assert decision.losers == ()  # the other branch stays live


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
