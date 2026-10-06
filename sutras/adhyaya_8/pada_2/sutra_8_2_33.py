"""
8.2.33  वा द्रुहमुहष्णुहष्णिहाम्  —  VIDHI

Padaccheda: वा द्रुह-मुह-ष्णुह-ष्णिहाम्

वा द्रुहमुहष्णुहष्णिहाम् (8.2.33)
Pāṭha: ashtadhyayi.com data.txt row i=82033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_33_vA_33"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.33", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA druhamuhazRuhazRihAm",
    text_dev              = "वा द्रुहमुहष्णुहष्णिहाम्",
    samagra_slp1          = "druha-muha-zRuha-zRihAm DAtoH haH padasya ante Jali GaH vA",
    samagra_dev           = "द्रुह-मुह-ष्णुह-ष्णिहाम् धातोः हः पदस्य अन्ते झलि घः वा",
    padaccheda_dev        = "वा द्रुह-मुह-ष्णुह-ष्णिहाम्",
    why_dev               = "(सूत्रम् 8.2.33) वा द्रुहमुहष्णुहष्णिहाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
