"""
3.2.122  पुरि लुङ् चास्मे  —  VIDHI

Padaccheda: पुरि लुङ् च अस्मे

krt-suffix rule: पुरि लुङ् चास्मे (122)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_122_puri_122"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.122", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puri luN cAsme",
    text_dev              = "पुरि लुङ् चास्मे",
    padaccheda_dev        = "पुरि लुङ् च अस्मे",
    why_dev               = "धातोः कृत्-प्रत्ययः [पुरि लुङ् चास्मे] विहितः (३.२.122)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
