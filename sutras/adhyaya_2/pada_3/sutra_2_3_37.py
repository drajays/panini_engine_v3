"""
2.3.37  यस्य च भावेन भावलक्षणम्  —  VIDHI

Padaccheda: यस्य च भावेन भाव-लक्षणम्

When the being of one marks the being of another, sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_37_yasya_bhava"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yasya ca BAvena BAvalakzaRam",
    text_dev              = "यस्य च भावेन भावलक्षणम्",
    padaccheda_dev        = "यस्य च भावेन भाव-लक्षणम्",
    why_dev               = "यस्य च भावेन भाव-लक्षणम् (२.३.३७)।",
    anuvritti_from        = ('2.3.36',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
