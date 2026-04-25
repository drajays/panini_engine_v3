from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk


def _state_diksamasa_bahuvrihi(*, has_sarvadi: bool) -> State:
    t = Term(
        kind="prakriti",
        varnas=[mk("d"), mk("a"), mk("k"), mk("z"), mk("i"), mk("R"), mk("a"), mk("p"), mk("U"), mk("r"), mk("v"), mk("A")],
        tags={"anga", "prātipadika", "diksamasa", "bahuvrihi"},
        meta={"upadesha_slp1": "dakziNapUrvA", "contains_sarvadi": has_sarvadi},
    )
    return State(terms=[t])


def test_metadata():
    r = SUTRA_REGISTRY["1.1.28"]
    assert r.sutra_type is SutraType.VIBHASHA
    assert "bahuvrIh" in r.text_slp1 or "bahuvrIh" in r.text_slp1.lower()


def test_declined_choice_does_not_tag():
    s0 = _state_diksamasa_bahuvrihi(has_sarvadi=True)
    s1 = apply_rule("1.1.28", s0, {"vibhasha_choice": False})
    assert "sarvanama" not in s1.terms[0].tags


def test_choice_true_tags_sarvanama():
    s0 = _state_diksamasa_bahuvrihi(has_sarvadi=True)
    s1 = apply_rule("1.1.28", s0, {"vibhasha_choice": True})
    assert "sarvanama" in s1.terms[0].tags


def test_no_sarvadi_member_cond_false():
    s0 = _state_diksamasa_bahuvrihi(has_sarvadi=False)
    s1 = apply_rule("1.1.28", s0, {"vibhasha_choice": True})
    assert "sarvanama" not in s1.terms[0].tags

