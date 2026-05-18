"""
3.2.136  अलंकृञ्निराकृञ्प्रजनोत्पचोत्पतोन्मदरुच्यपत्रपवृतुवृधुसहचर इष्णुच्  —  VIDHI

Padaccheda: अलंकृञ्-निराकृञ्-प्रजन-उत्पच-उत्पत-उन्मद-रुचि-अपत्रप-वृतु-वृधु-सह-चर इष्णुच्

krt-suffix rule: अलंकृञ्निराकृञ्प्रजनोत्पचोत्पतोन्मदरुच्यपत्रपवृतुवृधुसहचर इष्णुच् (136)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_136_alaMkfYnir_136"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_136_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "alaMkfYnirAkfYprajanotpacotpatonmadarucyapatrapavftuvfDusahacara izRuc",
    text_dev              = "अलंकृञ्निराकृञ्प्रजनोत्पचोत्पतोन्मदरुच्यपत्रपवृतुवृधुसहचर इष्णुच्",
    padaccheda_dev        = "अलंकृञ्-निराकृञ्-प्रजन-उत्पच-उत्पत-उन्मद-रुचि-अपत्रप-वृतु-वृधु-सह-चर इष्णुच्",
    why_dev               = "धातोः कृत्-प्रत्ययः [अलंकृञ्निराकृञ्प्रजनोत्पचोत्पतोन्मदरुच्यपत्रपवृतुवृधुसहचर इष्णुच्] विहितः (३.२.136)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
