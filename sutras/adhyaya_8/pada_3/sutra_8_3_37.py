"""
8.3.37  कुप्वोः ≍क≍पौ च  —  VIDHI

Padaccheda: कुप्वोः । XकXपौ । च

कुप्वोः XकXपौ च (8.3.37)
Pāṭha: ashtadhyayi.com data.txt row i=83037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_37_kupvoH_37"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.37", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'kupvoH kapO ca',
    text_dev              = 'कुप्वोः ≍क≍पौ च',
    samagra_slp1          = "visarjanIyasya kupvoH kapO visarjanIyaH ca",
    samagra_dev           = "विसर्जनीयस्य कुप्वोः ≍क≍पौ विसर्जनीयः च",
    padaccheda_dev        = "कुप्वोः । XकXपौ । च",
    why_dev               = "(सूत्रम् 8.3.37) कुप्वोः XकXपौ च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
