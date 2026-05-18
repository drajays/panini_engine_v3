"""
4.2.12  द्वैपवैयाघ्रादञ्  —  VIDHI

Padaccheda: द्वैप-वैयाघ्रात् अञ्

द्वैपवैयाघ्रादञ् (4.2.12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_12_dvEpavEyAG_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_12_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvEpavEyAGrAdaY",
    text_dev              = "द्वैपवैयाघ्रादञ्",
    padaccheda_dev        = "द्वैप-वैयाघ्रात् अञ्",
    why_dev               = "(सूत्रम् 4.2.12) द्वैपवैयाघ्रादञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
