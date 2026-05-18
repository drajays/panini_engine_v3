"""
2.4.4  अध्वर्युक्रतुरनपुंसकम्  —  VIDHI

Padaccheda: अध्वर्यु-क्रतुः / अनपुंसकम्

Śāstra: the dvandva compound of adhvaryu-kratu (the adhvaryu priest and the
ritual) is not napuṃsaka (i.e. it retains its natural gender); the ekavacana
from 2.4.1 does not compel napuṃsaka-tva here.

Engine: sets gate "2_4_4_adhvaryukratu_anapumsaka".
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE = "2_4_4_adhvaryukratu_anapumsaka"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE] = True
    state.samjna_registry[_GATE] = True
    return state


SUTRA = SutraRecord(
    sutra_id       = "2.4.4",
    sutra_type     = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1      = "aDvaryukratur anapuMsakam",
    text_dev       = "अध्वर्युक्रतुरनपुंसकम्",
    padaccheda_dev = "अध्वर्यु-क्रतुः / अनपुंसकम्",
    why_dev        = "अध्वर्यु-क्रतु-द्वन्द्वे नपुंसकत्वं न भवति।",
    anuvritti_from = ("2.4.2",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)
