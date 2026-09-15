"""
3.2.42  सर्वकूलाभ्रकरीषेषु कषः  —  VIDHI

Padaccheda: सर्व-कूल-अभ्र-करीषेषु कषः

krt-suffix rule: सर्वकूलाभ्रकरीषेषु कषः (42)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_42_sarvakUlAB_42"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.42", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.42"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.42",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarvakUlABrakarIzezu kazaH",
    text_dev              = "सर्वकूलाभ्रकरीषेषु कषः",
    padaccheda_dev        = "सर्व-कूल-अभ्र-करीषेषु कषः",
    why_dev               = "धातोः कृत्-प्रत्ययः [सर्वकूलाभ्रकरीषेषु कषः] विहितः (३.२.42)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
