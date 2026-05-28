"""
8.1.44  किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्  —  VIDHI

Padaccheda: किम् क्रियाप्रश्ने अन्-उपसर्गम् अप्रतिषिद्धम्

किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम् (8.1.44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_44_kiM_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_1_44_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kiM kriyApraSne'nupasargamapratizidDam",
    text_dev              = "किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्",
    padaccheda_dev        = "किम् क्रियाप्रश्ने अन्-उपसर्गम् अप्रतिषिद्धम्",
    why_dev               = "(सूत्रम् 8.1.44) किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
