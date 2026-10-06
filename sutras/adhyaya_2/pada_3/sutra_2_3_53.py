"""
2.3.53  कृञः प्रतियत्ने  —  VIDHI

Padaccheda: कृञः प्रतियत्ने

krnj in effort context takes sasthi.
Pāṭha: ashtadhyayi.com data.txt row i=23053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_53_krnjas_pratiyatna"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfYaH pratiyatne",
    text_dev              = "कृञः प्रतियत्ने",
    samagra_slp1          = "anaBihite kfYaH pratiyatne Seze zazWI karmaRi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनभिहिते कृञः प्रतियत्ने शेषे षष्ठी कर्मणि",
    padaccheda_dev        = "कृञः प्रतियत्ने",
    why_dev               = "कृञः प्रतियत्ने षष्ठी (२.३.५३)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
