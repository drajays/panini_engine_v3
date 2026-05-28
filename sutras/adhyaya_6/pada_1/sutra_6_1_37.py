"""
6.1.37  न सम्प्रसारणे सम्प्रसारणम्  —  VIDHI

Padaccheda: न सम्प्रसारणे सम्प्रसारणम्

न सम्प्रसारणे सम्प्रसारणम् (6.1.37)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_37_na_37"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_37_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na samprasAraRe samprasAraRam",
    text_dev              = "न सम्प्रसारणे सम्प्रसारणम्",
    padaccheda_dev        = "न सम्प्रसारणे सम्प्रसारणम्",
    why_dev               = "(सूत्रम् 6.1.37) न सम्प्रसारणे सम्प्रसारणम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
