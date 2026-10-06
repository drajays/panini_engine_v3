"""
8.4.63  शश्छोऽटि  —  VIDHI

Padaccheda: शस् । छः । अटि

शश्छोऽटि (8.4.63)
Pāṭha: ashtadhyayi.com data.txt row i=84063 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_63_SaSCowi_63"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.63", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'SaSCowi',
    text_dev              = 'शश्छोऽटि',
    samagra_slp1          = "padAntAt JayaH SaH CaH vA awi",
    samagra_dev           = "पदान्तात् झयः शः छः वा अटि",
    padaccheda_dev        = "शस् । छः । अटि",
    why_dev               = "(सूत्रम् 8.4.63) शश्छोऽटि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
