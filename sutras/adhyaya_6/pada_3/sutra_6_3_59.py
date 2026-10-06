"""
6.3.59  एकहलादौ पूरयितव्येऽन्यतरस्याम्  —  VIDHI

Padaccheda: एक-हल्-आदौ पूरयितव्ये अन्यतरस्याम्

एकहलादौ पूरयितव्येऽन्यतरस्याम् (6.3.59)
Pāṭha: ashtadhyayi.com data.txt row i=63059 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_59_ekahalAdO_59"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.59", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'ekahalAdO pUrayitavyenyatarasyAm',
    text_dev              = 'एकहलादौ पूरयितव्येऽन्यतरस्याम्',
    samagra_slp1          = "uttarapade ekahalAdO pUrayitavye anyatarasyAm treH udakasya udaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे एकहलादौ पूरयितव्ये अन्यतरस्याम् त्रेः उदकस्य उदः",
    padaccheda_dev        = "एक-हल्-आदौ पूरयितव्ये अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.3.59) एकहलादौ पूरयितव्येऽन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
