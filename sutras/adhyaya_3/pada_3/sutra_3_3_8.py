"""
3.3.8  लोडर्थलक्षणे च  —  VIDHI

Padaccheda: लोट्-अर्थ-लक्षणे च

krt-suffix rule: लोडर्थलक्षणे च
Pāṭha: ashtadhyayi.com data.txt row i=33008 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_8_loqarTalak_8"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.8", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "loqarTalakzaRe ca",
    text_dev              = "लोडर्थलक्षणे च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Bavizyati low-arTalakzaRe ca kft yAvat-purA-nipAtayoH viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भविष्यति लोट्-अर्थलक्षणे च कृत् यावत्-पुरा-निपातयोः विभाषा",
    padaccheda_dev        = "लोट्-अर्थ-लक्षणे च",
    why_dev               = "धातोः प्रत्ययः (३.3.8)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
