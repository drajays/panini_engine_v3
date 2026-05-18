"""
3.2.77  स्थः क च  —  VIDHI

Padaccheda: स्थः क (लुप्तप्रथमान्तनिर्देशः) च

krt-suffix rule: स्थः क च (77)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_77_sTaH_77"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_77_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTaH ka ca",
    text_dev              = "स्थः क च",
    padaccheda_dev        = "स्थः क (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः कृत्-प्रत्ययः [स्थः क च] विहितः (३.२.77)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
