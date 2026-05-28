"""
8.4.48  नादिन्याक्रोशे पुत्रस्य  —  VIDHI

Padaccheda: न ०/० आदिनी ७/१ आक्रोशे ७/१ पुत्रस्य ६/१

नादिन्याक्रोशे पुत्रस्य (8.4.48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_48_nAdinyAkro_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_48_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAdinyAkroSe putrasya",
    text_dev              = "नादिन्याक्रोशे पुत्रस्य",
    padaccheda_dev        = "न ०/० आदिनी ७/१ आक्रोशे ७/१ पुत्रस्य ६/१",
    why_dev               = "(सूत्रम् 8.4.48) नादिन्याक्रोशे पुत्रस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
