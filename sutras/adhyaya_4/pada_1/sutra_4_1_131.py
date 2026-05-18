"""
4.1.131  क्षुद्राभ्यो वा  —  VIDHI

Padaccheda: क्षुद्राभ्यः वा

क्षुद्राभ्यो वा (4.1.131)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_131_kzudrAByo_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_131_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzudrAByo vA",
    text_dev              = "क्षुद्राभ्यो वा",
    padaccheda_dev        = "क्षुद्राभ्यः वा",
    why_dev               = "(सूत्रम् 4.1.131) क्षुद्राभ्यो वा।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
