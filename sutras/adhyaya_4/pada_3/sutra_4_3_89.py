"""
4.3.89  सोऽस्य निवासः  —  VIDHI

Padaccheda: सः अस्य निवासः

सोऽस्य निवासः (4.3.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_89_sosya_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_89_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "so'sya nivAsaH",
    text_dev              = "सोऽस्य निवासः",
    padaccheda_dev        = "सः अस्य निवासः",
    why_dev               = "(सूत्रम् 4.3.89) सोऽस्य निवासः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
