"""
4.2.5  संज्ञायां श्रवणाश्वत्थाभ्याम्  —  VIDHI

Padaccheda: संज्ञायाम् श्रवण-अश्वत्थाभ्याम्

संज्ञायां श्रवणाश्वत्थाभ्याम् (4.2.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_5_saMjYAyAM_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.5", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAM SravaRASvatTAByAm",
    text_dev              = "संज्ञायां श्रवणाश्वत्थाभ्याम्",
    padaccheda_dev        = "संज्ञायाम् श्रवण-अश्वत्थाभ्याम्",
    why_dev               = "(सूत्रम् 4.2.5) संज्ञायां श्रवणाश्वत्थाभ्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
