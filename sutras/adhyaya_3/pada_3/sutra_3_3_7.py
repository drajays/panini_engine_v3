"""
3.3.7  लिप्स्यमानसिद्धौ च  —  VIDHI

Padaccheda: लिप्स्यमान-सिद्धौ च

krt-suffix rule: लिप्स्यमानसिद्धौ च
Pāṭha: ashtadhyayi.com data.txt row i=33007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_7_lipsyamAna_7"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.7", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lipsyamAnasidDO ca",
    text_dev              = "लिप्स्यमानसिद्धौ च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Bavizyati lipsyamAna-sidDO ca kft yAvat-purA-nipAtayoH viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भविष्यति लिप्स्यमान-सिद्धौ च कृत् यावत्-पुरा-निपातयोः विभाषा",
    padaccheda_dev        = "लिप्स्यमान-सिद्धौ च",
    why_dev               = "धातोः प्रत्ययः (३.3.7)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
