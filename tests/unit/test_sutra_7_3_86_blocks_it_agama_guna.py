from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology    import mk


def _state_with_anga_and_dit_pratyaya(*, it_agama: bool) -> State:
    # anga: k i t  (upadhā = i; antya = t)
    i_v = mk("i")
    if it_agama:
        i_v.tags.add("it_agama")
    anga = Term(kind="prakriti", varnas=[mk("k"), i_v, mk("t")], tags={"anga"}, meta={})
    pr = Term(kind="pratyaya", varnas=[mk("A")], tags={"pratyaya"}, meta={"dit_pratyaya": True})
    return State(terms=[anga, pr])


def test_7_3_86_applies_normally():
    s = _state_with_anga_and_dit_pratyaya(it_agama=False)
    s = apply_rule("1.1.6", s)   # gate on
    s2 = apply_rule("7.3.86", s)
    assert s2.flat_slp1().startswith("ket"), s2.flat_slp1()


def test_7_3_86_blocked_on_it_agama_by_1_1_6():
    s = _state_with_anga_and_dit_pratyaya(it_agama=True)
    s = apply_rule("1.1.6", s)
    s2 = apply_rule("7.3.86", s)
    assert s2.flat_slp1() == s.flat_slp1()

