"""
2.3.72  तुल्यार्थैरतुलोपमाभ्यां तृतीयाऽन्यतरस्याम्  —  VIDHI

Padaccheda: तुल्य-अर्थे अतुल-उपमाभ्याम् तृतीया अन्यतरस्याम्

Optionally tritiya with tulya-artha and atula, upama words.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_72_tulya_atula"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_72_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tulyArTEratulopamAByAM tftIyA'nyatarasyAm",
    text_dev              = "तुल्यार्थैरतुलोपमाभ्यां तृतीयाऽन्यतरस्याम्",
    padaccheda_dev        = "तुल्य-अर्थे अतुल-उपमाभ्याम् तृतीया अन्यतरस्याम्",
    why_dev               = "तृतीया च तुल्य-अर्थे अतुल-उपमाभ्याम् अन्यतरस्याम् (२.३.७२)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
