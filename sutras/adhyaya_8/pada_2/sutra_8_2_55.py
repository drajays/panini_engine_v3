"""
8.2.55  अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः  —  VIDHI

Padaccheda: अन्-उपसर्गात् फुल्ल-क्षीब-कृश-उल्लाघाः

अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः (8.2.55)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_55_anupasargA_55"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anupasargAt PullakzIbakfSollAGAH",
    text_dev              = "अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः",
    padaccheda_dev        = "अन्-उपसर्गात् फुल्ल-क्षीब-कृश-उल्लाघाः",
    why_dev               = "(सूत्रम् 8.2.55) अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
