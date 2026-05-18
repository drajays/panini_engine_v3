"""
3.2.129  ताच्छील्यवयोवचनशक्तिषु चानश्  —  VIDHI

Padaccheda: ताच्छील्य-वयोवचन-शक्तिषु चानश्

krt-suffix rule: ताच्छील्यवयोवचनशक्तिषु चानश् (129)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_129_tAcCIlyava_129"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_129_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.129"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.129",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tAcCIlyavayovacanaSaktizu cAnaS",
    text_dev              = "ताच्छील्यवयोवचनशक्तिषु चानश्",
    padaccheda_dev        = "ताच्छील्य-वयोवचन-शक्तिषु चानश्",
    why_dev               = "धातोः कृत्-प्रत्ययः [ताच्छील्यवयोवचनशक्तिषु चानश्] विहितः (३.२.129)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
