"""
2.1.39  स्तोकान्तिकदूरार्थकृच्छ्राणि क्तेन  —  VIDHI

Padaccheda: स्तोक-अन्तिक-दूर-अर्थ-कृच्छ्राणि क्तेन

stoka, antika, dura, krcchra with kta form tatpurusha compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_39_stoka_ktena"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stokAntikadUrArTakfcCrARi ktena",
    text_dev              = "स्तोकान्तिकदूरार्थकृच्छ्राणि क्तेन",
    padaccheda_dev        = "स्तोक-अन्तिक-दूर-अर्थ-कृच्छ्राणि क्तेन",
    why_dev               = "स्तोक-अन्तिक-आदिषु क्तान्तेन सह तत्पुरुषः (२.१.३९)।",
    anuvritti_from        = ('2.1.22',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
