"""
3.1.14  कष्टाय क्रमणे  —  VIDHI

Padaccheda: कष्टाय क्रमणे

Krt suffix rule from dhatu: कष्टाय क्रमणे (14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_14_kazwAya_14"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.14", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kazwAya kramaRe",
    text_dev              = "कष्टाय क्रमणे",
    padaccheda_dev        = "कष्टाय क्रमणे",
    why_dev               = "धातोः [कष्टाय क्रमणे]-प्रत्ययः विहितः (३.१.14)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
