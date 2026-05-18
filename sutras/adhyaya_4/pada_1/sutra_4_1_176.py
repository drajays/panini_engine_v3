"""
4.1.176  स्त्रियामवन्तिकुन्तिकुरुभ्यश्च  —  VIDHI

Padaccheda: स्त्रियाम् अवन्ति-कुन्ति-कुरुभ्यः च

स्त्रियामवन्तिकुन्तिकुरुभ्यश्च (4.1.176)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_176_striyAmava_176"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_176_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.176"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.176",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "striyAmavantikuntikuruByaSca",
    text_dev              = "स्त्रियामवन्तिकुन्तिकुरुभ्यश्च",
    padaccheda_dev        = "स्त्रियाम् अवन्ति-कुन्ति-कुरुभ्यः च",
    why_dev               = "(सूत्रम् 4.1.176) स्त्रियामवन्तिकुन्तिकुरुभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
