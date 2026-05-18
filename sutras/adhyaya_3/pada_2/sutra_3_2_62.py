"""
3.2.62  भजो ण्विः  —  VIDHI

Padaccheda: भजः ण्विः

krt-suffix rule: भजो ण्विः (62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_62_Bajo_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Bajo RviH",
    text_dev              = "भजो ण्विः",
    padaccheda_dev        = "भजः ण्विः",
    why_dev               = "धातोः कृत्-प्रत्ययः [भजो ण्विः] विहितः (३.२.62)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
