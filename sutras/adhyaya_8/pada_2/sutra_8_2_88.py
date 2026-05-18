"""
8.2.88  ये यज्ञकर्मणि  —  VIDHI

Padaccheda: ये (लुप्तषष्ठ्यन्तनिर्देशः) यज्ञकर्मणि

ये यज्ञकर्मणि (8.2.88)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_88_ye_88"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_88_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ye yajYakarmaRi",
    text_dev              = "ये यज्ञकर्मणि",
    padaccheda_dev        = "ये (लुप्तषष्ठ्यन्तनिर्देशः) यज्ञकर्मणि",
    why_dev               = "(सूत्रम् 8.2.88) ये यज्ञकर्मणि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
