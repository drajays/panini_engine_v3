"""
3.1.20  पुच्छभाण्डचीवराण्णिङ्  —  VIDHI

Padaccheda: पुच्छ-भाण्ड-चीवरात् णिङ्

Krt suffix rule from dhatu: पुच्छभाण्डचीवराण्णिङ् (20)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_20_pucCaBARqacI_20"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.20", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.20"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.20",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pucCaBARqacIvarARRiN",
    text_dev              = "पुच्छभाण्डचीवराण्णिङ्",
    padaccheda_dev        = "पुच्छ-भाण्ड-चीवरात् णिङ्",
    why_dev               = "धातोः [पुच्छभाण्डचीवराण्णिङ्]-प्रत्ययः विहितः (३.१.20)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
