"""
6.2.90  अर्मे चावर्णं द्व्यच्त्र्यच्  —  VIDHI

Padaccheda: अर्मे च अवर्णम् द्वि-अच् त्रि-अच्

अर्मे चावर्णं द्व्यच्त्र्यच् (6.2.90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_90_arme_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_90_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arme cAvarRaM dvyactryac",
    text_dev              = "अर्मे चावर्णं द्व्यच्त्र्यच्",
    padaccheda_dev        = "अर्मे च अवर्णम् द्वि-अच् त्रि-अच्",
    why_dev               = "(सूत्रम् 6.2.90) अर्मे चावर्णं द्व्यच्त्र्यच्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
