"""
2.3.65  कर्तृकर्मणोः कृति  —  VIDHI

Padaccheda: कर्तृ-कर्मणोः कृति

For krt-suffix forms, kartri and karma take sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_65_kartru_karmana_krti"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_65_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kartfkarmaRoH kfti",
    text_dev              = "कर्तृकर्मणोः कृति",
    padaccheda_dev        = "कर्तृ-कर्मणोः कृति",
    why_dev               = "कर्तृ-कर्मणोः कृति (२.३.६५)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
