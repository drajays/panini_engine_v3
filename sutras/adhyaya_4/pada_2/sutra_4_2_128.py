"""
4.2.128  नगरात् कुत्सनप्रावीण्ययोः  —  VIDHI

Padaccheda: नगरात् कुत्सन-प्रावीण्ययोः

नगरात् कुत्सनप्रावीण्ययोः (4.2.128)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_128_nagarAt_128"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_128_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.128"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.128",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nagarAt kutsanaprAvIRyayoH",
    text_dev              = "नगरात् कुत्सनप्रावीण्ययोः",
    padaccheda_dev        = "नगरात् कुत्सन-प्रावीण्ययोः",
    why_dev               = "(सूत्रम् 4.2.128) नगरात् कुत्सनप्रावीण्ययोः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
