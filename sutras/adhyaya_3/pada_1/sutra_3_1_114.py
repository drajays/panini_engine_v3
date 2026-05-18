"""
3.1.114  राजसूयसूर्यमृषोद्यरुच्यकुप्यकृष्टपच्याव्यथ्याः  —  VIDHI

Padaccheda: राजसूय-सूर्य-मृषोद्य-रुच्य-कुप्य-कृष्टपच्य-अव्यथ्याः

Krt suffix rule from dhatu: राजसूयसूर्यमृषोद्यरुच्यकुप्यकृष्टपच्याव्यथ्याः (114)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_114_rAjasUyasUry_114"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_114_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.114"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAjasUyasUryamfzodyarucyakupyakfzwapacyAvyaTyAH",
    text_dev              = "राजसूयसूर्यमृषोद्यरुच्यकुप्यकृष्टपच्याव्यथ्याः",
    padaccheda_dev        = "राजसूय-सूर्य-मृषोद्य-रुच्य-कुप्य-कृष्टपच्य-अव्यथ्याः",
    why_dev               = "धातोः [राजसूयसूर्यमृषोद्यरुच्यकुप्यकृष्टपच्याव्यथ्याः]-प्रत्ययः विहितः (३.१.114)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
