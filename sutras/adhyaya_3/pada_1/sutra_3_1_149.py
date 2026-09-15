"""
3.1.149  प्रुसृल्वः समभिहारे वुन्  —  VIDHI

Padaccheda: प्रु-सृल्वः ( अत्र पञ्चम्याः स्थाने जस्) समभिहारे वुन्

Krt suffix rule from dhatu: प्रुसृल्वः समभिहारे वुन् (149)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_149_prusflvaH_149"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.149", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.149"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.149",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prusflvaH samaBihAre vun",
    text_dev              = "प्रुसृल्वः समभिहारे वुन्",
    padaccheda_dev        = "प्रु-सृल्वः ( अत्र पञ्चम्याः स्थाने जस्) समभिहारे वुन्",
    why_dev               = "धातोः [प्रुसृल्वः समभिहारे वुन्]-प्रत्ययः विहितः (३.१.149)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
