"""
3.2.68  अदोऽनन्ने  —  VIDHI

Padaccheda: अदः अनन्ने

krt-suffix rule: अदोऽनन्ने (68)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_68_adonanne_68"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_68_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ado'nanne",
    text_dev              = "अदोऽनन्ने",
    padaccheda_dev        = "अदः अनन्ने",
    why_dev               = "धातोः कृत्-प्रत्ययः [अदोऽनन्ने] विहितः (३.२.68)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
