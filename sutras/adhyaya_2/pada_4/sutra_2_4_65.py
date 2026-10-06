"""
2.4.65  अत्रिभृगुकुत्सवसिष्ठगोतमाङ्गिरोभ्यश्च  —  VIDHI

Padaccheda: अत्रि-भृगु-कुत्स-वसिष्ठ-गोतम-अङ्गिरोभ्यः च

Also for atri, bhrgu, kutsa, vasistha, gautama, angiras.
Pāṭha: ashtadhyayi.com data.txt row i=24065 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_65_atri_bhrgu"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_65_yuna_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "atriBfgukutsavasizWagotamANgiroByaSca",
    text_dev              = "अत्रिभृगुकुत्सवसिष्ठगोतमाङ्गिरोभ्यश्च",
    samagra_slp1          = "atri-Bfgu-kutsa-vasizWa-gotama-aNgiroByaH ca luk bahuzu tena eva astriyAm gotre",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अत्रि-भृगु-कुत्स-वसिष्ठ-गोतम-अङ्गिरोभ्यः च लुक् बहुषु तेन एव अस्त्रियाम् गोत्रे",
    padaccheda_dev        = "अत्रि-भृगु-कुत्स-वसिष्ठ-गोतम-अङ्गिरोभ्यः च",
    why_dev               = "अत्रि-भृगु-कुत्स-वसिष्ठ-गोतम-अङ्गिरोभ्यः च (२.४.६५)।",
    anuvritti_from        = ('2.4.63',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
