"""
8.2.83  प्रत्यभिवादेऽशूद्रे  —  VIDHI

Padaccheda: प्रत्यभिवादे अशूद्रे

प्रत्यभिवादेअशूद्रे (8.2.83)
Pāṭha: ashtadhyayi.com data.txt row i=82083 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_83_pratyaBivA_83"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.83", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'pratyaBivAdeSUdre',
    text_dev              = 'प्रत्यभिवादेऽशूद्रे',
    samagra_slp1          = "aSUdravizaye pratyaBivAde vAkyasya weH plutaH udAttaH ",
    samagra_dev           = "अशूद्रविषये प्रत्यभिवादे वाक्यस्य टेः प्लुतः उदात्तः ।",
    padaccheda_dev        = "प्रत्यभिवादे अशूद्रे",
    why_dev               = "(सूत्रम् 8.2.83) प्रत्यभिवादेअशूद्रे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
