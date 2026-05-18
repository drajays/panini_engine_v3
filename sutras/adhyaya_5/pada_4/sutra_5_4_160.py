"""
5.4.160  निष्प्रवाणिश्च  —  VIDHI

Padaccheda: निष्प्रवाणिः च

निष्प्रवाणिश्च (5.4.160)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_160_nizpravARi_160"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_160_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.160"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.160",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizpravARiSca",
    text_dev              = "निष्प्रवाणिश्च",
    padaccheda_dev        = "निष्प्रवाणिः च",
    why_dev               = "(सूत्रम् 5.4.160) निष्प्रवाणिश्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
