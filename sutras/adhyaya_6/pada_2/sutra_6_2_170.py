"""
6.2.170  जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः  —  VIDHI

Padaccheda: जाति-काल-सुख-आदिभ्यः अनाच्छादनात् क्तः अ-कृत-मित-प्रतिपन्नाः

जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः (6.2.170)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_170_jAtikAlasu_170"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.170"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.170",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAtikAlasuKAdiByo'nAcCAdanAt kto'kftamitapratipannAH",
    text_dev              = "जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः",
    padaccheda_dev        = "जाति-काल-सुख-आदिभ्यः अनाच्छादनात् क्तः अ-कृत-मित-प्रतिपन्नाः",
    why_dev               = "(सूत्रम् 6.2.170) जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
