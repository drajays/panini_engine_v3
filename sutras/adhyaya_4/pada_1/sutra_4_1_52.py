"""
4.1.52  बहुव्रीहेश्चान्तोदात्तात्  —  VIDHI

Padaccheda: बहुव्रीहेः च अन्त-उदात्तात्

बहुव्रीहेश्चान्तोदात्तात् (4.1.52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_52_bahuvrIheS_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_52_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahuvrIheScAntodAttAt",
    text_dev              = "बहुव्रीहेश्चान्तोदात्तात्",
    padaccheda_dev        = "बहुव्रीहेः च अन्त-उदात्तात्",
    why_dev               = "(सूत्रम् 4.1.52) बहुव्रीहेश्चान्तोदात्तात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
