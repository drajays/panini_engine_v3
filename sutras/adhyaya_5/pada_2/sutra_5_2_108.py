"""
5.2.108  द्युद्रुभ्यां मः  —  VIDHI

Padaccheda: द्यु-द्रुभ्याम् मः

द्युद्रुभ्यां मः (5.2.108)
Pāṭha: ashtadhyayi.com data.txt row i=52108 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_108_dyudruByAM_108"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.108", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dyudruByAM maH",
    text_dev              = "द्युद्रुभ्यां मः",
    samagra_slp1          = "tat asya asmin astIti iti dyu-druByAm maH",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) द्यु-द्रुभ्याम् मः",
    padaccheda_dev        = "द्यु-द्रुभ्याम् मः",
    why_dev               = "(सूत्रम् 5.2.108) द्युद्रुभ्यां मः।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
