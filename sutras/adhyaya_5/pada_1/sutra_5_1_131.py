"""
5.1.131  इगन्ताच्च लघुपूर्वात्  —  VIDHI

Padaccheda: इक्-अन्तात् च लघु-पूर्वात्

इगन्ताच्च लघुपूर्वात् (5.1.131)
Pāṭha: ashtadhyayi.com data.txt row i=51131 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_131_igantAcca_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.131", state, "5.1.120"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "igantAcca laGupUrvAt",
    text_dev              = "इगन्ताच्च लघुपूर्वात्",
    samagra_slp1          = "tasya BAvaH  karmaRi ca iti igantAt laGupUrvAt aR",
    samagra_dev           = "'तस्य भावः , कर्मणि च' (इति) इगन्तात् लघुपूर्वात् अण्",
    padaccheda_dev        = "इक्-अन्तात् च लघु-पूर्वात्",
    why_dev               = "(सूत्रम् 5.1.131) इगन्ताच्च लघुपूर्वात्।",
    anuvritti_from        = ('5.1.120',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
