"""
8.3.50  कःकरत्करतिकृधिकृतेष्वनदितेः  —  VIDHI

Padaccheda: कः-करत्-करति-कृधि-कृतेषु अनदितेः

कःकरत्करतिकृधिकृतेष्वनदितेः (8.3.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_50_kaHkaratka_50"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_50_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaHkaratkaratikfDikftezvanaditeH",
    text_dev              = "कःकरत्करतिकृधिकृतेष्वनदितेः",
    padaccheda_dev        = "कः-करत्-करति-कृधि-कृतेषु अनदितेः",
    why_dev               = "(सूत्रम् 8.3.50) कःकरत्करतिकृधिकृतेष्वनदितेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
