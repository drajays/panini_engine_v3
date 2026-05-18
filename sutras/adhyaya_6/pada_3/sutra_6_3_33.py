"""
6.3.33  पितरामातरा च च्छन्दसि  —  VIDHI

Padaccheda: पितरामातरा च छन्दसि

पितरामातरा च च्छन्दसि (6.3.33)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_33_pitarAmAta_33"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_33_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pitarAmAtarA ca cCandasi",
    text_dev              = "पितरामातरा च च्छन्दसि",
    padaccheda_dev        = "पितरामातरा च छन्दसि",
    why_dev               = "(सूत्रम् 6.3.33) पितरामातरा च च्छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
