"""
4.3.98  वासुदेवार्जुनाभ्यां वुन्  —  VIDHI

Padaccheda: वासुदेव-अर्जुनाभ्याम् वुन्

वासुदेवार्जुनाभ्यां वुन् (4.3.98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_98_vAsudevArj_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_98_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAsudevArjunAByAM vun",
    text_dev              = "वासुदेवार्जुनाभ्यां वुन्",
    padaccheda_dev        = "वासुदेव-अर्जुनाभ्याम् वुन्",
    why_dev               = "(सूत्रम् 4.3.98) वासुदेवार्जुनाभ्यां वुन्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
