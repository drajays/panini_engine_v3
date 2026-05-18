"""
7.3.2  केकयमित्त्रयुप्रलयानां यादेरियः  —  VIDHI

Padaccheda: केकय-मित्त्रयु-प्रलयानाम् य-आदेः इयः

केकयमित्त्रयुप्रलयानां यादेरियः (7.3.2)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_2_kekayamitt_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_2_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kekayamittrayupralayAnAM yAderiyaH",
    text_dev              = "केकयमित्त्रयुप्रलयानां यादेरियः",
    padaccheda_dev        = "केकय-मित्त्रयु-प्रलयानाम् य-आदेः इयः",
    why_dev               = "(सूत्रम् 7.3.2) केकयमित्त्रयुप्रलयानां यादेरियः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
