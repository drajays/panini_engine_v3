"""
4.2.29  महेन्द्राद्घाणौ च  —  VIDHI

Padaccheda: महेन्द्रात् घ-अणौ च

महेन्द्राद्घाणौ च (4.2.29)
Pāṭha: ashtadhyayi.com data.txt row i=42029 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_29_mahendrAdG_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.29", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mahendrAdGARO ca",
    text_dev              = "महेन्द्राद्घाणौ च",
    samagra_slp1          = "sA asya devatA iti mahendrAt Ga-aRO Ca ca",
    samagra_dev           = "'सा अस्य देवता' (इति) महेन्द्रात् घ-अणौ, छ च",
    padaccheda_dev        = "महेन्द्रात् घ-अणौ च",
    why_dev               = "(सूत्रम् 4.2.29) महेन्द्राद्घाणौ च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
