"""
2.3.33  करणे च स्तोकाल्पकृच्छ्रकतिपयस्यासत्त्ववचनस्य  —  VIDHI

Padaccheda: करणे च स्तोक-अल्प-कृच्छ्र-कतिपयस्य असत्त्ववचनस्य

Tritiya for karana: stoka, alpa, krcchra, katipaya non-entities.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_33_karane_stoka_alpa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_33_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karaRe ca stokAlpakfcCrakatipayasyAsattvavacanasya",
    text_dev              = "करणे च स्तोकाल्पकृच्छ्रकतिपयस्यासत्त्ववचनस्य",
    padaccheda_dev        = "करणे च स्तोक-अल्प-कृच्छ्र-कतिपयस्य असत्त्ववचनस्य",
    why_dev               = "करणे च स्तोक-अल्प-कृच्छ्र-कतिपयस्य असत्त्ववचनस्य (२.३.३३)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
