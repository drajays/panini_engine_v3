"""
6.2.191  अतेरकृत्पदे  —  VIDHI

Padaccheda: अतेः अ-कृत्-पदे

अतेरकृत्पदे (6.2.191)
Pāṭha: ashtadhyayi.com data.txt row i=62191 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_191_aterakftpa_191"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.191", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.191"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.191",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aterakftpade",
    text_dev              = "अतेरकृत्पदे",
    samagra_slp1          = "uttarapadAdiH antaH ateH akftpade upasargAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः अतेः अकृत्पदे उपसर्गात्",
    padaccheda_dev        = "अतेः अ-कृत्-पदे",
    why_dev               = "(सूत्रम् 6.2.191) अतेरकृत्पदे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
