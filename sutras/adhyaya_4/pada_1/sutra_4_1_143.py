"""
4.1.143  स्वसुश्छः  —  VIDHI

Padaccheda: स्वसुः छः

स्वसुश्छः (4.1.143)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_143_svasuSCaH_143"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_143_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.143"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.143",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svasuSCaH",
    text_dev              = "स्वसुश्छः",
    padaccheda_dev        = "स्वसुः छः",
    why_dev               = "(सूत्रम् 4.1.143) स्वसुश्छः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
