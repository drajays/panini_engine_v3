"""
6.3.137  अन्येषामपि दृश्यते  —  VIDHI

Padaccheda: अन्येषाम् अपि दृश्यते (क्रियापदम्)

अन्येषामपि दृश्यते (6.3.137)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_137_anyezAmapi_137"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_137_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anyezAmapi dfSyate",
    text_dev              = "अन्येषामपि दृश्यते",
    padaccheda_dev        = "अन्येषाम् अपि दृश्यते (क्रियापदम्)",
    why_dev               = "(सूत्रम् 6.3.137) अन्येषामपि दृश्यते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
