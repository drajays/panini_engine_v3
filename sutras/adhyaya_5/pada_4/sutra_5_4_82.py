"""
5.4.82  प्रतेरुरसः सप्तमीस्थात्  —  VIDHI

Padaccheda: प्रतेः उरसः सप्तमी-स्थात्

प्रतेरुरसः सप्तमीस्थात् (5.4.82)
Pāṭha: ashtadhyayi.com data.txt row i=54082 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_82_prateruras_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.82", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.82"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.82",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praterurasaH saptamIsTAt",
    text_dev              = "प्रतेरुरसः सप्तमीस्थात्",
    samagra_slp1          = "prateH saptamIsTAt urasaH ac",
    samagra_dev           = "प्रतेः सप्तमीस्थात् उरसः अच्",
    padaccheda_dev        = "प्रतेः उरसः सप्तमी-स्थात्",
    why_dev               = "(सूत्रम् 5.4.82) प्रतेरुरसः सप्तमीस्थात्।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
