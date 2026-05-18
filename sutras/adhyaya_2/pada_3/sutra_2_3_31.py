"""
2.3.31  एनपा द्वितीया  —  VIDHI

Padaccheda: एनपा द्वितीया

ena-type pronoun takes dvitiya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_31_enapa_dvitiya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_31_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "enapA dvitIyA",
    text_dev              = "एनपा द्वितीया",
    padaccheda_dev        = "एनपा द्वितीया",
    why_dev               = "एनपा द्वितीया (२.३.३१)।",
    anuvritti_from        = ('2.3.2',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
