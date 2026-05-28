"""
6.2.168  नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः  —  VIDHI

Padaccheda: न अव्यय-दिक्शब्द-गो-महत्-स्थूल-मुष्टि-पृथु-वत्सेभ्यः

नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः (6.2.168)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_168_nAvyayadik_168"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.168"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.168",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAvyayadikSabdagomahatsTUlamuzwipfTuvatseByaH",
    text_dev              = "नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः",
    padaccheda_dev        = "न अव्यय-दिक्शब्द-गो-महत्-स्थूल-मुष्टि-पृथु-वत्सेभ्यः",
    why_dev               = "(सूत्रम् 6.2.168) नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
