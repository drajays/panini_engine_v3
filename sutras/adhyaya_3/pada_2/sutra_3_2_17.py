"""
3.2.17  भिक्षासेनाऽऽदायेषु च  —  VIDHI

Padaccheda: भिक्षा-सेना-आदायेषु च

krt-suffix rule: भिक्षासेनाऽऽदायेषु च (17)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_17_BikzAsenA_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BikzAsenA''dAyezu ca",
    text_dev              = "भिक्षासेनाऽऽदायेषु च",
    padaccheda_dev        = "भिक्षा-सेना-आदायेषु च",
    why_dev               = "धातोः कृत्-प्रत्ययः [भिक्षासेनाऽऽदायेषु च] विहितः (३.२.17)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
