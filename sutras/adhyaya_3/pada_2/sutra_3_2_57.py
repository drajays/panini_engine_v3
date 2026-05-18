"""
3.2.57  कर्तरि भुवः खिष्णुच्खुकञौ  —  VIDHI

Padaccheda: कर्तरि भुवः खिष्णुच्-खुकञौ

krt-suffix rule: कर्तरि भुवः खिष्णुच्खुकञौ (57)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_57_kartari_57"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_57_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.57"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.57",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kartari BuvaH KizRucKukaYO",
    text_dev              = "कर्तरि भुवः खिष्णुच्खुकञौ",
    padaccheda_dev        = "कर्तरि भुवः खिष्णुच्-खुकञौ",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्तरि भुवः खिष्णुच्खुकञौ] विहितः (३.२.57)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
