"""
3.3.60  नौ ण च  —  VIDHI

Padaccheda: नौ ण (लुप्तप्रथमान्तनिर्देशः) च

krt-suffix rule: नौ ण च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_60_nO_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nO Ra ca",
    text_dev              = "नौ ण च",
    padaccheda_dev        = "नौ ण (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः प्रत्ययः (३.3.60)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
