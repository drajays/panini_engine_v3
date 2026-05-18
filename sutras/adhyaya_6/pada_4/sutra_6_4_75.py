"""
6.4.75  बहुलं छन्दस्यमाङ्योगेऽपि  —  VIDHI

Padaccheda: बहुलम् छन्दसि अ-माङ्-योगे अपि

बहुलं छन्दस्यमाङ्योगेऽपि (6.4.75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_75_bahulaM_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_75_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahulaM CandasyamANyoge'pi",
    text_dev              = "बहुलं छन्दस्यमाङ्योगेऽपि",
    padaccheda_dev        = "बहुलम् छन्दसि अ-माङ्-योगे अपि",
    why_dev               = "(सूत्रम् 6.4.75) बहुलं छन्दस्यमाङ्योगेऽपि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
