"""
5.4.24  देवतान्तात्तादर्थ्ये यत्  —  VIDHI

Padaccheda: देवत-अन्तात् तादर्थ्ये यत्

देवतान्तात्तादर्थ्ये यत् (5.4.24)
Pāṭha: ashtadhyayi.com data.txt row i=54024 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_24_devatAntAt_24"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.24", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.24"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.24",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "devatAntAttAdarTye yat",
    text_dev              = "देवतान्तात्तादर्थ्ये यत्",
    samagra_slp1          = "devatAntAt tAdarTye yat",
    samagra_dev           = "देवतान्तात् तादर्थ्ये यत्",
    padaccheda_dev        = "देवत-अन्तात् तादर्थ्ये यत्",
    why_dev               = "(सूत्रम् 5.4.24) देवतान्तात्तादर्थ्ये यत्।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
