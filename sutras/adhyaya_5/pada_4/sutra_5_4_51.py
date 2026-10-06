"""
5.4.51  अरुर्मनश्चक्षुश्चेतोरहोरजसां लोपश्च  —  VIDHI

Padaccheda: अरुस्-मनस्-चक्षुस्-चेतस्-रहस्-रजसाम् लोपः च

अरुर्मनश्चक्षुश्चेतोरहोरजसां लोपश्च (5.4.51)
Pāṭha: ashtadhyayi.com data.txt row i=54051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_51_arurmanaSc_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.51", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arurmanaScakzuScetorahorajasAM lopaSca",
    text_dev              = "अरुर्मनश्चक्षुश्चेतोरहोरजसां लोपश्च",
    samagra_slp1          = "aBUtaBAve sampadyakartati kf-BU-astiyoge arus-manas-cakzus-cetas-rahas-rajasAm cvO lopaH",
    samagra_dev           = "अभूतभावे सम्पद्यकर्तति कृ-भू-अस्तियोगे अरुस्-मनस्-चक्षुस्-चेतस्-रहस्-रजसाम् च्वौ लोपः",
    padaccheda_dev        = "अरुस्-मनस्-चक्षुस्-चेतस्-रहस्-रजसाम् लोपः च",
    why_dev               = "(सूत्रम् 5.4.51) अरुर्मनश्चक्षुश्चेतोरहोरजसां लोपश्च।",
    anuvritti_from        = ('4.1.76',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
