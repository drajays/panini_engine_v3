"""
6.2.29  इगन्तकालकपालभगालशरावेषु द्विगौ  —  VIDHI

Padaccheda: इक्-अन्त-काल-कपाल-भगाल-शरावेषु द्विगौ

इगन्तकालकपालभगालशरावेषु द्विगौ (6.2.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_29_igantakAla_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "igantakAlakapAlaBagAlaSarAvezu dvigO",
    text_dev              = "इगन्तकालकपालभगालशरावेषु द्विगौ",
    padaccheda_dev        = "इक्-अन्त-काल-कपाल-भगाल-शरावेषु द्विगौ",
    why_dev               = "(सूत्रम् 6.2.29) इगन्तकालकपालभगालशरावेषु द्विगौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
