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
    return ijadi_gurumat_anrcchah("".join(v.slp1 for v in prev.varnas))


_IC = set("iIuUfFxXeEoO")          # ic: every vowel but a/ā
_DIRGHA_ETC = set("AIUFXeEoO")     # guru by itself (1.4.12 दीर्घं च)
_AC = set("aAiIuUfFxXeEoO")


def ijadi_gurumat_anrcchah(flat: str) -> bool:
    """इजादेः गुरुमतः अनृच्छः — ic-initial, has a guru vowel (long, or short before
    a saṃyoga: 1.4.11/12), and not ऋच्छ्. एध्, ईक्ष्, ऊह् → yes; इष्, उष्, ऋच्छ् → no."""
    if not flat or flat[0] not in _IC or flat == "fcC":
        return False
    for i, c in enumerate(flat):
        if c in _DIRGHA_ETC:
            return True
        if c in _AC and len(flat) - i - 1 >= 2 and not (set(flat[i + 1:i + 3]) & _AC):
            return True
    return False


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
    return state


SUTRA = SutraRecord(
    sutra_id="3.1.36",
    sutra_type=SutraType.VIDHI,
    text_slp1='ijAdeSca gurumatonfcCaH',
    text_dev='इजादेश्च गुरुमतोऽनृच्छः',
    padaccheda_dev="इजादेः / च / गुरुमतः / अनृच्छः",
    why_dev="इजादि-गुरुमत्-धातोः (ईक्ष्) लिट्-पूर्वम् आम्-आगमः — P014।",
    anuvritti_from=("3.1.35",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
