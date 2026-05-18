"""
7.2.57  सेऽसिचि कृतचृतच्छृदतृदनृतः  —  VIDHI

Padaccheda: से अ-सिचि कृत-चृत-च्छृद-तृद-नृतः

सेऽसिचि कृतचृतच्छृदतृदनृतः (7.2.57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_57_sesici_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_57_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "se'sici kftacftacCfdatfdanftaH",
    text_dev              = "सेऽसिचि कृतचृतच्छृदतृदनृतः",
    padaccheda_dev        = "से अ-सिचि कृत-चृत-च्छृद-तृद-नृतः",
    why_dev               = "(सूत्रम् 7.2.57) सेऽसिचि कृतचृतच्छृदतृदनृतः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
