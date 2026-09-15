"""
3.3.5  विभाषा कदाकर्ह्योः  —  VIDHI

Padaccheda: विभाषा कदा-कर्ह्योः

krt-suffix rule: विभाषा कदाकर्ह्योः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_5_viBAzA_5"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.5", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA kadAkarhyoH",
    text_dev              = "विभाषा कदाकर्ह्योः",
    padaccheda_dev        = "विभाषा कदा-कर्ह्योः",
    why_dev               = "धातोः प्रत्ययः (३.3.5)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
