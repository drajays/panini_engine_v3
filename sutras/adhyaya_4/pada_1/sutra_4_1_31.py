"""
4.1.31  रात्रेश्चाजसौ  —  VIDHI

Padaccheda: रात्रेः च अ-जसौ

रात्रेश्चाजसौ (4.1.31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_31_rAtreScAja_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAtreScAjasO",
    text_dev              = "रात्रेश्चाजसौ",
    padaccheda_dev        = "रात्रेः च अ-जसौ",
    why_dev               = "(सूत्रम् 4.1.31) रात्रेश्चाजसौ।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
