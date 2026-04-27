"""
6.1.4  पूर्वोऽभ्यासः  —  PARIBHASHA (narrow gate)

Glass-box: marks that the first member in a reduplication frame is the abhyāsa.
Pipelines may arm reduplication and then use this gate for later abhyāsa rules.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "6.1.4_purvo_abhyasa"


def cond(state: State) -> bool:
    return GATE_KEY not in state.paribhasha_gates and len(state.terms) >= 2


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "6.1.4",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "pUrvo abhyAsaH",
    text_dev       = "पूर्वोऽभ्यासः",
    padaccheda_dev = "पूर्वः / अभ्यासः",
    why_dev        = "द्वित्व-प्रसङ्गे पूर्वभागः अभ्यास-संज्ञकः (ग्लास-बॉक्स् gate)।",
    anuvritti_from = (),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

