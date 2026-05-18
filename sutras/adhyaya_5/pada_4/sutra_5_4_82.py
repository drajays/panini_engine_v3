"""
5.4.82  प्रतेरुरसः सप्तमीस्थात्  —  VIDHI

Padaccheda: प्रतेः उरसः सप्तमी-स्थात्

प्रतेरुरसः सप्तमीस्थात् (5.4.82)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_82_prateruras_82"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_82_arm") is True


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
    padaccheda_dev        = "प्रतेः उरसः सप्तमी-स्थात्",
    why_dev               = "(सूत्रम् 5.4.82) प्रतेरुरसः सप्तमीस्थात्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
