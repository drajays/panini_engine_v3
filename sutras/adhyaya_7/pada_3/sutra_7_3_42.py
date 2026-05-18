"""
7.3.42  शदेरगतौ तः  —  VIDHI

Padaccheda: शदेः अगतौ तः

शदेरगतौ तः (7.3.42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_42_SaderagatO_42"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_42_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SaderagatO taH",
    text_dev              = "शदेरगतौ तः",
    padaccheda_dev        = "शदेः अगतौ तः",
    why_dev               = "(सूत्रम् 7.3.42) शदेरगतौ तः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
