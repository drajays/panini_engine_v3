"""
3.2.55  पाणिघताडघौ शिल्पिनि  —  VIDHI

Padaccheda: पाणिघ-ताडघौ शिल्पिनि

krt-suffix rule: पाणिघताडघौ शिल्पिनि (55)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_55_pARiGatAqa_55"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.55", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pARiGatAqaGO Silpini",
    text_dev              = "पाणिघताडघौ शिल्पिनि",
    padaccheda_dev        = "पाणिघ-ताडघौ शिल्पिनि",
    why_dev               = "धातोः कृत्-प्रत्ययः [पाणिघताडघौ शिल्पिनि] विहितः (३.२.55)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
