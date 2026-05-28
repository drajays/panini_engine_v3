"""
8.2.47  श्योऽस्पर्शे  —  VIDHI

Padaccheda: श्यः अस्पर्शे

श्योऽस्पर्शे (8.2.47)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_47_SyosparSe_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Syo'sparSe",
    text_dev              = "श्योऽस्पर्शे",
    padaccheda_dev        = "श्यः अस्पर्शे",
    why_dev               = "(सूत्रम् 8.2.47) श्योऽस्पर्शे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
