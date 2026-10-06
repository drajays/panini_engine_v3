"""
3.4.25  कर्मण्याक्रोशे कृञः खमुञ्  —  VIDHI

Padaccheda: कर्मणि आक्रोशे कृञः खमुञ्

krt-suffix rule: कर्मण्याक्रोशे कृञः खमुञ्
Pāṭha: ashtadhyayi.com data.txt row i=34025 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_25_karmaRyAkr_25"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.25", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRyAkroSe kfYaH KamuY",
    text_dev              = "कर्मण्याक्रोशे कृञः खमुञ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH karmaRi AkroSe kfYaH KamuY kft samAnakarttfkayoH pUrvakAle",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कर्मणि आक्रोशे कृञः खमुञ् कृत् समानकर्त्तृकयोः पूर्वकाले",
    padaccheda_dev        = "कर्मणि आक्रोशे कृञः खमुञ्",
    why_dev               = "धातोः प्रत्ययः (३.4.25)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
