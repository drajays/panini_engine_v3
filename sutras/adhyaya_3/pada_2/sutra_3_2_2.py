"""
3.2.2  ह्वावामश्च  —  VIDHI

Padaccheda: ह्वा-वा-मः च

krt-suffix rule: ह्वावामश्च (2)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_2_hvAvAmaSca_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "hvAvAmaSca",
    text_dev              = "ह्वावामश्च",
    padaccheda_dev        = "ह्वा-वा-मः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [ह्वावामश्च] विहितः (३.२.2)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
