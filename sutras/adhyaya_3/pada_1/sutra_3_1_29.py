"""
3.1.29  ऋतेरीयङ्  —  VIDHI

Padaccheda: ऋतेः ईयङ्

Krt suffix rule from dhatu: ऋतेरीयङ् (29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_29_fterIyaN_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fterIyaN",
    text_dev              = "ऋतेरीयङ्",
    padaccheda_dev        = "ऋतेः ईयङ्",
    why_dev               = "धातोः [ऋतेरीयङ्]-प्रत्ययः विहितः (३.१.29)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
