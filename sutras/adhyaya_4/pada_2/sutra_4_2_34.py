"""
4.2.34  कालेभ्यो भववत्  —  VIDHI

Padaccheda: कालेभ्यः भव-वत्

कालेभ्यो भववत् (4.2.34)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_34_kAleByo_34"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_34_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAleByo Bavavat",
    text_dev              = "कालेभ्यो भववत्",
    padaccheda_dev        = "कालेभ्यः भव-वत्",
    why_dev               = "(सूत्रम् 4.2.34) कालेभ्यो भववत्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
