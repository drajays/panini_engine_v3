"""
2.1.32  कर्तृकरणे कृता बहुलम्  —  VIDHI

Padaccheda: कर्तृ-करणे कृता बहुलम्

karta and karana with kta-suffix form bahula tatpurusha compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_32_kartru_karana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_32_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kartfkaraRe kftA bahulam",
    text_dev              = "कर्तृकरणे कृता बहुलम्",
    padaccheda_dev        = "कर्तृ-करणे कृता बहुलम्",
    why_dev               = "कर्तृ-करणे कृता बहुलं समासः (२.१.३२)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
