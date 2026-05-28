"""
8.1.51  गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत्  —  VIDHI

Padaccheda: गति-अर्थ-लोटा लृट् न चेत् कारकम् सर्व-अन्यत्

गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत् (8.1.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_51_gatyarTalo_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_51_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gatyarTalowA lfRna cet kArakaM sarvAnyat",
    text_dev              = "गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत्",
    padaccheda_dev        = "गति-अर्थ-लोटा लृट् न चेत् कारकम् सर्व-अन्यत्",
    why_dev               = "(सूत्रम् 8.1.51) गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
