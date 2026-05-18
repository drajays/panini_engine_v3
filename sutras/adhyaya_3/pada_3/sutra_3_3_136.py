"""
3.3.136  भविष्यति मर्यादावचनेऽवरस्मिन्  —  VIDHI

Padaccheda: भविष्यति मर्यादावचने अवरस्मिन्

krt-suffix rule: भविष्यति मर्यादावचनेऽवरस्मिन्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_136_Bavizyati_136"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_136_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Bavizyati maryAdAvacane'varasmin",
    text_dev              = "भविष्यति मर्यादावचनेऽवरस्मिन्",
    padaccheda_dev        = "भविष्यति मर्यादावचने अवरस्मिन्",
    why_dev               = "धातोः प्रत्ययः (३.3.136)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
