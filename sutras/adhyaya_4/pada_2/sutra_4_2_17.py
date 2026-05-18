"""
4.2.17  शूलोखाद्यत्  —  VIDHI

Padaccheda: शूल-उखात् यत्

शूलोखाद्यत् (4.2.17)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_17_SUloKAdyat_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_17_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SUloKAdyat",
    text_dev              = "शूलोखाद्यत्",
    padaccheda_dev        = "शूल-उखात् यत्",
    why_dev               = "(सूत्रम् 4.2.17) शूलोखाद्यत्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
