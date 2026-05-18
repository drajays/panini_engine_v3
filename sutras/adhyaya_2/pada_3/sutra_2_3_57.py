"""
2.3.57  व्यवहृपणोः समर्थयोः  —  VIDHI

Padaccheda: बवि-अव-हृ-पणोः समर्थयोः

vyava-hr and pan when related take sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_57_vyava_hri_pana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_57_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vyavahfpaRoH samarTayoH",
    text_dev              = "व्यवहृपणोः समर्थयोः",
    padaccheda_dev        = "बवि-अव-हृ-पणोः समर्थयोः",
    why_dev               = "व्यव-हृ-पणोः समर्थयोः षष्ठी (२.३.५७)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
