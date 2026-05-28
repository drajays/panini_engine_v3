"""
6.1.209  जुष्टार्पिते च छन्दसि  —  VIDHI

Padaccheda: जुष्ट-अर्पिते च छन्दसि

जुष्टार्पिते च छन्दसि (6.1.209)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_209_juzwArpite_209"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.209"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.209",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "juzwArpite ca Candasi",
    text_dev              = "जुष्टार्पिते च छन्दसि",
    padaccheda_dev        = "जुष्ट-अर्पिते च छन्दसि",
    why_dev               = "(सूत्रम् 6.1.209) जुष्टार्पिते च छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
