"""
5.1.59  पङ्क्तिविंशतित्रिंशत्चत्वारिंशत्पञ्चाशत्षष्टिसप्तत्यशीतिनवतिशतम्  —  VIDHI

Padaccheda: पङ्‍क्ति-विंशति-त्रिंशत्-चत्वारिंशत्-पञ्चाशत्-षष्टि-सप्तति-अशीति-नवति-शतम्

पङ्क्तिविंशतित्रिंशत्चत्वारिंशत्पञ्चाशत्षष्टिसप्तत्यशीतिनवतिशतम् (5.1.59)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_59_paNktiviMS_59"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_59_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.59"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.59",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paNktiviMSatitriMSatcatvAriMSatpaYcASatzazwisaptatyaSItinavatiSatam",
    text_dev              = "पङ्क्तिविंशतित्रिंशत्चत्वारिंशत्पञ्चाशत्षष्टिसप्तत्यशीतिनवतिशतम्",
    padaccheda_dev        = "पङ्‍क्ति-विंशति-त्रिंशत्-चत्वारिंशत्-पञ्चाशत्-षष्टि-सप्तति-अशीति-नवति-शतम्",
    why_dev               = "(सूत्रम् 5.1.59) पङ्क्तिविंशतित्रिंशत्चत्वारिंशत्पञ्चाशत्षष्टिसप्तत्यशीतिनवतिशतम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
