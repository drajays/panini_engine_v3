"""
3.2.164  गत्वरश्च  —  VIDHI

Padaccheda: गत्वरः च

krt-suffix rule: गत्वरश्च (164)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_164_gatvaraSca_164"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_164_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.164"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.164",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gatvaraSca",
    text_dev              = "गत्वरश्च",
    padaccheda_dev        = "गत्वरः च",
    why_dev               = "धातोः कृत्-प्रत्ययः [गत्वरश्च] विहितः (३.२.164)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
