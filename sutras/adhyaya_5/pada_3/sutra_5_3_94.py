"""
5.3.94  एकाच्च प्राचाम्  —  VIDHI

Padaccheda: एकात् च प्राचाम्

एकाच्च प्राचाम् (5.3.94)
Pāṭha: ashtadhyayi.com data.txt row i=53094 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_94_ekAcca_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.94", state, "5.3.70"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ekAcca prAcAm",
    text_dev              = "एकाच्च प्राचाम्",
    samagra_slp1          = "dvayoH ekasya nirDAraRe ekAt qatarac bahUnAm ekasya nirDAraRe ekAt qatamac - iti prAcAm matam ",
    samagra_dev           = "द्वयोः एकस्य निर्धारणे एकात् डतरच्, बहूनाम् एकस्य निर्धारणे एकात् डतमच् - (इति) प्राचाम् (मतम्) ।",
    padaccheda_dev        = "एकात् च प्राचाम्",
    why_dev               = "(सूत्रम् 5.3.94) एकाच्च प्राचाम्।",
    anuvritti_from        = ('5.3.70',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
