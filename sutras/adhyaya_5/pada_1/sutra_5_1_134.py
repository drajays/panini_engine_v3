"""
5.1.134  गोत्रचरणाच्श्लाघाऽत्याकारतदवेतेषु  —  VIDHI

Padaccheda: गोत्र-चरणात् श्लाघा-अत्याकार-तदवेतेषु

गोत्रचरणाच्श्लाघाऽत्याकारतदवेतेषु (5.1.134)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_134_gotracaraR_134"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_134_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.134"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.134",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gotracaraRAcSlAGA'tyAkAratadavetezu",
    text_dev              = "गोत्रचरणाच्श्लाघाऽत्याकारतदवेतेषु",
    padaccheda_dev        = "गोत्र-चरणात् श्लाघा-अत्याकार-तदवेतेषु",
    why_dev               = "(सूत्रम् 5.1.134) गोत्रचरणाच्श्लाघाऽत्याकारतदवेतेषु।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
