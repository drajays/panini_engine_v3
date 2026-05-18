"""
5.1.96  तत्र च दीयते कार्यं भववत्  —  VIDHI

Padaccheda: तत्र च दीयते (क्रियापदम्) कार्यम् भव-वत्

तत्र च दीयते कार्यं भववत् (5.1.96)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_96_tatra_96"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_96_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatra ca dIyate kAryaM Bavavat",
    text_dev              = "तत्र च दीयते कार्यं भववत्",
    padaccheda_dev        = "तत्र च दीयते (क्रियापदम्) कार्यम् भव-वत्",
    why_dev               = "(सूत्रम् 5.1.96) तत्र च दीयते कार्यं भववत्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
