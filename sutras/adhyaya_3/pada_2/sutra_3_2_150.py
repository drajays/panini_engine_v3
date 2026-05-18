"""
3.2.150  जुचङ्क्रम्यदन्द्रम्यसृगृधिज्वलशुचलषपतपदः  —  VIDHI

Padaccheda: जु-चङ्क्रम्य-दन्द्रम्य-सृ-गृधि-ज्वल-शुच-लष-पत-पदः

krt-suffix rule: जुचङ्क्रम्यदन्द्रम्यसृगृधिज्वलशुचलषपतपदः (150)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_150_jucaNkramy_150"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_150_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.150"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.150",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jucaNkramyadandramyasfgfDijvalaSucalazapatapadaH",
    text_dev              = "जुचङ्क्रम्यदन्द्रम्यसृगृधिज्वलशुचलषपतपदः",
    padaccheda_dev        = "जु-चङ्क्रम्य-दन्द्रम्य-सृ-गृधि-ज्वल-शुच-लष-पत-पदः",
    why_dev               = "धातोः कृत्-प्रत्ययः [जुचङ्क्रम्यदन्द्रम्यसृगृधिज्वलशुचलषपतपदः] विहितः (३.२.150)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
