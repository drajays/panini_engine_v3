"""
7.2.61  अचस्तास्वत् थल्यनिटो नित्यम्  —  VIDHI

Padaccheda: अचः तास्-वत् थलि अन्-इटः नित्यम्

अचस्तास्वत् थल्यनिटो नित्यम् (7.2.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_61_acastAsvat_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "acastAsvat Talyaniwo nityam",
    text_dev              = "अचस्तास्वत् थल्यनिटो नित्यम्",
    padaccheda_dev        = "अचः तास्-वत् थलि अन्-इटः नित्यम्",
    why_dev               = "(सूत्रम् 7.2.61) अचस्तास्वत् थल्यनिटो नित्यम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
