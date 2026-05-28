"""
5.1.88  वर्षाल्लुक् च  —  VIDHI

Padaccheda: वर्षात् लुक् च

वर्षाल्लुक् च (5.1.88)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_88_varzAlluk_88"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.88", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varzAlluk ca",
    text_dev              = "वर्षाल्लुक् च",
    padaccheda_dev        = "वर्षात् लुक् च",
    why_dev               = "(सूत्रम् 5.1.88) वर्षाल्लुक् च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
