"""
4.1.147  गोत्रस्त्रियाः कुत्सने ण च  —  VIDHI

Padaccheda: गोत्र-स्त्रियाः कुत्सने ण (लुप्तप्रथमान्तनिर्देशः) च

गोत्रस्त्रियाः कुत्सने ण च (4.1.147)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_147_gotrastriy_147"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_147_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.147"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.147",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gotrastriyAH kutsane Ra ca",
    text_dev              = "गोत्रस्त्रियाः कुत्सने ण च",
    padaccheda_dev        = "गोत्र-स्त्रियाः कुत्सने ण (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "(सूत्रम् 4.1.147) गोत्रस्त्रियाः कुत्सने ण च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
