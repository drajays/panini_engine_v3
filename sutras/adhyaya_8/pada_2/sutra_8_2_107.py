"""
8.2.107  एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ  —  VIDHI

Padaccheda: एचः अप्रगृह्यस्य अदूरात् हूते पूर्वस्य अर्धस्य उत्तरस्य इत्-उतौ

एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ (8.2.107)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_107_ecopragfh_107"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_107_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "eco'pragfhyasyAdUrAdDUte pUrvasyArDasyAduttarasyedutO",
    text_dev              = "एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ",
    padaccheda_dev        = "एचः अप्रगृह्यस्य अदूरात् हूते पूर्वस्य अर्धस्य उत्तरस्य इत्-उतौ",
    why_dev               = "(सूत्रम् 8.2.107) एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
