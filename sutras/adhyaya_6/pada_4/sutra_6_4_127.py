"""
6.4.127  अर्वणस्त्रसावनञः  —  VIDHI

Padaccheda: अर्वणः तृ (लुप्तप्रथमान्तनिर्देशः) अ-सौ अन्-अञः

अर्वणस्त्रसावनञः (6.4.127)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_127_arvaRastra_127"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_127_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arvaRastrasAvanaYaH",
    text_dev              = "अर्वणस्त्रसावनञः",
    padaccheda_dev        = "अर्वणः तृ (लुप्तप्रथमान्तनिर्देशः) अ-सौ अन्-अञः",
    why_dev               = "(सूत्रम् 6.4.127) अर्वणस्त्रसावनञः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
