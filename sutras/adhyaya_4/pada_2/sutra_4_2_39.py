"""
4.2.39  गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद्वुञ्  —  VIDHI

Padaccheda: गोत्र-उक्ष-उष्ट्र-उरभ्र-राज-राजन्य-राजपुत्र-वत्स-मनुष्य-अजात् वुञ्

गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद्वुञ् (4.2.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_39_gotrokzozw_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.39", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gotrokzozwroraBrarAjarAjanyarAjaputravatsamanuzyAjAdvuY",
    text_dev              = "गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद्वुञ्",
    padaccheda_dev        = "गोत्र-उक्ष-उष्ट्र-उरभ्र-राज-राजन्य-राजपुत्र-वत्स-मनुष्य-अजात् वुञ्",
    why_dev               = "(सूत्रम् 4.2.39) गोत्रोक्षोष्ट्रोरभ्रराजराजन्यराजपुत्रवत्समनुष्याजाद्वुञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
