"""
3.2.100  अनौ कर्मणि  —  VIDHI

Padaccheda: अनौ कर्मणि

krt-suffix rule: अनौ कर्मणि (100)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_100_anO_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_100_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anO karmaRi",
    text_dev              = "अनौ कर्मणि",
    padaccheda_dev        = "अनौ कर्मणि",
    why_dev               = "धातोः कृत्-प्रत्ययः [अनौ कर्मणि] विहितः (३.२.100)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
