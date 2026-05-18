"""
5.2.124  वाचो ग्मिनिः  —  VIDHI

Padaccheda: वाचः ग्मिनिः

वाचो ग्मिनिः (5.2.124)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_124_vAco_124"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_124_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAco gminiH",
    text_dev              = "वाचो ग्मिनिः",
    padaccheda_dev        = "वाचः ग्मिनिः",
    why_dev               = "(सूत्रम् 5.2.124) वाचो ग्मिनिः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
