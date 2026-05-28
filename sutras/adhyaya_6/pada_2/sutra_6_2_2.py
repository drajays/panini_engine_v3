"""
6.2.2  तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः  —  VIDHI

Padaccheda: तत्पुरुषे तुल्य-अर्थ-तृतीया-सप्तमी-उपमान-अव्यय-द्वितीया-कृत्याः

तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः (6.2.2)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_2_tatpuruze_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatpuruze tulyArTatftIyAsaptamyupamAnAvyayadvitIyAkftyAH",
    text_dev              = "तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः",
    padaccheda_dev        = "तत्पुरुषे तुल्य-अर्थ-तृतीया-सप्तमी-उपमान-अव्यय-द्वितीया-कृत्याः",
    why_dev               = "(सूत्रम् 6.2.2) तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
