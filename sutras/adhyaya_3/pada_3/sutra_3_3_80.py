"""
3.3.80  उद्घनोऽत्याधानम्  —  VIDHI

Padaccheda: उद्‍घनः अत्याधानम्

krt-suffix rule: उद्घनोऽत्याधानम्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_80_udGanotyA_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_80_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udGano'tyADAnam",
    text_dev              = "उद्घनोऽत्याधानम्",
    padaccheda_dev        = "उद्‍घनः अत्याधानम्",
    why_dev               = "धातोः प्रत्ययः (३.3.80)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
