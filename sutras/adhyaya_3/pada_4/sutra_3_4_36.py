"""
3.4.36  समूलाकृतजीवेषु हन्कृञ्ग्रहः  —  VIDHI

Padaccheda: समूल-अकृत-जीवेषु हन्-कृञ्-ग्रहः

krt-suffix rule: समूलाकृतजीवेषु हन्कृञ्ग्रहः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_36_samUlAkfta_36"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.36", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samUlAkftajIvezu hankfYgrahaH",
    text_dev              = "समूलाकृतजीवेषु हन्कृञ्ग्रहः",
    padaccheda_dev        = "समूल-अकृत-जीवेषु हन्-कृञ्-ग्रहः",
    why_dev               = "धातोः प्रत्ययः (३.4.36)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
