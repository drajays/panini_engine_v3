"""
3.1.90  कुषिरजोः प्राचां श्यन् परस्मैपदं च  —  VIDHI

Padaccheda: कुषि-रजोः प्राचाम् श्यन् परस्मैपदम् च

Krt suffix rule from dhatu: कुषिरजोः प्राचां श्यन् परस्मैपदं च (90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_90_kuzirajoH_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_90_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kuzirajoH prAcAM Syan parasmEpadaM ca",
    text_dev              = "कुषिरजोः प्राचां श्यन् परस्मैपदं च",
    padaccheda_dev        = "कुषि-रजोः प्राचाम् श्यन् परस्मैपदम् च",
    why_dev               = "धातोः [कुषिरजोः प्राचां श्यन् परस्मैपदं च]-प्रत्ययः विहितः (३.१.90)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
