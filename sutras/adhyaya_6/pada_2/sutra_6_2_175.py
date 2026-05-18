"""
6.2.175  बहोर्नञ्वदुत्तरपदभूम्नि  —  VIDHI

Padaccheda: बहोः नञ्-वत् उत्तरपद-भूम्नि

बहोर्नञ्वदुत्तरपदभूम्नि (6.2.175)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_175_bahornaYva_175"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_175_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.175"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.175",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahornaYvaduttarapadaBUmni",
    text_dev              = "बहोर्नञ्वदुत्तरपदभूम्नि",
    padaccheda_dev        = "बहोः नञ्-वत् उत्तरपद-भूम्नि",
    why_dev               = "(सूत्रम् 6.2.175) बहोर्नञ्वदुत्तरपदभूम्नि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
