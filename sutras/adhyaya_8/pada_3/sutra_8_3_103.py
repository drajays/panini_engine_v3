"""
8.3.103  युष्मत्तत्ततक्षुःष्वन्तःपादम्  —  VIDHI

Padaccheda: युष्मत्-त्द्-ततक्षुःषु अन्तः-पादम्

युष्मत्तत्ततक्षुःष्वन्तःपादम् (8.3.103)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_103_yuzmattatt_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_103_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yuzmattattatakzuHzvantaHpAdam",
    text_dev              = "युष्मत्तत्ततक्षुःष्वन्तःपादम्",
    padaccheda_dev        = "युष्मत्-त्द्-ततक्षुःषु अन्तः-पादम्",
    why_dev               = "(सूत्रम् 8.3.103) युष्मत्तत्ततक्षुःष्वन्तःपादम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
