"""
3.2.73  विजुपे छन्दसि  —  VIDHI

Padaccheda: विच् उपे छन्दसि

krt-suffix rule: विजुपे छन्दसि (73)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_73_vijupe_73"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.73", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vijupe Candasi",
    text_dev              = "विजुपे छन्दसि",
    padaccheda_dev        = "विच् उपे छन्दसि",
    why_dev               = "धातोः कृत्-प्रत्ययः [विजुपे छन्दसि] विहितः (३.२.73)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
