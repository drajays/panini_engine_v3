"""
2.4.66  बह्वचः इञः प्राच्यभरतेषु  —  VIDHI

Padaccheda: बहु-अचः इञः प्राच्यभरतेषु

Bahvac with inja in pracya and bharata territory.
Pāṭha: ashtadhyayi.com data.txt row i=24066 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_66_bahvac_inja_pracya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_66_yuna_context") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["luk_kind"]             = "2.4.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahvacaH iYaH prAcyaBaratezu",
    text_dev              = "बह्वचः इञः प्राच्यभरतेषु",
    samagra_slp1          = "bahu-acaH iYaH prAcya-Baratezu luk bahuzu tena eva astriyAm gotre",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "बहु-अचः इञः प्राच्य-भरतेषु लुक् बहुषु तेन एव अस्त्रियाम् गोत्रे",
    padaccheda_dev        = "बहु-अचः इञः प्राच्यभरतेषु",
    why_dev               = "बहु-अचः इञः प्राच्यभरतेषु (२.४.६६)।",
    anuvritti_from        = ('2.4.58',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
