"""
7.2.76  रुदादिभ्यः सार्वधातुके  —  VIDHI

Padaccheda: रुद-आदिभ्यः सार्वधातुके

रुदादिभ्यः सार्वधातुके (7.2.76)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_76_rudAdiByaH_76"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.76", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_2_76_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rudAdiByaH sArvaDAtuke",
    text_dev              = "रुदादिभ्यः सार्वधातुके",
    padaccheda_dev        = "रुद-आदिभ्यः सार्वधातुके",
    why_dev               = "(सूत्रम् 7.2.76) रुदादिभ्यः सार्वधातुके।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
