"""
6.2.69  गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे  —  VIDHI

Padaccheda: गोत्र-अन्तेवासि-माणव-ब्राह्मणेषु क्षेपे

गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे (6.2.69)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_69_gotrAntevA_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gotrAntevAsimARavabrAhmaRezu kzepe",
    text_dev              = "गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे",
    padaccheda_dev        = "गोत्र-अन्तेवासि-माणव-ब्राह्मणेषु क्षेपे",
    why_dev               = "(सूत्रम् 6.2.69) गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
