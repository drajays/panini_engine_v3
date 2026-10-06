"""
5.2.70  तन्त्रादचिरापहृते  —  VIDHI

Padaccheda: तन्त्रात् अचिरापहृते

तन्त्रादचिरापहृते (5.2.70)
Pāṭha: ashtadhyayi.com data.txt row i=52070 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_70_tantrAdaci_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.70", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tantrAdacirApahfte",
    text_dev              = "तन्त्रादचिरापहृते",
    samagra_slp1          = "acira-apahfte iti tantrAt kan",
    samagra_dev           = "'अचिर-अपहृते' (इति) तन्त्रात् कन्",
    padaccheda_dev        = "तन्त्रात् अचिरापहृते",
    why_dev               = "(सूत्रम् 5.2.70) तन्त्रादचिरापहृते।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
