"""
7.3.46  उदीचामातः स्थाने यकपूर्वायाः  —  VIDHI

Padaccheda: उदीचाम् आतः स्थाने य-क-पूर्वायाः

उदीचामातः स्थाने यकपूर्वायाः (7.3.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_46_udIcAmAtaH_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.46", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_3_46_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udIcAmAtaH sTAne yakapUrvAyAH",
    text_dev              = "उदीचामातः स्थाने यकपूर्वायाः",
    padaccheda_dev        = "उदीचाम् आतः स्थाने य-क-पूर्वायाः",
    why_dev               = "(सूत्रम् 7.3.46) उदीचामातः स्थाने यकपूर्वायाः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
