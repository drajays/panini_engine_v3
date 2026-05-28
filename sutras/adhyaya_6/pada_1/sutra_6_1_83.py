"""
6.1.83  भय्यप्रवय्ये च च्छन्दसि  —  VIDHI

Padaccheda: भय्य-प्रवय्ये च छन्दसि

भय्यप्रवय्ये च च्छन्दसि (6.1.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_83_Bayyaprava_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_83_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Bayyapravayye ca cCandasi",
    text_dev              = "भय्यप्रवय्ये च च्छन्दसि",
    padaccheda_dev        = "भय्य-प्रवय्ये च छन्दसि",
    why_dev               = "(सूत्रम् 6.1.83) भय्यप्रवय्ये च च्छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
