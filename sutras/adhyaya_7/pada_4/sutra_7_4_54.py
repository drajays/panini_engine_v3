"""
7.4.54  सनि मीमाघुरभलभशकपतपदामच इस्  —  VIDHI

Padaccheda: सनि मी-मा-घु-रभ-लभ-शक-पत-पदाम् अच इस्

सनि मीमाघुरभलभशकपतपदामच इस् (7.4.54)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_4_54_sani_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_4_54_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sani mImAGuraBalaBaSakapatapadAmaca is",
    text_dev              = "सनि मीमाघुरभलभशकपतपदामच इस्",
    padaccheda_dev        = "सनि मी-मा-घु-रभ-लभ-शक-पत-पदाम् अच इस्",
    why_dev               = "(सूत्रम् 7.4.54) सनि मीमाघुरभलभशकपतपदामच इस्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
