"""
6.3.77  नगोऽप्राणिष्वन्यतरस्याम्  —  VIDHI

Padaccheda: नगः अप्राणिषु अन्यतरस्याम्

नगोऽप्राणिष्वन्यतरस्याम् (6.3.77)
Pāṭha: ashtadhyayi.com data.txt row i=63077 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_77_nagoprARi_77"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.77", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'nagoprARizvanyatarasyAm',
    text_dev              = 'नगोऽप्राणिष्वन्यतरस्याम्',
    samagra_slp1          = "uttarapade nagaH aprARizu anyatarasyAm naYaH prakftyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे नगः अप्राणिषु अन्यतरस्याम् नञः प्रकृत्या",
    padaccheda_dev        = "नगः अप्राणिषु अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.3.77) नगोऽप्राणिष्वन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
