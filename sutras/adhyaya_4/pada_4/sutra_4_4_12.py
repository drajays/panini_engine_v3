"""
4.4.12  वेतनादिभ्यो जीवति  —  VIDHI

Padaccheda: वेतन-आदिभ्यः जीवति (क्रियापदम्)

वेतनादिभ्यो जीवति (4.4.12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_12_vetanAdiBy_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_12_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vetanAdiByo jIvati",
    text_dev              = "वेतनादिभ्यो जीवति",
    padaccheda_dev        = "वेतन-आदिभ्यः जीवति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.12) वेतनादिभ्यो जीवति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
