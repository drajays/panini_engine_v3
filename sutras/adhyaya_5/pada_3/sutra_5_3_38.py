"""
5.3.38  उत्तराच्च  —  VIDHI

Padaccheda: उत्तरात् च

उत्तराच्च (5.3.38)
Pāṭha: ashtadhyayi.com data.txt row i=53038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_38_uttarAcca_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.38", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttarAcca",
    text_dev              = "उत्तराच्च",
    samagra_slp1          = "uttarAt saptamI-praTamAByaH dik-deSa-kAlezu dUre AhiH Ac ca",
    samagra_dev           = "उत्तरात्  सप्तमी-प्रथमाभ्यः दिक्-देश-कालेषु दूरे आहिः आच्  च",
    padaccheda_dev        = "उत्तरात् च",
    why_dev               = "(सूत्रम् 5.3.38) उत्तराच्च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
