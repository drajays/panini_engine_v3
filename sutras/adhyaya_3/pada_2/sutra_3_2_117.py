"""
3.2.117  प्रश्ने चासन्नकाले  —  VIDHI

Padaccheda: प्रश्ने च आसन्नकाले

krt-suffix rule: प्रश्ने चासन्नकाले (117)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_117_praSne_117"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.117", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praSne cAsannakAle",
    text_dev              = "प्रश्ने चासन्नकाले",
    padaccheda_dev        = "प्रश्ने च आसन्नकाले",
    why_dev               = "धातोः कृत्-प्रत्ययः [प्रश्ने चासन्नकाले] विहितः (३.२.117)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
