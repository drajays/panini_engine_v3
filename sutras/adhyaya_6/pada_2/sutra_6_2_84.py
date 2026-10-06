"""
6.2.84  ग्रामेऽनिवसन्तः  —  VIDHI

Padaccheda: ग्रामे अनिवसन्तः

ग्रामेऽनिवसन्तः (6.2.84)
Pāṭha: ashtadhyayi.com data.txt row i=62084 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_84_grAmeniva_84"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.84", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.84"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'grAmenivasantaH',
    text_dev              = 'ग्रामेऽनिवसन्तः',
    samagra_slp1          = "AdiH udAttaH grAme anivasantaH pUrvapadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आदिः उदात्तः ग्रामे अनिवसन्तः पूर्वपदम्",
    padaccheda_dev        = "ग्रामे अनिवसन्तः",
    why_dev               = "(सूत्रम् 6.2.84) ग्रामेऽनिवसन्तः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
