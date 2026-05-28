"""
3.3.153  कामप्रवेदनेऽकच्चिति  —  VIDHI

Padaccheda: काम-प्रवेदने अ-कच्चिति

krt-suffix rule: कामप्रवेदनेऽकच्चिति
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_153_kAmapraved_153"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.153"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.153",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAmapravedane'kacciti",
    text_dev              = "कामप्रवेदनेऽकच्चिति",
    padaccheda_dev        = "काम-प्रवेदने अ-कच्चिति",
    why_dev               = "धातोः प्रत्ययः (३.3.153)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
