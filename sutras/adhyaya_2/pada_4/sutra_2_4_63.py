"""
2.4.63  यस्कादिभ्यो गोत्रे  —  VIDHI

Padaccheda: यस्क-आदिभ्यः गोत्रे

For yaska etc. in gotra context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_63_yaska_gotre"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_63_yuna_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaskAdiByo gotre",
    text_dev              = "यस्कादिभ्यो गोत्रे",
    padaccheda_dev        = "यस्क-आदिभ्यः गोत्रे",
    why_dev               = "यस्क-आदिभ्यः गोत्रे (२.४.६३)।",
    anuvritti_from        = ('2.4.62',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
