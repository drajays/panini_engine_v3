"""
4.1.157  उदीचां वृद्धादगोत्रात्  —  VIDHI

Padaccheda: उदीचाम् वृद्धात् अ-गोत्रात्

उदीचां वृद्धादगोत्रात् (4.1.157)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_157_udIcAM_157"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_157_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.157"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udIcAM vfdDAdagotrAt",
    text_dev              = "उदीचां वृद्धादगोत्रात्",
    padaccheda_dev        = "उदीचाम् वृद्धात् अ-गोत्रात्",
    why_dev               = "(सूत्रम् 4.1.157) उदीचां वृद्धादगोत्रात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
