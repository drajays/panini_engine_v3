"""
3.1.140  ज्वलितिकसन्तेभ्यो णः  —  VIDHI

Padaccheda: ज्वलिति-कस्-अन्तेभ्यः णः

Krt suffix rule from dhatu: ज्वलितिकसन्तेभ्यो णः (140)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_140_jvalitikasan_140"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.140", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.140"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.140",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jvalitikasanteByo RaH",
    text_dev              = "ज्वलितिकसन्तेभ्यो णः",
    padaccheda_dev        = "ज्वलिति-कस्-अन्तेभ्यः णः",
    why_dev               = "धातोः [ज्वलितिकसन्तेभ्यो णः]-प्रत्ययः विहितः (३.१.140)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
