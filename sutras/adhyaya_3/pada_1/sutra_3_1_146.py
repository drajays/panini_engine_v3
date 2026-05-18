"""
3.1.146  गस्थकन्  —  VIDHI

Padaccheda: गः थकन्

Krt suffix rule from dhatu: गस्थकन् (146)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_146_gasTakan_146"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_146_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.146"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.146",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gasTakan",
    text_dev              = "गस्थकन्",
    padaccheda_dev        = "गः थकन्",
    why_dev               = "धातोः [गस्थकन्]-प्रत्ययः विहितः (३.१.146)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
