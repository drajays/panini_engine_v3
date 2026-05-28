"""
4.4.66  तदस्मै दीयते नियुक्तम्  —  VIDHI

Padaccheda: तत् अस्मै दीयते (क्रियापदम्) नियुक्तम्

तदस्मै दीयते नियुक्तम् (4.4.66)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_66_tadasmE_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.66", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasmE dIyate niyuktam",
    text_dev              = "तदस्मै दीयते नियुक्तम्",
    padaccheda_dev        = "तत् अस्मै दीयते (क्रियापदम्) नियुक्तम्",
    why_dev               = "(सूत्रम् 4.4.66) तदस्मै दीयते नियुक्तम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
