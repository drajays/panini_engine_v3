"""
6.3.69  वाचंयमपुरंदरौ च  —  VIDHI

Padaccheda: वाचंयम-पुरंदरौ च

वाचंयमपुरंदरौ च (6.3.69)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_69_vAcaMyamap_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_69_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAcaMyamapuraMdarO ca",
    text_dev              = "वाचंयमपुरंदरौ च",
    padaccheda_dev        = "वाचंयम-पुरंदरौ च",
    why_dev               = "(सूत्रम् 6.3.69) वाचंयमपुरंदरौ च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
