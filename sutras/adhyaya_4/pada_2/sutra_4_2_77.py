"""
4.2.77  सुवास्त्वादिभ्योऽण्  —  VIDHI

Padaccheda: सुवास्तु-आदिभ्यः अण्

सुवास्त्वादिभ्योऽण् (4.2.77)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_77_suvAstvAdi_77"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_77_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suvAstvAdiByo'R",
    text_dev              = "सुवास्त्वादिभ्योऽण्",
    padaccheda_dev        = "सुवास्तु-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 4.2.77) सुवास्त्वादिभ्योऽण्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
