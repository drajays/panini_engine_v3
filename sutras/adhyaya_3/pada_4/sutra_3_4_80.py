"""
3.4.80  थासस्से  —  VIDHI

The ātmanepada 2sg tiṅ ādeśa thās (TAs in SLP1) is replaced by se.

  thās → se   (ātmanepada 2sg present, e.g. भूयसे)

Condition: find a tiṅ ādeśa term with upadesha_slp1 == "TAs".
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from phonology.varna import parse_slp1_upadesha_sequence


def _find_thas(state: State):
    for ti, t in enumerate(state.terms):
        if t.kind != "pratyaya":
            continue
        if t.meta.get("3_4_80_done"):
            continue
        if "tin_adesha_3_4_78" not in t.tags:
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "TAs":
            return ti
    return None


def cond(state: State) -> bool:
    return _find_thas(state) is not None


def act(state: State) -> State:
    ti = _find_thas(state)
    if ti is None:
        return state
    t = state.terms[ti]
    t.meta["upadesha_slp1_original"] = t.meta.get("upadesha_slp1_original", "TAs")
    t.varnas = parse_slp1_upadesha_sequence("se")
    t.meta["upadesha_slp1"] = "se"
    t.meta["3_4_80_done"] = True
    state.samjna_registry["3.4.80_thasasse"] = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = False,
    text_slp1             = "TAsasse",
    text_dev              = "थासस्से",
    padaccheda_dev        = "थासः से (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "आत्मनेपद-२मध्यम-एकवचने 'थास्' स्थाने 'से' आदेशः।",
    anuvritti_from        = ('3.4.79',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
