"""
7.3.28  प्रवाहणस्य ढे  —  VIDHI

Padaccheda: प्रवाहणस्य ढे

प्रवाहणस्य ढे (7.3.28)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_28_pravAhaRas_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_28_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pravAhaRasya Qe",
    text_dev              = "प्रवाहणस्य ढे",
    padaccheda_dev        = "प्रवाहणस्य ढे",
    why_dev               = "(सूत्रम् 7.3.28) प्रवाहणस्य ढे।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
