from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.lopa_ghost import LUK_LOPA_GHOST_TAG, term_is_sup_luk_ghost
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology import mk


def test_metadata():
    r = SUTRA_REGISTRY["2.4.71"]
    assert r.sutra_id == "2.4.71"
    assert r.sutra_type is SutraType.VIDHI
    assert "luk" in r.text_slp1.lower()


def test_zero_width_ghost_internal_sup_when_armed():
    t1 = Term(kind="prakriti", varnas=[mk("r")], tags={"prātipadika"}, meta={})
    sup = Term(
        kind="pratyaya",
        varnas=[mk("A"), mk("s")],
        tags={"sup", "pratyaya"},
        meta={"upadesha_slp1": "As"},
    )
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={})
    s0 = State(
        terms=[t1, sup, t2],
        meta={"2_4_71_luk_arm": True, "pratipadika_avayava_ready": True},
    )

    s1 = apply_rule("2.4.71", s0)
    assert len(s1.terms) == 3
    assert s1.meta.get("2_4_71_luk_arm") is False
    assert s1.meta.get("2_4_71_luk") is True
    g = s1.terms[1]
    assert term_is_sup_luk_ghost(g)
    assert LUK_LOPA_GHOST_TAG in g.tags
    assert "sup" in g.tags
    assert g.varnas == []
    assert s1.flat_slp1() == "rp"


def test_skips_when_not_armed():
    t1 = Term(kind="prakriti", varnas=[mk("r")], tags={"prātipadika"}, meta={})
    sup = Term(kind="pratyaya", varnas=[mk("A"), mk("s")], tags={"sup"}, meta={"upadesha_slp1": "As"})
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={})
    s0 = State(terms=[t1, sup, t2], meta={})

    s1 = apply_rule("2.4.71", s0)
    assert len(s1.terms) == 3


def test_skips_when_armed_but_pratipadika_ready_false():
    t1 = Term(kind="prakriti", varnas=[mk("r")], tags={"prātipadika"}, meta={})
    sup = Term(kind="pratyaya", varnas=[mk("A"), mk("s")], tags={"sup"}, meta={"upadesha_slp1": "As"})
    t2 = Term(kind="prakriti", varnas=[mk("p")], tags={"prātipadika"}, meta={})
    s0 = State(terms=[t1, sup, t2], meta={"2_4_71_luk_arm": True})

    s1 = apply_rule("2.4.71", s0)
    assert len(s1.terms) == 3
