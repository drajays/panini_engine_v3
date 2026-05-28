"""
2.3.58  दिवस्तदर्थस्य  —  VIDHI

Padaccheda: दिवः तदर्थस्य

div in its own meaning takes sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_58_divas_tadartha"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_58_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.58"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.58",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "divastadarTasya",
    text_dev              = "दिवस्तदर्थस्य",
    padaccheda_dev        = "दिवः तदर्थस्य",
    why_dev               = "दिवः तदर्थस्य (२.३.५८)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
