"""
6.1.169  अन्तोदत्तादुत्तरपदादन्यतरस्यामनित्यसमासे  —  VIDHI

Padaccheda: अन्त-उदात्तात् उत्तरपदात् अन्यतरस्याम् अनित्य-समासे

अन्तोदत्तादुत्तरपदादन्यतरस्यामनित्यसमासे (6.1.169)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_169_antodattAd_169"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.169", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.169"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.169",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antodattAduttarapadAdanyatarasyAmanityasamAse",
    text_dev              = "अन्तोदत्तादुत्तरपदादन्यतरस्यामनित्यसमासे",
    padaccheda_dev        = "अन्त-उदात्तात् उत्तरपदात् अन्यतरस्याम् अनित्य-समासे",
    why_dev               = "(सूत्रम् 6.1.169) अन्तोदत्तादुत्तरपदादन्यतरस्यामनित्यसमासे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
