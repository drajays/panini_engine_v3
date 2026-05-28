"""
6.3.119  मतौ बह्वचोऽनजिरादीनाम्  —  VIDHI

Padaccheda: मतौ बहु-अचः अनजिर-आदीनाम्

मतौ बह्वचोऽनजिरादीनाम् (6.3.119)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_119_matO_119"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.119"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.119",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "matO bahvaco'najirAdInAm",
    text_dev              = "मतौ बह्वचोऽनजिरादीनाम्",
    padaccheda_dev        = "मतौ बहु-अचः अनजिर-आदीनाम्",
    why_dev               = "(सूत्रम् 6.3.119) मतौ बह्वचोऽनजिरादीनाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
