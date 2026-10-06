"""
6.2.139  गतिकारकोपपदात् कृत्  —  VIDHI

Padaccheda: गति-कारक-उपपदात् कृत्

गतिकारकोपपदात् कृत् (6.2.139)
Pāṭha: ashtadhyayi.com data.txt row i=62139 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_139_gatikArako_139"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.139", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.139"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.139",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gatikArakopapadAt kft",
    text_dev              = "गतिकारकोपपदात् कृत्",
    samagra_slp1          = "uttarapadAdiH gatikAraka-upapadAt kft prakftyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः गतिकारक-उपपदात् कृत् प्रकृत्या",
    padaccheda_dev        = "गति-कारक-उपपदात् कृत्",
    why_dev               = "(सूत्रम् 6.2.139) गतिकारकोपपदात् कृत्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
