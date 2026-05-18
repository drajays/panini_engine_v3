"""
2.4.8  क्षुद्रजन्तवः  —  VIDHI

Padaccheda: क्षुद्र-जन्तवः

Śāstra: dvandva compounds of small creatures (kṣudrajantavaḥ) take ekavacana.

Engine: sets gate "2_4_8_ksudrajantava_ekavacana".
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "2_4_8_ksudrajantava_ekavacana"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.8",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = "kzudrajantavaH",
    text_dev       = "क्षुद्रजन्तवः",
    padaccheda_dev = "क्षुद्र-जन्तवः",
    why_dev        = "क्षुद्रजन्तु-द्वन्द्वे एकवचनम्।",
    anuvritti_from = ("2.4.1", "2.4.2"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
