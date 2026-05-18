"""
3.4.76  क्तोऽधिकरणे च ध्रौव्यगतिप्रत्यवसानार्थेभ्यः  —  VIDHI

Padaccheda: क्तः अधिकरणे च ध्रौव्य-गति-प्रत्यवसान-अर्थेभ्यः

krt-suffix rule: क्तोऽधिकरणे च ध्रौव्यगतिप्रत्यवसानार्थेभ्यः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_76_ktoDikara_76"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_76_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kto'DikaraRe ca DrOvyagatipratyavasAnArTeByaH",
    text_dev              = "क्तोऽधिकरणे च ध्रौव्यगतिप्रत्यवसानार्थेभ्यः",
    padaccheda_dev        = "क्तः अधिकरणे च ध्रौव्य-गति-प्रत्यवसान-अर्थेभ्यः",
    why_dev               = "धातोः प्रत्ययः (३.4.76)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
