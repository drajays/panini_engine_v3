"""
5.2.140  अहंशुभमोर्युस्  —  VIDHI

Padaccheda: अहं-शुभमोः युस्

अहंशुभमोर्युस् (5.2.140)
Pāṭha: ashtadhyayi.com data.txt row i=52140 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_140_ahaMSuBamo_140"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.140", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.140"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.140",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ahaMSuBamoryus",
    text_dev              = "अहंशुभमोर्युस्",
    samagra_slp1          = "tat asya asmin astIti iti aham-SuBamoH yus",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) अहम्-शुभमोः युस्",
    padaccheda_dev        = "अहं-शुभमोः युस्",
    why_dev               = "(सूत्रम् 5.2.140) अहंशुभमोर्युस्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
