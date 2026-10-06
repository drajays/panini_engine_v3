"""
6.2.120  वीरवीर्यौ च  —  VIDHI

Padaccheda: वीर-वीर्यौ च

वीरवीर्यौ च (6.2.120)
Pāṭha: ashtadhyayi.com data.txt row i=62120 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_120_vIravIryO_120"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.120", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.120"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vIravIryO ca",
    text_dev              = "वीरवीर्यौ च",
    samagra_slp1          = "udAttaH uttarapadAdiH vIra-vIryO ca bahuvrIhO soH Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः वीर-वीर्यौ च बहुव्रीहौ सोः छन्दसि",
    padaccheda_dev        = "वीर-वीर्यौ च",
    why_dev               = "(सूत्रम् 6.2.120) वीरवीर्यौ च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
