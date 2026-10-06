"""
5.2.21  व्रातेन जीवति  —  VIDHI

Padaccheda: व्रातेन जीवति (क्रियापदम्)

व्रातेन जीवति (5.2.21)
Pāṭha: ashtadhyayi.com data.txt row i=52021 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_21_vrAtena_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.21", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vrAtena jIvati",
    text_dev              = "व्रातेन जीवति",
    samagra_slp1          = "vrAtena jIvati iti KaY",
    samagra_dev           = "'व्रातेन जीवति' (इति) खञ्",
    padaccheda_dev        = "व्रातेन जीवति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.2.21) व्रातेन जीवति।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
