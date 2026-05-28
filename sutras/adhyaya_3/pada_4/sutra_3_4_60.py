"""
3.4.60  तिर्यच्यपवर्गे  —  VIDHI

Padaccheda: तिर्यचि अपवर्गे

krt-suffix rule: तिर्यच्यपवर्गे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_60_tiryacyapa_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tiryacyapavarge",
    text_dev              = "तिर्यच्यपवर्गे",
    padaccheda_dev        = "तिर्यचि अपवर्गे",
    why_dev               = "धातोः प्रत्ययः (३.4.60)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
