"""
3.4.11  दृशे विख्ये च  —  VIDHI

Padaccheda: दृशे विख्ये च

krt-suffix rule: दृशे विख्ये च
Pāṭha: ashtadhyayi.com data.txt row i=34011 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_11_dfSe_11"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.11", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dfSe viKye ca",
    text_dev              = "दृशे विख्ये च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH dfSe viKye ca kft Candasi tumarTe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः दृशे विख्ये च कृत् छन्दसि तुमर्थे",
    padaccheda_dev        = "दृशे विख्ये च",
    why_dev               = "धातोः प्रत्ययः (३.4.11)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
