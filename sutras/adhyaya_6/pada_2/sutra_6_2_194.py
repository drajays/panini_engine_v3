"""
6.2.194  उपाद् द्व्यजजिनमगौरादयः  —  VIDHI

Padaccheda: उपात् द्वि-अच्-अजिन अगौर-आदयः

उपाद् द्व्यजजिनमगौरादयः (6.2.194)
Pāṭha: ashtadhyayi.com data.txt row i=62194 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_194_upAd_194"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.194", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.194"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.194",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upAd dvyajajinamagOrAdayaH",
    text_dev              = "उपाद् द्व्यजजिनमगौरादयः",
    samagra_slp1          = "uttarapadAdiH antaH upAt dvyajajinam agOrAdayaH upasargAt tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः उपात् द्व्यजजिनम् अगौरादयः उपसर्गात् तत्पुरुषे",
    padaccheda_dev        = "उपात् द्वि-अच्-अजिन अगौर-आदयः",
    why_dev               = "(सूत्रम् 6.2.194) उपाद् द्व्यजजिनमगौरादयः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
