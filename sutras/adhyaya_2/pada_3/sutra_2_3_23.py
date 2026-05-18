"""
2.3.23  हेतौ  —  VIDHI

Padaccheda: हेतौ

Tritiya marks the cause (hetu).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_23_hetau_tritiya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_23_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hetO",
    text_dev              = "हेतौ",
    padaccheda_dev        = "हेतौ",
    why_dev               = "हेतौ (२.३.२३)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
