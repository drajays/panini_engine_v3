"""
6.2.116  नञो जरमरमित्रमृताः  —  VIDHI

Padaccheda: नञः जर-मर-मित्र-मृताः

नञो जरमरमित्रमृताः (6.2.116)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_116_naYo_116"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_116_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naYo jaramaramitramftAH",
    text_dev              = "नञो जरमरमित्रमृताः",
    padaccheda_dev        = "नञः जर-मर-मित्र-मृताः",
    why_dev               = "(सूत्रम् 6.2.116) नञो जरमरमित्रमृताः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
