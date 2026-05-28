"""
3.3.54  वृणोतेराच्छादने  —  VIDHI

Padaccheda: वृणोतेः आच्छादने

krt-suffix rule: वृणोतेराच्छादने
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_54_vfRoterAcC_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_54_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vfRoterAcCAdane",
    text_dev              = "वृणोतेराच्छादने",
    padaccheda_dev        = "वृणोतेः आच्छादने",
    why_dev               = "धातोः प्रत्ययः (३.3.54)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
