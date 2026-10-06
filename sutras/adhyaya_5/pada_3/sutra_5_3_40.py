"""
5.3.40  अस्ताति च  —  VIDHI

Padaccheda: अस्ताति च

अस्ताति च (5.3.40)
Pāṭha: ashtadhyayi.com data.txt row i=53040 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_40_astAti_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.40", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "astAti ca",
    text_dev              = "अस्ताति च",
    samagra_slp1          = "pUrva-aDara-avarARAmastAti pur-aD-avaH",
    samagra_dev           = "पूर्व-अधर-अवराणामस्ताति पुर्-अध्-अवः",
    padaccheda_dev        = "अस्ताति च",
    why_dev               = "(सूत्रम् 5.3.40) अस्ताति च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
