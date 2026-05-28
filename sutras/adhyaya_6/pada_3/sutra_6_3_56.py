"""
6.3.56  वा घोषमिश्रशब्देषु  —  VIDHI

Padaccheda: वा घोष-मिश्र-शब्देषु

वा घोषमिश्रशब्देषु (6.3.56)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_56_vA_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA GozamiSraSabdezu",
    text_dev              = "वा घोषमिश्रशब्देषु",
    padaccheda_dev        = "वा घोष-मिश्र-शब्देषु",
    why_dev               = "(सूत्रम् 6.3.56) वा घोषमिश्रशब्देषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
