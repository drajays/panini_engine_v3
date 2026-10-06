"""
6.2.62  ग्रामः शिल्पिनि  —  VIDHI

Padaccheda: ग्रामः शिल्पिनि

ग्रामः शिल्पिनि (6.2.62)
Pāṭha: ashtadhyayi.com data.txt row i=62062 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_62_grAmaH_62"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.62", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAmaH Silpini",
    text_dev              = "ग्रामः शिल्पिनि",
    samagra_slp1          = "grAmaH Silpini prakftyA pUrvapadam anyatarasyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "ग्रामः शिल्पिनि प्रकृत्या पूर्वपदम् अन्यतरस्याम्",
    padaccheda_dev        = "ग्रामः शिल्पिनि",
    why_dev               = "(सूत्रम् 6.2.62) ग्रामः शिल्पिनि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
