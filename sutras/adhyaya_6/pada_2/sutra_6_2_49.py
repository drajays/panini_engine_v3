"""
6.2.49  गतिरनन्तरः  —  VIDHI

Padaccheda: गतिः अनन्तरः

गतिरनन्तरः (6.2.49)
Pāṭha: ashtadhyayi.com data.txt row i=62049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_49_gatiranant_49"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.49", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gatiranantaraH",
    text_dev              = "गतिरनन्तरः",
    samagra_slp1          = "gatiH anantaraH pUrvapadam prakftyA kte karmaRi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "गतिः अनन्तरः पूर्वपदम् प्रकृत्या क्ते कर्मणि",
    padaccheda_dev        = "गतिः अनन्तरः",
    why_dev               = "(सूत्रम् 6.2.49) गतिरनन्तरः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
