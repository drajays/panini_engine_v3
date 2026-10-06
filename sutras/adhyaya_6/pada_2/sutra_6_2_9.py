"""
6.2.9  शारदेऽनार्तवे  —  VIDHI

Padaccheda: शारदे अनार्तवे

शारदेअनार्तवे (6.2.9)
Pāṭha: ashtadhyayi.com data.txt row i=62009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_9_SAradeanAr_9"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.9", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'SAradenArtave',
    text_dev              = 'शारदेऽनार्तवे',
    samagra_slp1          = "SArade anArtave prakftyA pUrvapadam tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "शारदे अनार्तवे प्रकृत्या पूर्वपदम् तत्पुरुषे",
    padaccheda_dev        = "शारदे अनार्तवे",
    why_dev               = "(सूत्रम् 6.2.9) शारदेअनार्तवे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
