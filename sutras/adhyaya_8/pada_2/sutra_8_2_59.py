"""
8.2.59  भित्तं शकलम्  —  VIDHI

Padaccheda: भित्तम् शकलम्

भित्तं शकलम् (8.2.59)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_59_BittaM_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_59_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BittaM Sakalam",
    text_dev              = "भित्तं शकलम्",
    padaccheda_dev        = "भित्तम् शकलम्",
    why_dev               = "(सूत्रम् 8.2.59) भित्तं शकलम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
