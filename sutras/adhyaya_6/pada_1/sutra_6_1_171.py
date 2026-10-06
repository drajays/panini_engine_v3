"""
6.1.171  ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः  —  VIDHI

Padaccheda: ऊट्-इदम्-पदादि-अप्-पुम्-रै-द्युभ्यः

ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः (6.1.171)
Pāṭha: ashtadhyayi.com data.txt row i=61171 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_171_UqidampadA_171"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.171", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.171"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.171",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UqidampadAdyappumrEdyuByaH",
    text_dev              = "ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः",
    samagra_slp1          = "UW-idam-padAdi-ap-pum-rE-dyuByaH udAttaH antaH viBaktiH antodattAt aYceH Candasi asarvanAmasTAnam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "ऊठ्-इदम्-पदादि-अप्-पुम्-रै-द्युभ्यः उदात्तः अन्तः विभक्तिः अन्तोदत्तात् अञ्चेः छन्दसि असर्वनामस्थानम्",
    padaccheda_dev        = "ऊट्-इदम्-पदादि-अप्-पुम्-रै-द्युभ्यः",
    why_dev               = "(सूत्रम् 6.1.171) ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
