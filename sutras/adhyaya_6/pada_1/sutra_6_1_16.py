"""
6.1.16  ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च  —  VIDHI

Padaccheda: ग्रहि-ज्या-वयि-व्यधि-वष्टि-विचति-वृश्चति-पृच्छति-भृज्जतीनाम् ङ्-इति च

ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च (6.1.16)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_16_grahijyAva_16"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_16_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.16"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.16",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grahijyAvayivyaDivazwivicativfScatipfcCatiBfjjatInAM Niti ca",
    text_dev              = "ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च",
    padaccheda_dev        = "ग्रहि-ज्या-वयि-व्यधि-वष्टि-विचति-वृश्चति-पृच्छति-भृज्जतीनाम् ङ्-इति च",
    why_dev               = "(सूत्रम् 6.1.16) ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
