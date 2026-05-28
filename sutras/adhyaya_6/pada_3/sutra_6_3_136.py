"""
6.3.136  निपातस्य च  —  VIDHI

Padaccheda: निपातस्य च

निपातस्य च (6.3.136)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_136_nipAtasya_136"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nipAtasya ca",
    text_dev              = "निपातस्य च",
    padaccheda_dev        = "निपातस्य च",
    why_dev               = "(सूत्रम् 6.3.136) निपातस्य च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
