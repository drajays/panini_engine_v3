"""
2.1.48  पात्रेसमितादयश्च  —  VIDHI

Padaccheda: पात्रेसमितादयः च

patresamita etc. in samjna context form tatpurusha compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_48_patresamita"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pAtresamitAdayaSca",
    text_dev              = "पात्रेसमितादयश्च",
    padaccheda_dev        = "पात्रेसमितादयः च",
    why_dev               = "पात्रेसमित-आदिभ्यश्च संज्ञायां तत्पुरुषः (२.१.४८)।",
    anuvritti_from        = ('2.1.44',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
