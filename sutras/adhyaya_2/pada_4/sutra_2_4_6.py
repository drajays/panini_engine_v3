"""
2.4.6  जातिरप्राणिनाम्  —  VIDHI

Padaccheda: जातिः / अप्राणिनाम्

Śāstra: in dvandva compounds of non-animate beings (aprāṇin), a jāti
(genus/species) compound takes ekavacana.

Engine: sets gate "2_4_6_jati_apranin_ekavacana".
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "2_4_6_jati_apranin_ekavacana"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.6",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = "jAtir aprARinAm",
    text_dev       = "जातिरप्राणिनाम्",
    padaccheda_dev = "जातिः / अप्राणिनाम्",
    why_dev        = "अप्राणि-जाति-द्वन्द्वे एकवचनम्।",
    anuvritti_from = ("2.4.1", "2.4.2"),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
