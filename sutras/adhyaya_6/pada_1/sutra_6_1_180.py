"""
6.1.180  झल्युपोत्तमम्  —  VIDHI

Padaccheda: झलि उप-उत्तमम्

झल्युपोत्तमम् (6.1.180)
Pāṭha: ashtadhyayi.com data.txt row i=61180 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_180_Jalyupotta_180"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.180", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.180"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.180",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Jalyupottamam",
    text_dev              = "झल्युपोत्तमम्",
    samagra_slp1          = "Jali upottamam udAttaH antaH viBaktiH nAm anyatarasyAm zaw-tri-caturByaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "झलि उपोत्तमम् उदात्तः अन्तः विभक्तिः नाम् अन्यतरस्याम् षट्-त्रि-चतुर्भ्यः",
    padaccheda_dev        = "झलि उप-उत्तमम्",
    why_dev               = "(सूत्रम् 6.1.180) झल्युपोत्तमम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
