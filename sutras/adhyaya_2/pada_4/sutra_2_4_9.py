"""
2.4.9  येषां च विरोधः शाश्वतिकः  —  VIDHI

Padaccheda: येषाम् / च / विरोधः / शाश्वतिकः

Śāstra: dvandva compounds whose members have a permanent (śāśvatika) mutual
opposition also take ekavacana.

Engine: sets gate "2_4_9_virodha_sasvatika_ekavacana".
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "2_4_9_virodha_sasvatika_ekavacana"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.9",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = "yezAM ca viroDAH SAzvatikaH",
    text_dev       = "येषां च विरोधः शाश्वतिकः",
    padaccheda_dev = "येषाम् / च / विरोधः / शाश्वतिकः",
    why_dev        = "शाश्वत-विरोध-युक्त-द्वन्द्वे एकवचनम्।",
    anuvritti_from = ("2.4.1", "2.4.2"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
