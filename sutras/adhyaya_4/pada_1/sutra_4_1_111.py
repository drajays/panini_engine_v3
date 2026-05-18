"""
4.1.111  भर्गात् त्रैगर्ते  —  VIDHI

Padaccheda: भर्गात् त्रैगर्ते

भर्गात् त्रैगर्ते (4.1.111)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_111_BargAt_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_111_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BargAt trEgarte",
    text_dev              = "भर्गात् त्रैगर्ते",
    padaccheda_dev        = "भर्गात् त्रैगर्ते",
    why_dev               = "(सूत्रम् 4.1.111) भर्गात् त्रैगर्ते।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
