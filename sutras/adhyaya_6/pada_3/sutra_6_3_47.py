"""
6.3.47  द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः  —  VIDHI

Padaccheda: द्वि-अष्टनः संख्यायाम् अ-बहुव्रीहि-अशीत्योः

द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः (6.3.47)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_47_dvyazwanaH_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvyazwanaH saMKyAyAmabahuvrIhyaSItyoH",
    text_dev              = "द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः",
    padaccheda_dev        = "द्वि-अष्टनः संख्यायाम् अ-बहुव्रीहि-अशीत्योः",
    why_dev               = "(सूत्रम् 6.3.47) द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
