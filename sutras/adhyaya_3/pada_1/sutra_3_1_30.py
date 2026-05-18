"""
3.1.30  कमेर्णिङ्  —  VIDHI

Padaccheda: कमेः णिङ्

Krt suffix rule from dhatu: कमेर्णिङ् (30)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_30_kamerRiN_30"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_30_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kamerRiN",
    text_dev              = "कमेर्णिङ्",
    padaccheda_dev        = "कमेः णिङ्",
    why_dev               = "धातोः [कमेर्णिङ्]-प्रत्ययः विहितः (३.१.30)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
