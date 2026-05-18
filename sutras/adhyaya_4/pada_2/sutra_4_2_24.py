"""
4.2.24  साऽस्य देवता  —  VIDHI

Padaccheda: सा अस्य देवता

साऽस्य देवता (4.2.24)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_24_sAsya_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_24_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sA'sya devatA",
    text_dev              = "साऽस्य देवता",
    padaccheda_dev        = "सा अस्य देवता",
    why_dev               = "(सूत्रम् 4.2.24) साऽस्य देवता।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
