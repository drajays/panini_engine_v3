"""
5.2.46  शदन्तविंशतेश्च  —  VIDHI

Padaccheda: शत्-अन्त-विंशतेः च

शदन्तविंशतेश्च (5.2.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_46_SadantaviM_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.46", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SadantaviMSateSca",
    text_dev              = "शदन्तविंशतेश्च",
    padaccheda_dev        = "शत्-अन्त-विंशतेः च",
    why_dev               = "(सूत्रम् 5.2.46) शदन्तविंशतेश्च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
