from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def test_metadata_type():
    r = SUTRA_REGISTRY["1.1.6"]
    assert r.sutra_type is SutraType.PARIBHASHA
    assert "dIdhI" in r.text_slp1 or "vevI" in r.text_slp1


def test_sets_gate_once():
    s0 = State(terms=[Term(kind="prakriti", varnas=[mk("a")], tags=set(), meta={})])
    s1 = apply_rule("1.1.6", s0)
    assert s1.paribhasha_gates.get("id_agama_guna_nishedha") is True
    s2 = apply_rule("1.1.6", s1)
    assert s2.paribhasha_gates.get("id_agama_guna_nishedha") is True

