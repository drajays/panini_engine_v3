"""
5.3.27  दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो दिग्देशकालेष्वस्तातिः  —  VIDHI

Padaccheda: दिक्शब्देभ्यः सप्तमी-पञ्चमी-प्रथमाभ्यः दिग्-देश-कालेषु अस्तातिः

दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो दिग्देशकालेष्वस्तातिः (5.3.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_27_dikSabdeBy_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.27", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dikSabdeByaH saptamIpaYcamIpraTamAByo digdeSakAlezvastAtiH",
    text_dev              = "दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो दिग्देशकालेष्वस्तातिः",
    padaccheda_dev        = "दिक्शब्देभ्यः सप्तमी-पञ्चमी-प्रथमाभ्यः दिग्-देश-कालेषु अस्तातिः",
    why_dev               = "(सूत्रम् 5.3.27) दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो दिग्देशकालेष्वस्तातिः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
