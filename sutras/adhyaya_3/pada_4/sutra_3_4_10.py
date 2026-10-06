"""
3.4.10  प्रयै रोहिष्यै अव्यथिष्यै  —  VIDHI

Padaccheda: प्रयै रोहिष्यै अव्यथिष्यै

krt-suffix rule: प्रयै रोहिष्यै अव्यथिष्यै
Pāṭha: ashtadhyayi.com data.txt row i=34010 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_10_prayE_10"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.10", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prayE rohizyE avyaTizyE",
    text_dev              = "प्रयै रोहिष्यै अव्यथिष्यै",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH prayE rohizyE avyaTizyE kft Candasi tumarTe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः प्रयै रोहिष्यै अव्यथिष्यै कृत् छन्दसि तुमर्थे",
    padaccheda_dev        = "प्रयै रोहिष्यै अव्यथिष्यै",
    why_dev               = "धातोः प्रत्ययः (३.4.10)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
