"""
3.2.6  प्रे दाज्ञः  —  VIDHI

Padaccheda: प्रे दा-ज्ञः

krt-suffix rule: प्रे दाज्ञः (6)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_6_pre_6"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pre dAjYaH",
    text_dev              = "प्रे दाज्ञः",
    padaccheda_dev        = "प्रे दा-ज्ञः",
    why_dev               = "धातोः कृत्-प्रत्ययः [प्रे दाज्ञः] विहितः (३.२.6)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
