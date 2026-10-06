"""
8.3.33  मय उञो वो वा  —  VIDHI

Padaccheda: मयः उञो वः वा

मय उञो वो वा (8.3.33)
Pāṭha: ashtadhyayi.com data.txt row i=83033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_33_maya_33"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.33", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "maya uYo vo vA",
    text_dev              = "मय उञो वो वा",
    samagra_slp1          = "padasya mayaH uYaH vaH vA aci",
    samagra_dev           = "पदस्य मयः उञः वः वा अचि",
    padaccheda_dev        = "मयः उञो वः वा",
    why_dev               = "(सूत्रम् 8.3.33) मय उञो वो वा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
