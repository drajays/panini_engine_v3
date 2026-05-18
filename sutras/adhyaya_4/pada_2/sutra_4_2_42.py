"""
4.2.42  ब्राह्मणमाणववाडवाद्यन्  —  VIDHI

Padaccheda: ब्राह्मण-माणव-वाडवात् यन्

ब्राह्मणमाणववाडवाद्यन् (4.2.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_42_brAhmaRamA_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_42_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "brAhmaRamARavavAqavAdyan",
    text_dev              = "ब्राह्मणमाणववाडवाद्यन्",
    padaccheda_dev        = "ब्राह्मण-माणव-वाडवात् यन्",
    why_dev               = "(सूत्रम् 4.2.42) ब्राह्मणमाणववाडवाद्यन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
