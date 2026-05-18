"""
6.3.3  ओजःसहोऽम्भस्तमसः तृतीयायाः  —  VIDHI

Padaccheda: ओजः-सहः-अम्भः-तमसः तृतीयायाः

ओजःसहोऽम्भस्तमसः तृतीयायाः (6.3.3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_3_ojaHsahom_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_3_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ojaHsaho'mBastamasaH tftIyAyAH",
    text_dev              = "ओजःसहोऽम्भस्तमसः तृतीयायाः",
    padaccheda_dev        = "ओजः-सहः-अम्भः-तमसः तृतीयायाः",
    why_dev               = "(सूत्रम् 6.3.3) ओजःसहोऽम्भस्तमसः तृतीयायाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
