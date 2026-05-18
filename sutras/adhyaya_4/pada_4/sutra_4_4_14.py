"""
4.4.14  आयुधाच्छ च  —  VIDHI

Padaccheda: आयुधात् छ (लुप्तप्रथमान्तनिर्देशः) च

आयुधाच्छ च (4.4.14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_14_AyuDAcCa_14"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_14_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AyuDAcCa ca",
    text_dev              = "आयुधाच्छ च",
    padaccheda_dev        = "आयुधात् छ (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 4.4.14) आयुधाच्छ च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
