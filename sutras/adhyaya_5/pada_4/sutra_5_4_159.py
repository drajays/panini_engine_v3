"""
5.4.159  नाडीतन्त्र्योः स्वाङ्गे  —  VIDHI

Padaccheda: नाडी-तन्त्र्योः स्वाङ्गे

नाडीतन्त्र्योः स्वाङ्गे (5.4.159)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_159_nAqItantry_159"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_159_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.159"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.159",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAqItantryoH svANge",
    text_dev              = "नाडीतन्त्र्योः स्वाङ्गे",
    padaccheda_dev        = "नाडी-तन्त्र्योः स्वाङ्गे",
    why_dev               = "(सूत्रम् 5.4.159) नाडीतन्त्र्योः स्वाङ्गे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
