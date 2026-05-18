"""
3.3.25  वौ क्षुश्रुवः  —  VIDHI

Padaccheda: वौ क्षु-श्रुवः

krt-suffix rule: वौ क्षुश्रुवः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_25_vO_25"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_25_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vO kzuSruvaH",
    text_dev              = "वौ क्षुश्रुवः",
    padaccheda_dev        = "वौ क्षु-श्रुवः",
    why_dev               = "धातोः प्रत्ययः (३.3.25)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
