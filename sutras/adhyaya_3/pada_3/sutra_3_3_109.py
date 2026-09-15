"""
3.3.109  संज्ञायाम्  —  VIDHI

Padaccheda: संज्ञायाम्

krt-suffix rule: संज्ञायाम्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_109_saMjYAyAm_109"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.109", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.109"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.109",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAm",
    text_dev              = "संज्ञायाम्",
    padaccheda_dev        = "संज्ञायाम्",
    why_dev               = "धातोः प्रत्ययः (३.3.109)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
