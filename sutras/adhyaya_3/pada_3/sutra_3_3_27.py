"""
3.3.27  प्रे द्रुस्तुस्रुवः  —  VIDHI

Padaccheda: प्रे द्रु-स्तु-स्रुवः

krt-suffix rule: प्रे द्रुस्तुस्रुवः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_27_pre_27"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.27", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pre drustusruvaH",
    text_dev              = "प्रे द्रुस्तुस्रुवः",
    padaccheda_dev        = "प्रे द्रु-स्तु-स्रुवः",
    why_dev               = "धातोः प्रत्ययः (३.3.27)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
