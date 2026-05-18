"""
6.2.89  अमहन्नवं नगरेऽनुदीचाम्  —  VIDHI

Padaccheda: अमहन्नवम् नगरे अनुदीचाम्

अमहन्नवं नगरेऽनुदीचाम् (6.2.89)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_89_amahannava_89"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_89_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.89"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.89",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "amahannavaM nagare'nudIcAm",
    text_dev              = "अमहन्नवं नगरेऽनुदीचाम्",
    padaccheda_dev        = "अमहन्नवम् नगरे अनुदीचाम्",
    why_dev               = "(सूत्रम् 6.2.89) अमहन्नवं नगरेऽनुदीचाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
