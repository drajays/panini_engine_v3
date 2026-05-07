"""
3.1.36  इजादेश्च गुरुमतोऽनृच्छः  —  VIDHI (narrow: *ām* before *liṭ*)

Teaching **corrected_prakriyas_v2** **P014** (*īkṣāñcakre*): for an *ijādi*
*gurumad* dhātu (here **``Ikz``**) before *liṭ*, insert the **ām** affix before
the *liṭ* placeholder.

Engine:
  • ``state.meta['corrected_v2_P014_3_1_36_am_arm']``
  • tape ends ``… + dhātu(Ikz) + liT``
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

_LAKARA_LIT = frozenset({"liT"})


def _lit_index(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up in _LAKARA_LIT:
            return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get("corrected_v2_P014_3_1_36_am_arm"):
        return False
    if not state.meta.get("lakara_liT"):
        return False
    li = _lit_index(state)
    if li is None or li < 1:
        return False
    if li >= 2 and (state.terms[li - 1].meta.get("upadesha_slp1") or "").strip() == "Am":
        return False
    prev = state.terms[li - 1]
    if "dhatu" not in prev.tags:
        return False
    if (prev.meta.get("upadesha_slp1") or "").strip() != "Ikz":
        return False
    flat = "".join(v.slp1 for v in prev.varnas)
    if flat != "Ikz":
        return False
    return True


def act(state: State) -> State:
    if not cond(state):
        return state
    li = _lit_index(state)
    assert li is not None
    am = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Am")),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "Am"},
    )
    state.terms.insert(li, am)
    state.meta.pop("corrected_v2_P014_3_1_36_am_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.36",
    sutra_type=SutraType.VIDHI,
    text_slp1="ijAdeS ca gurumato'nfcCaH",
    text_dev="इजादेश्च गुरुमतोऽनृच्छः",
    padaccheda_dev="इजादेः / च / गुरुमतः / अनृच्छः",
    why_dev="इजादि-गुरुमत्-धातोः (ईक्ष्) लिट्-पूर्वम् आम्-आगमः — P014।",
    anuvritti_from=("3.1.35",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
