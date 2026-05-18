"""
4.3.80  गोत्रादङ्कवत्  —  VIDHI

Padaccheda: गोत्रात् अङ्क-वत्

गोत्रादङ्कवत् (4.3.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_80_gotrAdaNka_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_80_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gotrAdaNkavat",
    text_dev              = "गोत्रादङ्कवत्",
    padaccheda_dev        = "गोत्रात् अङ्क-वत्",
    why_dev               = "(सूत्रम् 4.3.80) गोत्रादङ्कवत्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
