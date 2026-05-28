"""
3.2.18  पुरोऽग्रतोऽग्रेषु सर्तेः  —  VIDHI

Padaccheda: पुरः-अग्रतः-अग्रेषु सर्त्तेः

krt-suffix rule: पुरोऽग्रतोऽग्रेषु सर्तेः (18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_18_purograto_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_2_18_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puro'grato'grezu sarteH",
    text_dev              = "पुरोऽग्रतोऽग्रेषु सर्तेः",
    padaccheda_dev        = "पुरः-अग्रतः-अग्रेषु सर्त्तेः",
    why_dev               = "धातोः कृत्-प्रत्ययः [पुरोऽग्रतोऽग्रेषु सर्तेः] विहितः (३.२.18)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
