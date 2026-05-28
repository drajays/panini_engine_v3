"""
6.1.196  थलि च सेटीडन्तो वा  —  VIDHI

Padaccheda: थलि च सेटि इट् अन्तः वा

थलि च सेटीडन्तो वा (6.1.196)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_196_Tali_196"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_196_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.196"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.196",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Tali ca sewIqanto vA",
    text_dev              = "थलि च सेटीडन्तो वा",
    padaccheda_dev        = "थलि च सेटि इट् अन्तः वा",
    why_dev               = "(सूत्रम् 6.1.196) थलि च सेटीडन्तो वा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
