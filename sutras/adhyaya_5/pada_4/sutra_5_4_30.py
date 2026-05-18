"""
5.4.30  लोहितान्मणौ  —  VIDHI

Padaccheda: लोहितात् मणौ

लोहितान्मणौ (5.4.30)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_30_lohitAnmaR_30"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_30_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lohitAnmaRO",
    text_dev              = "लोहितान्मणौ",
    padaccheda_dev        = "लोहितात् मणौ",
    why_dev               = "(सूत्रम् 5.4.30) लोहितान्मणौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
