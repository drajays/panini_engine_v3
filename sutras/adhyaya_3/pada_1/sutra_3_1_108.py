"""
3.1.108  हनस्त च  —  VIDHI

Padaccheda: हनः त (लुप्तप्रथमान्तनिर्देशः) च

Krt suffix rule from dhatu: हनस्त च (108)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_108_hanasta_108"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_108_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.108"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.108",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hanasta ca",
    text_dev              = "हनस्त च",
    padaccheda_dev        = "हनः त (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः [हनस्त च]-प्रत्ययः विहितः (३.१.108)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
