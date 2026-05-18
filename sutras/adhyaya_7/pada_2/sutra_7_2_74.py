"""
7.2.74  स्मिपूङ्रञ्ज्वशां सनि  —  VIDHI

Padaccheda: स्मि-पूङ्‍-ऋ-अञ्जू-अशाम् सनि

स्मिपूङ्रञ्ज्वशां सनि (7.2.74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_74_smipUNraYj_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_74_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "smipUNraYjvaSAM sani",
    text_dev              = "स्मिपूङ्रञ्ज्वशां सनि",
    padaccheda_dev        = "स्मि-पूङ्‍-ऋ-अञ्जू-अशाम् सनि",
    why_dev               = "(सूत्रम् 7.2.74) स्मिपूङ्रञ्ज्वशां सनि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
