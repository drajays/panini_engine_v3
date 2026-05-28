"""
8.2.92  अग्नीत्प्रेषणे परस्य च  —  VIDHI

Padaccheda: अग्नीत्प्रेषणे परस्य च

अग्नीत्प्रेषणे परस्य च (8.2.92)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_92_agnItpreza_92"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_92_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "agnItprezaRe parasya ca",
    text_dev              = "अग्नीत्प्रेषणे परस्य च",
    padaccheda_dev        = "अग्नीत्प्रेषणे परस्य च",
    why_dev               = "(सूत्रम् 8.2.92) अग्नीत्प्रेषणे परस्य च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
