"""
4.1.51  क्तादल्पाख्यायाम्  —  VIDHI

Padaccheda: क्तात् अल्प-आख्यायाम्

क्तादल्पाख्यायाम् (4.1.51)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_51_ktAdalpAKy_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_51_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ktAdalpAKyAyAm",
    text_dev              = "क्तादल्पाख्यायाम्",
    padaccheda_dev        = "क्तात् अल्प-आख्यायाम्",
    why_dev               = "(सूत्रम् 4.1.51) क्तादल्पाख्यायाम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
