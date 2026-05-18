"""
3.2.186  कर्तरि चर्षिदेवतयोः  —  VIDHI

Padaccheda: कर्तरि च ऋषि-देवतयोः

krt-suffix rule: कर्तरि चर्षिदेवतयोः (186)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_186_kartari_186"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_186_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.186"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.186",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kartari carzidevatayoH",
    text_dev              = "कर्तरि चर्षिदेवतयोः",
    padaccheda_dev        = "कर्तरि च ऋषि-देवतयोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्तरि चर्षिदेवतयोः] विहितः (३.२.186)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
