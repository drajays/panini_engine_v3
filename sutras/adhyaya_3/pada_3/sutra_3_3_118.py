"""
3.3.118  पुंसि संज्ञायां घः प्रायेण  —  VIDHI

Padaccheda: पुंसि संज्ञायाम् घः प्रायेण

krt-suffix rule: पुंसि संज्ञायां घः प्रायेण
Pāṭha: ashtadhyayi.com data.txt row i=33118 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_118_puMsi_118"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.118", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.118"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.118",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puMsi saMjYAyAM GaH prAyeRa",
    text_dev              = "पुंसि संज्ञायां घः प्रायेण",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH karaRADikaraRayoH puMsi saMjYAyAm GaH prAyeRa kft karaRa-aDikaraRayoH ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः करणाधिकरणयोः पुंसि संज्ञायाम् घः प्रायेण कृत् करण-अधिकरणयोः च",
    padaccheda_dev        = "पुंसि संज्ञायाम् घः प्रायेण",
    why_dev               = "धातोः प्रत्ययः (३.3.118)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
