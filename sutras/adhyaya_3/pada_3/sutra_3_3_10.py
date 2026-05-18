"""
3.3.10  तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्  —  VIDHI

Padaccheda: तुमुँन्-ण्वुलौ क्रियायाम् क्रिया-अर्थायाम्

krt-suffix rule: तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_10_tumunRvulO_10"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_3_10_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tumunRvulO kriyAyAM kriyArTAyAm",
    text_dev              = "तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्",
    padaccheda_dev        = "तुमुँन्-ण्वुलौ क्रियायाम् क्रिया-अर्थायाम्",
    why_dev               = "धातोः प्रत्ययः (३.3.10)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
