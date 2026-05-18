"""
6.1.141  हिंसायां प्रतेश्च  —  VIDHI

Padaccheda: हिंसायाम् प्रतेः च

हिंसायां प्रतेश्च (6.1.141)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_141_hiMsAyAM_141"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_141_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.141"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.141",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hiMsAyAM prateSca",
    text_dev              = "हिंसायां प्रतेश्च",
    padaccheda_dev        = "हिंसायाम् प्रतेः च",
    why_dev               = "(सूत्रम् 6.1.141) हिंसायां प्रतेश्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
