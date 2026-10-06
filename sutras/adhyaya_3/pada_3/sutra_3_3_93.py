"""
3.3.93  कर्मण्यधिकरणे च  —  VIDHI

Padaccheda: कर्मणि अधिकरणे च

krt-suffix rule: कर्मण्यधिकरणे च
Pāṭha: ashtadhyayi.com data.txt row i=33093 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_93_karmaRyaDi_93"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.93", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.93"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRyaDikaraRe ca",
    text_dev              = "कर्मण्यधिकरणे च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm karmaRi aDikaraRe ca kft GoH kiH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् कर्मणि अधिकरणे च कृत् घोः किः",
    padaccheda_dev        = "कर्मणि अधिकरणे च",
    why_dev               = "धातोः प्रत्ययः (३.3.93)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
