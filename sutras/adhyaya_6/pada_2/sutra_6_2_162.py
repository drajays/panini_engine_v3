"""
6.2.162  बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने  —  VIDHI

Padaccheda: बहुव्रीहौ इदम्-एतद्-तद्‍भ्यः प्रथम-पूरणयोः क्रियागणने

बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने (6.2.162)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_162_bahuvrIhAv_162"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.162"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.162",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahuvrIhAvidametattadByaH praTamapUraRayoH kriyAgaRane",
    text_dev              = "बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने",
    padaccheda_dev        = "बहुव्रीहौ इदम्-एतद्-तद्‍भ्यः प्रथम-पूरणयोः क्रियागणने",
    why_dev               = "(सूत्रम् 6.2.162) बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
