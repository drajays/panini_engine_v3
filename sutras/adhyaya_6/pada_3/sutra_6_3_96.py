"""
6.3.96  सध मादस्थयोश्छन्दसि  —  VIDHI

Padaccheda: सध (लुप्तप्रथमान्तनिर्देशः) माद-स्थयोः छन्दसि

सध मादस्थयोश्छन्दसि (6.3.96)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_96_saDa_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_96_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saDa mAdasTayoSCandasi",
    text_dev              = "सध मादस्थयोश्छन्दसि",
    padaccheda_dev        = "सध (लुप्तप्रथमान्तनिर्देशः) माद-स्थयोः छन्दसि",
    why_dev               = "(सूत्रम् 6.3.96) सध मादस्थयोश्छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
