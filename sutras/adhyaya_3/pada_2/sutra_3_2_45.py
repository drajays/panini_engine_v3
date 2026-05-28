"""
3.2.45  आशिते भुवः करणभावयोः  —  VIDHI

Padaccheda: आशिते भुवः करण-भावयोः

krt-suffix rule: आशिते भुवः करणभावयोः (45)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_45_ASite_45"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_45_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ASite BuvaH karaRaBAvayoH",
    text_dev              = "आशिते भुवः करणभावयोः",
    padaccheda_dev        = "आशिते भुवः करण-भावयोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [आशिते भुवः करणभावयोः] विहितः (३.२.45)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
