"""
6.3.63  ङ्यापोः संज्ञाछन्दसोर्बहुलम्  —  VIDHI

Padaccheda: ङी-आपोः संज्ञा-छन्दसोः बहुलम्

ङ्यापोः संज्ञाछन्दसोर्बहुलम् (6.3.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_63_NyApoH_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "NyApoH saMjYACandasorbahulam",
    text_dev              = "ङ्यापोः संज्ञाछन्दसोर्बहुलम्",
    padaccheda_dev        = "ङी-आपोः संज्ञा-छन्दसोः बहुलम्",
    why_dev               = "(सूत्रम् 6.3.63) ङ्यापोः संज्ञाछन्दसोर्बहुलम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
