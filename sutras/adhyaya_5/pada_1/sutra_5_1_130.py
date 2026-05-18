"""
5.1.130  हायनान्तयुवादिभ्योऽण्  —  VIDHI

Padaccheda: हायन-अन्त-युव-आदिभ्यः अण्

हायनान्तयुवादिभ्योऽण् (5.1.130)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_130_hAyanAntay_130"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_130_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.130"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.130",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hAyanAntayuvAdiByo'R",
    text_dev              = "हायनान्तयुवादिभ्योऽण्",
    padaccheda_dev        = "हायन-अन्त-युव-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 5.1.130) हायनान्तयुवादिभ्योऽण्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
