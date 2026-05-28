"""
3.2.5  तुन्दशोकयोः परिमृजापनुदोः  —  VIDHI

Padaccheda: तुन्द-शोकयोः परिमृज-अपनुदोः

krt-suffix rule: तुन्दशोकयोः परिमृजापनुदोः (5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_5_tundaSokay_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tundaSokayoH parimfjApanudoH",
    text_dev              = "तुन्दशोकयोः परिमृजापनुदोः",
    padaccheda_dev        = "तुन्द-शोकयोः परिमृज-अपनुदोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [तुन्दशोकयोः परिमृजापनुदोः] विहितः (३.२.5)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
