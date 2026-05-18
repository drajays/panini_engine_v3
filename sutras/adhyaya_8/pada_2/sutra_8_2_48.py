"""
8.2.48  अञ्चोऽनपादाने  —  VIDHI

Padaccheda: अञ्चः अन्-अपादाने

अञ्चोऽनपादाने (8.2.48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_48_aYconapAd_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_48_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aYco'napAdAne",
    text_dev              = "अञ्चोऽनपादाने",
    padaccheda_dev        = "अञ्चः अन्-अपादाने",
    why_dev               = "(सूत्रम् 8.2.48) अञ्चोऽनपादाने।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
