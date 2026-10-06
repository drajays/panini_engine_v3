"""
4.1.96  बाह्वादिभ्यश्च  —  VIDHI

Padaccheda: बाहु-आदिभ्यः च

बाह्वादिभ्यश्च (4.1.96)
Pāṭha: ashtadhyayi.com data.txt row i=41096 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_96_bAhvAdiBya_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.96", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bAhvAdiByaSca",
    text_dev              = "बाह्वादिभ्यश्च",
    samagra_slp1          = "tasya apatyam iti bAhvAdiByaH iY pratyayaH",
    samagra_dev           = "'तस्य अपत्यम्' इति बाह्वादिभ्यः इञ् प्रत्ययः",
    padaccheda_dev        = "बाहु-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.1.96) बाह्वादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
