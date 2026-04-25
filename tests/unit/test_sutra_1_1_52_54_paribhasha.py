"""1.1.52/1.1.54 paribhāṣā gates — presence + idempotence."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def test_metadata():
    r52 = SUTRA_REGISTRY["1.1.52"]
    r54 = SUTRA_REGISTRY["1.1.54"]
    assert r52.sutra_type is SutraType.PARIBHASHA
    assert r54.sutra_type is SutraType.PARIBHASHA


def test_paribhasha_gates_set_once():
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("SAlA"),
        tags={"anga"},
        meta={"upadesha_slp1": "SAlA"},
    )
    s0 = State(terms=[t])
    s1 = apply_rule("1.1.52", s0)
    s2 = apply_rule("1.1.54", s1)
    assert "1.1.52_alo_antyasya" in s2.paribhasha_gates
    assert "1.1.54_adesh_parasya" in s2.paribhasha_gates
    # idempotence
    s3 = apply_rule("1.1.52", s2)
    s4 = apply_rule("1.1.54", s3)
    assert s4.paribhasha_gates == s2.paribhasha_gates

