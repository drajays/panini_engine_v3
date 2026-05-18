"""
8.3.64  स्थाऽऽदिष्वभ्यासेन चाभ्यासय  —  VIDHI

Padaccheda: स्था-आदिषु अभ्यासेन च अभ्यासस्य

स्थाऽऽदिष्वभ्यासेन चाभ्यासय (8.3.64)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_64_sTAdizva_64"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_64_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTA''dizvaByAsena cAByAsaya",
    text_dev              = "स्थाऽऽदिष्वभ्यासेन चाभ्यासय",
    padaccheda_dev        = "स्था-आदिषु अभ्यासेन च अभ्यासस्य",
    why_dev               = "(सूत्रम् 8.3.64) स्थाऽऽदिष्वभ्यासेन चाभ्यासय।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
