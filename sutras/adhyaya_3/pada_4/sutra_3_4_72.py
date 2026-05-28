"""
3.4.72  गत्यर्थाकर्मकश्लिषशीङ्स्थाऽऽसवसजनरुहजीर्यतिभ्यश्च  —  VIDHI

Padaccheda: गति-अर्थ-अकर्मक-श्लिष-शीङ्-स्था-आस-वस-जन-रुह-जीर्यतिभ्यः च

krt-suffix rule: गत्यर्थाकर्मकश्लिषशीङ्स्थाऽऽसवसजनरुहजीर्यतिभ्यश्च
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_72_gatyarTAka_72"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gatyarTAkarmakaSlizaSINsTA''savasajanaruhajIryatiByaSca",
    text_dev              = "गत्यर्थाकर्मकश्लिषशीङ्स्थाऽऽसवसजनरुहजीर्यतिभ्यश्च",
    padaccheda_dev        = "गति-अर्थ-अकर्मक-श्लिष-शीङ्-स्था-आस-वस-जन-रुह-जीर्यतिभ्यः च",
    why_dev               = "धातोः प्रत्ययः (३.4.72)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
