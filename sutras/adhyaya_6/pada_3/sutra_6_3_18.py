"""
6.3.18  शयवासवासिषु अकालात्  —  VIDHI

Padaccheda: शय-वास-वासिषु अकालात्

शयवासवासिषु अकालात् (6.3.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_18_SayavAsavA_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_18_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SayavAsavAsizu akAlAt",
    text_dev              = "शयवासवासिषु अकालात्",
    padaccheda_dev        = "शय-वास-वासिषु अकालात्",
    why_dev               = "(सूत्रम् 6.3.18) शयवासवासिषु अकालात्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
