"""
5.3.99  जीविकाऽर्थे चापण्ये  —  VIDHI

Padaccheda: जीविका-अर्थे च अपण्ये

जीविकाऽर्थे चापण्ये (5.3.99)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_99_jIvikArTe_99"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_99_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jIvikA'rTe cApaRye",
    text_dev              = "जीविकाऽर्थे चापण्ये",
    padaccheda_dev        = "जीविका-अर्थे च अपण्ये",
    why_dev               = "(सूत्रम् 5.3.99) जीविकाऽर्थे चापण्ये।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
