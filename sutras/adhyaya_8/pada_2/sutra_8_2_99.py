"""
8.2.99  प्रतिश्रवणे च  —  VIDHI

Padaccheda: प्रतिश्रवणे च

प्रतिश्रवणे च (8.2.99)
Pāṭha: ashtadhyayi.com data.txt row i=82099 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_99_pratiSrava_99"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.99", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratiSravaRe ca",
    text_dev              = "प्रतिश्रवणे च",
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH pratiSravaRe ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः प्रतिश्रवणे च",
    padaccheda_dev        = "प्रतिश्रवणे च",
    why_dev               = "(सूत्रम् 8.2.99) प्रतिश्रवणे च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
