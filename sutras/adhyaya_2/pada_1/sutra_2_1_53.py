"""
2.1.53  कुत्सितानि कुत्सनैः  —  VIDHI

Padaccheda: कुत्सितानि कुत्सनैः

Despicable things with disparaging words form karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_53_kutsita_kutsana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kutsitAni kutsanEH",
    text_dev              = "कुत्सितानि कुत्सनैः",
    padaccheda_dev        = "कुत्सितानि कुत्सनैः",
    why_dev               = "कुत्सितानां कुत्सनैः सह कर्मधारयः (२.१.५३)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
