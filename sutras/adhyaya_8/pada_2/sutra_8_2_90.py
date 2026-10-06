"""
8.2.90  याज्याऽन्तः  —  VIDHI

Padaccheda: याज्या-अन्तः

याज्याऽन्तः (8.2.90)
Pāṭha: ashtadhyayi.com data.txt row i=82090 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_90_yAjyAntaH_90"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.90", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'yAjyAntaH',
    text_dev              = 'याज्याऽन्तः',
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH yAjyAntaH yajYakarmaRi weH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः याज्याऽन्तः यज्ञकर्मणि टेः",
    padaccheda_dev        = "याज्या-अन्तः",
    why_dev               = "(सूत्रम् 8.2.90) याज्याऽन्तः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
