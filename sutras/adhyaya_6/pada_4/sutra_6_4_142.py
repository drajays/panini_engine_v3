"""
6.4.142  ति विंशतेर्डिति  —  VIDHI

Padaccheda: ति (लुप्तषष्ठ्यन्तनिर्देशः) विंशतेः डिति

ति विंशतेर्डिति (6.4.142)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_142_ti_142"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.142", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.142"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.142",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ti viMSaterqiti",
    text_dev              = "ति विंशतेर्डिति",
    padaccheda_dev        = "ति (लुप्तषष्ठ्यन्तनिर्देशः) विंशतेः डिति",
    why_dev               = "(सूत्रम् 6.4.142) ति विंशतेर्डिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
