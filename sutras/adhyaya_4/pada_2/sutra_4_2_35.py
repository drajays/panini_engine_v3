"""
4.2.35  महाराजप्रोष्ठपदाट्ठञ्  —  VIDHI

Padaccheda: महाराज-प्रोष्ठपदात् ठञ्

महाराजप्रोष्ठपदाट्ठञ् (4.2.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_35_mahArAjapr_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_35_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mahArAjaprozWapadAwWaY",
    text_dev              = "महाराजप्रोष्ठपदाट्ठञ्",
    padaccheda_dev        = "महाराज-प्रोष्ठपदात् ठञ्",
    why_dev               = "(सूत्रम् 4.2.35) महाराजप्रोष्ठपदाट्ठञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
