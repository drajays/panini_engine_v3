"""
3.2.89  सुकर्मपापमन्त्रपुण्येषु कृञः  —  VIDHI

Padaccheda: सु-कर्म-पाप-मन्त्र-पुण्येषु कृञः

krt-suffix rule: सुकर्मपापमन्त्रपुण्येषु कृञः (89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_89_sukarmapAp_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_89_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sukarmapApamantrapuRyezu kfYaH",
    text_dev              = "सुकर्मपापमन्त्रपुण्येषु कृञः",
    padaccheda_dev        = "सु-कर्म-पाप-मन्त्र-पुण्येषु कृञः",
    why_dev               = "धातोः कृत्-प्रत्ययः [सुकर्मपापमन्त्रपुण्येषु कृञः] विहितः (३.२.89)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
