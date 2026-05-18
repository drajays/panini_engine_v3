"""
6.2.122  कंसमन्थशूर्पपाय्यकाण्डं द्विगौ  —  VIDHI

Padaccheda: कंस-मन्थ-शूर्प-पाय्य-काण्डम् द्विगौ

कंसमन्थशूर्पपाय्यकाण्डं द्विगौ (6.2.122)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_122_kaMsamanTa_122"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_122_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaMsamanTaSUrpapAyyakARqaM dvigO",
    text_dev              = "कंसमन्थशूर्पपाय्यकाण्डं द्विगौ",
    padaccheda_dev        = "कंस-मन्थ-शूर्प-पाय्य-काण्डम् द्विगौ",
    why_dev               = "(सूत्रम् 6.2.122) कंसमन्थशूर्पपाय्यकाण्डं द्विगौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
