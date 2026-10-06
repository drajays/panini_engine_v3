"""
5.2.87  सपूर्वाच्च  —  VIDHI

Padaccheda: स-पूर्वात् च

सपूर्वाच्च (5.2.87)
Pāṭha: ashtadhyayi.com data.txt row i=52087 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_87_sapUrvAcca_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.87", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sapUrvAcca",
    text_dev              = "सपूर्वाच्च",
    samagra_slp1          = "anena iti sapUrvAt pUrvAt iniH",
    samagra_dev           = "'अनेन' (इति) सपूर्वात् पूर्वात् इनिः",
    padaccheda_dev        = "स-पूर्वात् च",
    why_dev               = "(सूत्रम् 5.2.87) सपूर्वाच्च।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
