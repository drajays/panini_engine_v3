"""
8.2.91  ब्रूहिप्रेष्यश्रौषड्वौषडावहानामादेः  —  VIDHI

Padaccheda: ब्रूहि-प्रेष्य-श्रौषतट्-वौषट्-आवहानाम् आदेः

ब्रूहिप्रेस्यश्रौषड्वौषडावहानामादेः (8.2.91)
Pāṭha: ashtadhyayi.com data.txt row i=82091 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_91_brUhipresy_91"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.91", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'brUhiprezyaSrOzaqvOzaqAvahAnAmAdeH',
    text_dev              = 'ब्रूहिप्रेष्यश्रौषड्वौषडावहानामादेः',
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH brUhipresyaSrOzaqvOzaqAvahAnAm AdeH yajYakarmaRi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः ब्रूहिप्रेस्यश्रौषड्वौषडावहानाम् आदेः यज्ञकर्मणि",
    padaccheda_dev        = "ब्रूहि-प्रेष्य-श्रौषतट्-वौषट्-आवहानाम् आदेः",
    why_dev               = "(सूत्रम् 8.2.91) ब्रूहिप्रेस्यश्रौषड्वौषडावहानामादेः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
