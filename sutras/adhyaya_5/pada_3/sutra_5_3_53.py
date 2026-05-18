"""
5.3.53  भूतपूर्वे चरट्  —  VIDHI

Padaccheda: भूतपूर्वे चरट्

भूतपूर्वे चरट् (5.3.53)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_53_BUtapUrve_53"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BUtapUrve caraw",
    text_dev              = "भूतपूर्वे चरट्",
    padaccheda_dev        = "भूतपूर्वे चरट्",
    why_dev               = "(सूत्रम् 5.3.53) भूतपूर्वे चरट्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
