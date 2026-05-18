"""
8.1.48  किम्वृत्तं च चिदुत्तरम्  —  VIDHI

Padaccheda: किम्-वृत्तम् च चित्-उत्तरम्

किम्वृत्तं च चिदुत्तरम् (8.1.48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_48_kimvfttaM_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_48_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kimvfttaM ca ciduttaram",
    text_dev              = "किम्वृत्तं च चिदुत्तरम्",
    padaccheda_dev        = "किम्-वृत्तम् च चित्-उत्तरम्",
    why_dev               = "(सूत्रम् 8.1.48) किम्वृत्तं च चिदुत्तरम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
