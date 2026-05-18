"""
4.4.38  आक्रन्दाट्ठञ्च  —  VIDHI

Padaccheda: आक्रन्दात् ठञ् च

आक्रन्दाट्ठञ्च (4.4.38)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_38_AkrandAwWa_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_38_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AkrandAwWaYca",
    text_dev              = "आक्रन्दाट्ठञ्च",
    padaccheda_dev        = "आक्रन्दात् ठञ् च",
    why_dev               = "(सूत्रम् 4.4.38) आक्रन्दाट्ठञ्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
