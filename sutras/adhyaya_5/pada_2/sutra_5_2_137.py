"""
5.2.137  संज्ञायां मन्माभ्याम्.ह्  —  VIDHI

Padaccheda: संज्ञायाम् मन्-मभ्याम्

संज्ञायां मन्माभ्याम्.ह् (5.2.137)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_137_saMjYAyAM_137"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.137", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM manmAByAm.h",
    text_dev              = "संज्ञायां मन्माभ्याम्.ह्",
    padaccheda_dev        = "संज्ञायाम् मन्-मभ्याम्",
    why_dev               = "(सूत्रम् 5.2.137) संज्ञायां मन्माभ्याम्.ह्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
