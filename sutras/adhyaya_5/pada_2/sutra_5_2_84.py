"""
5.2.84  श्रोत्रियंश्छन्दोऽधीते  —  VIDHI

Padaccheda: श्रोत्रियन् छन्दः अधीते (क्रियापदम्)

श्रोत्रियंश्छन्दोऽधीते (5.2.84)
Pāṭha: ashtadhyayi.com data.txt row i=52084 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_84_SrotriyaMS_84"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.84", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.84"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'SrotriyaMSCandoDIte',
    text_dev              = 'श्रोत्रियंश्छन्दोऽधीते',
    samagra_slp1          = "CandaH aDIte iti Srotriyan vA nipAtyate",
    samagra_dev           = "'छन्दः अधीते' (इति) श्रोत्रियन् वा (निपात्यते)",
    padaccheda_dev        = "श्रोत्रियन् छन्दः अधीते (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.2.84) श्रोत्रियंश्छन्दोऽधीते।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
