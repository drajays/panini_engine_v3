"""
8.4.62  झयो होऽन्यतरस्याम्  —  VIDHI

Padaccheda: झयः । होः । अन्यतरस्याम्

झयो होऽन्यतरस्याम् (8.4.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_62_Jayo_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_62_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Jayo ho'nyatarasyAm",
    text_dev              = "झयो होऽन्यतरस्याम्",
    padaccheda_dev        = "झयः । होः । अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.4.62) झयो होऽन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
