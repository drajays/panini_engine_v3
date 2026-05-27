"""
2.4.81  आमः  —  VIDHI (narrow: *liṭ* *luk* after *ām*)

Teaching **P014**: after **ām** is placed before *liṭ*, the *liṭ* *pratyaya*
undergoes *luk* (disappears).  The **īkṣ** + **ām** pieces are then fused into
one **prātipadika** *Term* (**``IkzAm``**) for the periphrastic spine.

Engine:
  • ``state.meta['2_4_81_lit_luk_arm']``
  • expects ``… + Ikz + Am + liT``
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State, Term


def _site(state: State) -> bool:
    if not state.meta.get("2_4_81_lit_luk_arm"):
        return False
    if len(state.terms) < 3:
        return False
    a, b, c = state.terms[-3], state.terms[-2], state.terms[-1]
    if "dhatu" not in a.tags:
        return False
    if (a.meta.get("upadesha_slp1") or "").strip() != "Ikz":
        return False
    if (b.meta.get("upadesha_slp1") or "").strip() != "Am":
        return False
    if (c.meta.get("upadesha_slp1") or "").strip() != "liT":
        return False
    return True


def cond(state: State) -> bool:
    return _site(state)


def act(state: State) -> State:
    if not _site(state):
        return state
    ikz, am = state.terms[-3], state.terms[-2]
    del state.terms[-3:]
    merged = Term(
        kind="prakriti",
        varnas=list(ikz.varnas) + list(am.varnas),
        tags={"anga", "prātipadika"},
        meta={},
    )
    state.terms.append(merged)
    state.meta.pop("2_4_81_lit_luk_arm", None)
    return state


SUTRA = SutraRecord(
    sutra_id="2.4.81",
    sutra_type=SutraType.VIDHI,
    text_slp1="AmaH",
    text_dev="आमः",
    padaccheda_dev="आमः",
    why_dev="आम्-परे लिट्-लुक्; ईक्ष्+आम् → ईक्षाम् (प्रातिपदिकम्) — P014।",
    anuvritti_from=("2.4.1",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
