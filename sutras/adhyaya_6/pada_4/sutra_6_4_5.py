"""
6.4.5  छन्दस्युभयथा  —  VIDHI

Padaccheda: छन्दसि उभयथा

छन्दस्युभयथा (6.4.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_5_CandasyuBa_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.5", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandasyuBayaTA",
    text_dev              = "छन्दस्युभयथा",
    padaccheda_dev        = "छन्दसि उभयथा",
    why_dev               = "(सूत्रम् 6.4.5) छन्दस्युभयथा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
