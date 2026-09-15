"""
3.3.47  परौ यज्ञे  —  VIDHI

Padaccheda: परौ यज्ञे

krt-suffix rule: परौ यज्ञे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_47_parO_47"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.47", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parO yajYe",
    text_dev              = "परौ यज्ञे",
    padaccheda_dev        = "परौ यज्ञे",
    why_dev               = "धातोः प्रत्ययः (३.3.47)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
