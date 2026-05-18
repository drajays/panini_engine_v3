"""
2.3.19  सहयुक्तेऽप्रधाने  —  VIDHI

Padaccheda: सह-युक्ते अप्रधाने

saha with non-primary member takes tritiya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_19_saha_apradhana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_19_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sahayukte'praDAne",
    text_dev              = "सहयुक्तेऽप्रधाने",
    padaccheda_dev        = "सह-युक्ते अप्रधाने",
    why_dev               = "सह-युक्ते अप्रधाने (२.३.१९)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
