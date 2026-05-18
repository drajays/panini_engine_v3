"""
6.4.53  जनिता मन्त्रे  —  VIDHI

Padaccheda: जनिता मन्त्रे

जनिता मन्त्रे (6.4.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_53_janitA_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "janitA mantre",
    text_dev              = "जनिता मन्त्रे",
    padaccheda_dev        = "जनिता मन्त्रे",
    why_dev               = "(सूत्रम् 6.4.53) जनिता मन्त्रे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
