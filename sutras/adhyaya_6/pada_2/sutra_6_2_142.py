"""
6.2.142  नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु  —  VIDHI

Padaccheda: न उत्तरपदे अनुदात्त-आदौ अ-पृथिवी-रुद्र-पूष-मन्थिषु

नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु (6.2.142)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_142_nottarapad_142"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_142_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.142"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.142",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nottarapade'nudAttAdAvapfTivIrudrapUzamanTizu",
    text_dev              = "नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु",
    padaccheda_dev        = "न उत्तरपदे अनुदात्त-आदौ अ-पृथिवी-रुद्र-पूष-मन्थिषु",
    why_dev               = "(सूत्रम् 6.2.142) नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
