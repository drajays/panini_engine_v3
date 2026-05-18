"""
5.4.74  ऋक्पूरप्धूःपथामानक्षे  —  VIDHI

Padaccheda: ऋक्-पूः-अप्-धूह्-पथाम् अ (लुप्तप्रथमान्तनिर्देशः) अनक्षे

ऋक्पूरप्धूःपथामानक्षे (5.4.74)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_74_fkpUrapDUH_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_74_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fkpUrapDUHpaTAmAnakze",
    text_dev              = "ऋक्पूरप्धूःपथामानक्षे",
    padaccheda_dev        = "ऋक्-पूः-अप्-धूह्-पथाम् अ (लुप्तप्रथमान्तनिर्देशः) अनक्षे",
    why_dev               = "(सूत्रम् 5.4.74) ऋक्पूरप्धूःपथामानक्षे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
