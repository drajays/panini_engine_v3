"""
8.1.64  वैवावेति च च्छन्दसि  —  VIDHI

Padaccheda: वै-वाव (लुप्तप्रथमान्तनिर्देशः) इति च छन्दसि

वैवावेति च च्छन्दसि (8.1.64)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_64_vEvAveti_64"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vEvAveti ca cCandasi",
    text_dev              = "वैवावेति च च्छन्दसि",
    padaccheda_dev        = "वै-वाव (लुप्तप्रथमान्तनिर्देशः) इति च छन्दसि",
    why_dev               = "(सूत्रम् 8.1.64) वैवावेति च च्छन्दसि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
