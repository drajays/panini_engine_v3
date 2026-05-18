"""
6.1.170  अञ्चेश्छन्दस्यसर्वनामस्थानम्  —  VIDHI

Padaccheda: अञ्चेः छन्दसि अ-सर्वनामस्थानम्

अञ्चेश्छन्दस्यसर्वनामस्थानम् (6.1.170)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_170_aYceSCanda_170"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_170_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.170"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.170",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aYceSCandasyasarvanAmasTAnam",
    text_dev              = "अञ्चेश्छन्दस्यसर्वनामस्थानम्",
    padaccheda_dev        = "अञ्चेः छन्दसि अ-सर्वनामस्थानम्",
    why_dev               = "(सूत्रम् 6.1.170) अञ्चेश्छन्दस्यसर्वनामस्थानम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
