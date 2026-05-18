"""
5.2.4  विभाषा तिलमाषोमाभङ्गाऽणुभ्यः  —  VIDHI

Padaccheda: विभाषा तिल-माष-उमा-भङ्गा-अणुभ्यः

विभाषा तिलमाषोमाभङ्गाऽणुभ्यः (5.2.4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_4_viBAzA_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_4_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA tilamAzomABaNgA'RuByaH",
    text_dev              = "विभाषा तिलमाषोमाभङ्गाऽणुभ्यः",
    padaccheda_dev        = "विभाषा तिल-माष-उमा-भङ्गा-अणुभ्यः",
    why_dev               = "(सूत्रम् 5.2.4) विभाषा तिलमाषोमाभङ्गाऽणुभ्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
