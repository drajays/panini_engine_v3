"""
4.2.67  तदस्मिन्नस्तीति देशे तन्नाम्नि  —  VIDHI

Padaccheda: तत् अस्मिन् अस्ति (क्रियापदम्) इति देशे तन्नाम्नि

तदस्मिन्नस्तीति देशे तन्नाम्नि (4.2.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_67_tadasminna_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.67", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasminnastIti deSe tannAmni",
    text_dev              = "तदस्मिन्नस्तीति देशे तन्नाम्नि",
    padaccheda_dev        = "तत् अस्मिन् अस्ति (क्रियापदम्) इति देशे तन्नाम्नि",
    why_dev               = "(सूत्रम् 4.2.67) तदस्मिन्नस्तीति देशे तन्नाम्नि।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
