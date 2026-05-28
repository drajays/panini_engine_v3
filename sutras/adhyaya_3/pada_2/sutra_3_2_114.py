"""
3.2.114  विभाषा साकाङ्क्षे  —  VIDHI

Padaccheda: विभाषा साकाङ्क्षे

krt-suffix rule: विभाषा साकाङ्क्षे (114)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_114_viBAzA_114"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.114"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA sAkANkze",
    text_dev              = "विभाषा साकाङ्क्षे",
    padaccheda_dev        = "विभाषा साकाङ्क्षे",
    why_dev               = "धातोः कृत्-प्रत्ययः [विभाषा साकाङ्क्षे] विहितः (३.२.114)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
