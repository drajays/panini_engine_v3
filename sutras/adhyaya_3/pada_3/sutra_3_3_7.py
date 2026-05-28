"""
3.3.7  लिप्स्यमानसिद्धौ च  —  VIDHI

Padaccheda: लिप्स्यमान-सिद्धौ च

krt-suffix rule: लिप्स्यमानसिद्धौ च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_7_lipsyamAna_7"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lipsyamAnasidDO ca",
    text_dev              = "लिप्स्यमानसिद्धौ च",
    padaccheda_dev        = "लिप्स्यमान-सिद्धौ च",
    why_dev               = "धातोः प्रत्ययः (३.3.7)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
