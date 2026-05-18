"""
5.3.61  ज्य च  —  VIDHI

Padaccheda: ज्य (लुप्तप्रथमान्तनिर्देशः) च

ज्य च (5.3.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_61_jya_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jya ca",
    text_dev              = "ज्य च",
    padaccheda_dev        = "ज्य (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 5.3.61) ज्य च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
