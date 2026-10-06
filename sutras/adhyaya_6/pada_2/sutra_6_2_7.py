"""
6.2.7  पदेऽपदेशे  —  VIDHI

Padaccheda: पदे अपदेशे

पदेऽपदेशे (6.2.7)
Pāṭha: ashtadhyayi.com data.txt row i=62007 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_7_padepadeS_7"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.7", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'padepadeSe',
    text_dev              = 'पदेऽपदेशे',
    samagra_slp1          = "pade apadeSe prakftyA pUrvapadam tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदे अपदेशे प्रकृत्या पूर्वपदम् तत्पुरुषे",
    padaccheda_dev        = "पदे अपदेशे",
    why_dev               = "(सूत्रम् 6.2.7) पदेऽपदेशे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
