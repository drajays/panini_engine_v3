"""
2.3.25  विभाषा गुणेऽस्त्रियाम्  —  VIDHI

Padaccheda: विभाषा गुणे अ-स्त्रियाम्

Optional tritiya for quality words in non-feminine gender.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_25_guna_astriyam"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_25_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA guRe'striyAm",
    text_dev              = "विभाषा गुणेऽस्त्रियाम्",
    padaccheda_dev        = "विभाषा गुणे अ-स्त्रियाम्",
    why_dev               = "गुणे अस्त्रियाम् विभाषा (२.३.२५)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
