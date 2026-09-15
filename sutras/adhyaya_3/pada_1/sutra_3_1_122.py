"""
3.1.122  अमावस्यदन्यतरस्याम्  —  VIDHI

Padaccheda: अमावस्यत् अन्यतरस्याम्

Krt suffix rule from dhatu: अमावस्यदन्यतरस्याम् (122)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_122_amAvasyadany_122"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.122", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "amAvasyadanyatarasyAm",
    text_dev              = "अमावस्यदन्यतरस्याम्",
    padaccheda_dev        = "अमावस्यत् अन्यतरस्याम्",
    why_dev               = "धातोः [अमावस्यदन्यतरस्याम्]-प्रत्ययः विहितः (३.१.122)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
