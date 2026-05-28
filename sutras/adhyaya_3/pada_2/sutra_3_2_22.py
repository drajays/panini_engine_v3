"""
3.2.22  कर्मणि भृतौ  —  VIDHI

Padaccheda: कर्मणि भृतौ

krt-suffix rule: कर्मणि भृतौ (22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_22_karmaRi_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_22_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRi BftO",
    text_dev              = "कर्मणि भृतौ",
    padaccheda_dev        = "कर्मणि भृतौ",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्मणि भृतौ] विहितः (३.२.22)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
