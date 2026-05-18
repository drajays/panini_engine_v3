"""
4.1.145  व्यन् सपत्ने  —  VIDHI

Padaccheda: व्यन् सपत्ने

व्यन् सपत्ने (4.1.145)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_145_vyan_145"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_145_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.145"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.145",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyan sapatne",
    text_dev              = "व्यन् सपत्ने",
    padaccheda_dev        = "व्यन् सपत्ने",
    why_dev               = "(सूत्रम् 4.1.145) व्यन् सपत्ने।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
