"""
5.1.73  संशयमापन्नः  —  VIDHI

Padaccheda: संशयम् आपन्नः

संशयमापन्नः (5.1.73)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_73_saMSayamAp_73"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_73_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMSayamApannaH",
    text_dev              = "संशयमापन्नः",
    padaccheda_dev        = "संशयम् आपन्नः",
    why_dev               = "(सूत्रम् 5.1.73) संशयमापन्नः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
