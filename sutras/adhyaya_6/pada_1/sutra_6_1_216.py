"""
6.1.216  त्यागरागहासकुहश्वठक्रथानाम्  —  VIDHI

Padaccheda: त्याग-राग-हास-कुह-श्वठ-क्रथानाम्

त्यागरागहासकुहश्वठक्रथानाम् (6.1.216)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_216_tyAgarAgah_216"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.216", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.216"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.216",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tyAgarAgahAsakuhaSvaWakraTAnAm",
    text_dev              = "त्यागरागहासकुहश्वठक्रथानाम्",
    padaccheda_dev        = "त्याग-राग-हास-कुह-श्वठ-क्रथानाम्",
    why_dev               = "(सूत्रम् 6.1.216) त्यागरागहासकुहश्वठक्रथानाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
