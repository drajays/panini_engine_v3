"""
3.4.117  छन्दस्युभयथा  —  VIDHI

Padaccheda: छन्दसि उभयथा

krt-suffix rule: छन्दस्युभयथा
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_117_CandasyuBa_117"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandasyuBayaTA",
    text_dev              = "छन्दस्युभयथा",
    padaccheda_dev        = "छन्दसि उभयथा",
    why_dev               = "धातोः प्रत्ययः (३.4.117)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
