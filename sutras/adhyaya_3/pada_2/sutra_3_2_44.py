"""
3.2.44  क्षेमप्रियमद्रेऽण् च  —  VIDHI

Padaccheda: क्षेम-प्रिय-मद्रे अण् च

krt-suffix rule: क्षेमप्रियमद्रेऽण् च (44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_44_kzemapriya_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_44_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzemapriyamadre'R ca",
    text_dev              = "क्षेमप्रियमद्रेऽण् च",
    padaccheda_dev        = "क्षेम-प्रिय-मद्रे अण् च",
    why_dev               = "धातोः कृत्-प्रत्ययः [क्षेमप्रियमद्रेऽण् च] विहितः (३.२.44)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
