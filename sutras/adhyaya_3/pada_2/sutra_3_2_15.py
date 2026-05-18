"""
3.2.15  अधिकरणे शेतेः  —  VIDHI

Padaccheda: अधिकरणे शेतेः

krt-suffix rule: अधिकरणे शेतेः (15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_15_aDikaraRe_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_15_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aDikaraRe SeteH",
    text_dev              = "अधिकरणे शेतेः",
    padaccheda_dev        = "अधिकरणे शेतेः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अधिकरणे शेतेः] विहितः (३.२.15)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
