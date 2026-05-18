"""
4.4.35  पक्षिमत्स्यमृगान् हन्ति  —  VIDHI

Padaccheda: पक्षि-मत्स्य-मृगान् हन्ति (क्रियापदम्)

पक्षिमत्स्यमृगान् हन्ति (4.4.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_35_pakzimatsy_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_35_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pakzimatsyamfgAn hanti",
    text_dev              = "पक्षिमत्स्यमृगान् हन्ति",
    padaccheda_dev        = "पक्षि-मत्स्य-मृगान् हन्ति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.35) पक्षिमत्स्यमृगान् हन्ति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
