"""
7.1.74  तृतीयादिषु भाषितपुंस्कं पुंवद्गालवस्य  —  VIDHI

Padaccheda: तृतीया-आदिषु भाषितपुंस्कम् पुंवत् गालवस्य

तृतीयाऽऽदिषु भाषितपुंस्कं पुंवद्गालवस्य (7.1.74)
Pāṭha: ashtadhyayi.com data.txt row i=71074 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_74_tftIyAdi_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.74", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'tftIyAdizu BAzitapuMskaM puMvadgAlavasya',
    text_dev              = 'तृतीयादिषु भाषितपुंस्कं पुंवद्गालवस्य',
    samagra_slp1          = "BAzitapuMskasya napuMsakasya ikaH aNgasya tftIyAdizu aci viBaktO puMvad - gAlavasya",
    samagra_dev           = "भाषितपुंस्कस्य नपुंसकस्य इकः अङ्गस्य तृतीयादिषु अचि विभक्तौ पुंवद् - गालवस्य",
    padaccheda_dev        = "तृतीया-आदिषु भाषितपुंस्कम् पुंवत् गालवस्य",
    why_dev               = "(सूत्रम् 7.1.74) तृतीयाऽऽदिषु भाषितपुंस्कं पुंवद्गालवस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
