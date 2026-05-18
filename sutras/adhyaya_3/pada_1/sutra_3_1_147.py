"""
3.1.147  ण्युट् च  —  VIDHI

Padaccheda: ण्युट् च

Krt suffix rule from dhatu: ण्युट् च (147)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_147_Ryuw_147"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_147_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.147"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.147",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ryuw ca",
    text_dev              = "ण्युट् च",
    padaccheda_dev        = "ण्युट् च",
    why_dev               = "धातोः [ण्युट् च]-प्रत्ययः विहितः (३.१.147)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
