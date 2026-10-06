"""
8.2.102  उपरिस्विदासीदिति च  —  VIDHI

Padaccheda: उपरि स्वित् आसीत् (क्रियापदम्) इति च

उपरिस्विदासीदिति च (8.2.102)
Pāṭha: ashtadhyayi.com data.txt row i=82102 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_102_uparisvidA_102"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.102", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uparisvidAsIditi ca",
    text_dev              = "उपरिस्विदासीदिति च",
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH upari svit AsIt iti ca anudAttam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः उपरि स्वित् आसीत् इति च अनुदात्तम्",
    padaccheda_dev        = "उपरि स्वित् आसीत् (क्रियापदम्) इति च",
    why_dev               = "(सूत्रम् 8.2.102) उपरिस्विदासीदिति च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
