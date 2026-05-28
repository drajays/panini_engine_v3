"""
6.3.75  नभ्राण्नपान्नवेदानासत्यानमुचिनकुलनखनपुंसकनक्षत्रनक्रनाकेषु प्रकृत्या  —  VIDHI

Padaccheda: नभ्राट्-नपात्-नवेदा-नासत्या-नमुचि-नकुल-नख-नपुंसक-नक्षत्र-नक्र-नाकेषु प्रकृत्या

नभ्राण्नपान्नवेदानासत्यानमुचिनकुलनखनपुंसकनक्षत्रनक्रनाकेषु प्रकृत्या (6.3.75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_75_naBrARnapA_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "naBrARnapAnnavedAnAsatyAnamucinakulanaKanapuMsakanakzatranakranAkezu prakftyA",
    text_dev              = "नभ्राण्नपान्नवेदानासत्यानमुचिनकुलनखनपुंसकनक्षत्रनक्रनाकेषु प्रकृत्या",
    padaccheda_dev        = "नभ्राट्-नपात्-नवेदा-नासत्या-नमुचि-नकुल-नख-नपुंसक-नक्षत्र-नक्र-नाकेषु प्रकृत्या",
    why_dev               = "(सूत्रम् 6.3.75) नभ्राण्नपान्नवेदानासत्यानमुचिनकुलनखनपुंसकनक्षत्रनक्रनाकेषु प्रकृत्या।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
