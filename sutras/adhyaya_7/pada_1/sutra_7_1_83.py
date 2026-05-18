"""
7.1.83  दृक्स्ववस्स्वतवसां छन्दसि  —  VIDHI

Padaccheda: दृक्-स्ववस्-स्वतवसाम् छन्दसि

दृक्स्ववस्स्वतवसां छन्दसि (7.1.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_1_83_dfksvavass_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_1_83_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dfksvavassvatavasAM Candasi",
    text_dev              = "दृक्स्ववस्स्वतवसां छन्दसि",
    padaccheda_dev        = "दृक्-स्ववस्-स्वतवसाम् छन्दसि",
    why_dev               = "(सूत्रम् 7.1.83) दृक्स्ववस्स्वतवसां छन्दसि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
