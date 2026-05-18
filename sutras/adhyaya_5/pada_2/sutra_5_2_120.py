"""
5.2.120  रूपादाहतप्रशंसयोरप्  —  VIDHI

Padaccheda: रूपात् आहत-प्रशंसयोः यप्

रूपादाहतप्रशंसयोरप् (5.2.120)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_120_rUpAdAhata_120"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_120_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.120"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rUpAdAhatapraSaMsayorap",
    text_dev              = "रूपादाहतप्रशंसयोरप्",
    padaccheda_dev        = "रूपात् आहत-प्रशंसयोः यप्",
    why_dev               = "(सूत्रम् 5.2.120) रूपादाहतप्रशंसयोरप्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
