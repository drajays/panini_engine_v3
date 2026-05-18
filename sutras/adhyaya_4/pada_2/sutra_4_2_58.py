"""
4.2.58  घञः साऽस्यां क्रियेति ञः  —  VIDHI

Padaccheda: घञः सा अस्याम् क्रिया इति ञः

घञः साऽस्यां क्रियेति ञः (4.2.58)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_58_GaYaH_58"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_58_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "GaYaH sA'syAM kriyeti YaH",
    text_dev              = "घञः साऽस्यां क्रियेति ञः",
    padaccheda_dev        = "घञः सा अस्याम् क्रिया इति ञः",
    why_dev               = "(सूत्रम् 4.2.58) घञः साऽस्यां क्रियेति ञः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
