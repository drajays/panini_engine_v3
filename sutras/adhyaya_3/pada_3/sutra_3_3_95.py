"""
3.3.95  स्थागापापचां भावे  —  VIDHI

Padaccheda: स्था-गा-पा-पचः भावे

krt-suffix rule: स्थागापापचां भावे
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_95_sTAgApApac_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTAgApApacAM BAve",
    text_dev              = "स्थागापापचां भावे",
    padaccheda_dev        = "स्था-गा-पा-पचः भावे",
    why_dev               = "धातोः प्रत्ययः (३.3.95)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
