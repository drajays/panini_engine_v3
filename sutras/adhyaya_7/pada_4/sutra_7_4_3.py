"""
7.4.3  भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम्  —  VIDHI

Padaccheda: भ्राज-भास-भाष-दीप-जीव-मील-पीडाम् अन्यतरस्याम्

भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम् (7.4.3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_3_BrAjaBAsaB_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.3", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BrAjaBAsaBAzadIpajIvamIlapIqAmanyatarasyAm",
    text_dev              = "भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम्",
    padaccheda_dev        = "भ्राज-भास-भाष-दीप-जीव-मील-पीडाम् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 7.4.3) भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
