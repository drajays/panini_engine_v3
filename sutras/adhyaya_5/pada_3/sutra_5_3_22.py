"""
5.3.22  सद्यःपरुत्परार्यैषमःपरेद्यव्यद्यपूर्वेद्युरन्येद्युरन्यतरेद्युरितरेद्युरपरेद्युरधरेद्युरुभयेद्युरुत्तरेद्युः  —  VIDHI

Padaccheda: सद्यः परुत् परारी ऐषमः परेद्यवि अद्य पूर्वेद्युः अन्येद्युः अन्यतरेद्युः इतरेद्युः अपरेद्युः अधरेद्युः उभयेद्युः उत्तरेद्युः

सद्यःपरुत्परार्यैषमःपरेद्यव्यद्यपूर्वेद्युरन्येद्युरन्यतरेद्युरितरेद्युरपरेद्युरधरेद्युरुभयेद्युरुत्तरेद्युः (5.3.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_22_sadyaHparu_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sadyaHparutparAryEzamaHparedyavyadyapUrvedyuranyedyuranyataredyuritaredyuraparedyuraDaredyuruBayedyuruttaredyuH",
    text_dev              = "सद्यःपरुत्परार्यैषमःपरेद्यव्यद्यपूर्वेद्युरन्येद्युरन्यतरेद्युरितरेद्युरपरेद्युरधरेद्युरुभयेद्युरुत्तरेद्युः",
    padaccheda_dev        = "सद्यः परुत् परारी ऐषमः परेद्यवि अद्य पूर्वेद्युः अन्येद्युः अन्यतरेद्युः इतरेद्युः अपरेद्युः अधरेद्युः उभयेद्युः उत्तरेद्युः",
    why_dev               = "(सूत्रम् 5.3.22) सद्यःपरुत्परार्यैषमःपरेद्यव्यद्यपूर्वेद्युरन्येद्युरन्यतरेद्युरितरेद्युरपरेद्युरधरेद्युरुभयेद्युरुत्तरेद्युः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
