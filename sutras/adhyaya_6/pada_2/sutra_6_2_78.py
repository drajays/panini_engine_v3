"""
6.2.78  गोतन्तियवं पाले  —  VIDHI

Padaccheda: गो-तन्ति-यवम् पाले

गोतन्तियवं पाले (6.2.78)
Pāṭha: ashtadhyayi.com data.txt row i=62078 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_78_gotantiyav_78"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.78", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.78"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.78",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gotantiyavaM pAle",
    text_dev              = "गोतन्तियवं पाले",
    samagra_slp1          = "AdiH udAttaH go-tanti-yavam pAle pUrvapadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आदिः उदात्तः गो-तन्ति-यवम् पाले पूर्वपदम्",
    padaccheda_dev        = "गो-तन्ति-यवम् पाले",
    why_dev               = "(सूत्रम् 6.2.78) गोतन्तियवं पाले।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
