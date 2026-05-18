"""
6.1.219  मतोः पूर्वमात् संज्ञायां स्त्रियाम्  —  VIDHI

Padaccheda: मतोः पूर्वम् आत् संज्ञायाम् स्त्रियाम्

मतोः पूर्वमात् संज्ञायां स्त्रियाम् (6.1.219)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_219_matoH_219"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_219_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.219"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.219",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "matoH pUrvamAt saMjYAyAM striyAm",
    text_dev              = "मतोः पूर्वमात् संज्ञायां स्त्रियाम्",
    padaccheda_dev        = "मतोः पूर्वम् आत् संज्ञायाम् स्त्रियाम्",
    why_dev               = "(सूत्रम् 6.1.219) मतोः पूर्वमात् संज्ञायां स्त्रियाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
