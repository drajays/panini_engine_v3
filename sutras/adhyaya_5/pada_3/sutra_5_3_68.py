"""
5.3.68  विभाषा सुपो बहुच् पुरस्तात्तु  —  VIDHI

Padaccheda: विभाषा सुपः बहुच् पुरस्तात् तु

विभाषा सुपो बहुच् पुरस्तात्तु (5.3.68)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_68_viBAzA_68"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_68_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA supo bahuc purastAttu",
    text_dev              = "विभाषा सुपो बहुच् पुरस्तात्तु",
    padaccheda_dev        = "विभाषा सुपः बहुच् पुरस्तात् तु",
    why_dev               = "(सूत्रम् 5.3.68) विभाषा सुपो बहुच् पुरस्तात्तु।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
