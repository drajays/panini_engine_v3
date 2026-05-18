"""
5.2.22  साप्तपदीनं सख्यम्  —  VIDHI

Padaccheda: साप्तपदीनम् सख्यम्

साप्तपदीनं सख्यम् (5.2.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_22_sAptapadIn_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_22_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sAptapadInaM saKyam",
    text_dev              = "साप्तपदीनं सख्यम्",
    padaccheda_dev        = "साप्तपदीनम् सख्यम्",
    why_dev               = "(सूत्रम् 5.2.22) साप्तपदीनं सख्यम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
