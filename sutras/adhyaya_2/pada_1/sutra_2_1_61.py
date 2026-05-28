"""
2.1.61  सन्महत्परमोत्तमोत्कृष्टाः पूज्यमानैः  —  VIDHI

Padaccheda: सत्-महत्-परम-उत्तम-उत्कृष्टाः पूज्यमानैः

sat, mahat, parama, uttama, utkrsta with pujyamana form karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_61_sat_mahat_pujya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sanmahatparamottamotkfzwAH pUjyamAnEH",
    text_dev              = "सन्महत्परमोत्तमोत्कृष्टाः पूज्यमानैः",
    padaccheda_dev        = "सत्-महत्-परम-उत्तम-उत्कृष्टाः पूज्यमानैः",
    why_dev               = "सत्-महत्-परम-उत्तम-उत्कृष्टाः पूज्यमानैः सह कर्मधारयः (२.१.६१)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
