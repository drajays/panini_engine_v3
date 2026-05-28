"""
3.3.55  परौ भुवोऽवज्ञाने  —  VIDHI

Padaccheda: परौ भुवः अवज्ञाने

krt-suffix rule: परौ भुवोऽवज्ञाने
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_55_parO_55"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_55_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parO Buvo'vajYAne",
    text_dev              = "परौ भुवोऽवज्ञाने",
    padaccheda_dev        = "परौ भुवः अवज्ञाने",
    why_dev               = "धातोः प्रत्ययः (३.3.55)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
