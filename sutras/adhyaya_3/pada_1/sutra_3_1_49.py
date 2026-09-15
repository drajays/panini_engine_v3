"""
3.1.49  विभाषा धेट्श्व्योः  —  VIDHI

Padaccheda: विभाषा धेट्-श्व्योः

Krt suffix rule from dhatu: विभाषा धेट्श्व्योः (49)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_49_viBAzA_49"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.49", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA DewSvyoH",
    text_dev              = "विभाषा धेट्श्व्योः",
    padaccheda_dev        = "विभाषा धेट्-श्व्योः",
    why_dev               = "धातोः [विभाषा धेट्श्व्योः]-प्रत्ययः विहितः (३.१.49)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
