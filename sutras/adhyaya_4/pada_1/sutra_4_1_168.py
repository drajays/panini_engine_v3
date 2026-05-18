"""
4.1.168  जनपदशब्दात् क्षत्रियादञ्  —  VIDHI

Padaccheda: जनपद-शब्दात् क्षत्रियात् अञ्

जनपदशब्दात् क्षत्रियादञ् (4.1.168)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_168_janapadaSa_168"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_168_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.168"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.168",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "janapadaSabdAt kzatriyAdaY",
    text_dev              = "जनपदशब्दात् क्षत्रियादञ्",
    padaccheda_dev        = "जनपद-शब्दात् क्षत्रियात् अञ्",
    why_dev               = "(सूत्रम् 4.1.168) जनपदशब्दात् क्षत्रियादञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
