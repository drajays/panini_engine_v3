"""
1.2.65  वृद्धो यूना तल्लक्षणश्चेदेव विशेषः  —  VIDHI (SAMJNA gate)

*Padaccheda:* **वृद्धः** / **यूना** / **तत्-लक्षणः** / **चेत्** / **एव** / **विशेषः**

When ekaśeṣa applies between a vṛddha (elder) and a yūna (junior/young
person), if the distinguishing qualifier (viśeṣa) is *tal-lakṣaṇa* —
derived from or marked by the feminine ā suffix characteristic of the
pair — then ekaśeṣa is applicable.  This restricts the ekaśeṣa of
1.2.64 to cases where the qualifying feature is inherently tied to the
pair's shared marking.

Operational role (v3):
  - Registers the gate ``1_2_65_vfdDa_yUna`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when determining whether the
    vṛddha–yūna pair qualifies for ekaśeṣa under the tal-lakṣaṇa
    condition.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_65_vfdDa_yUna"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.65",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "vfdDo yUnA tallakzaRazcedeva vizezaH",
    text_dev                = "वृद्धो यूना तल्लक्षणश्चेदेव विशेषः",
    padaccheda_dev          = "वृद्धः / यूना / तत्-लक्षणः / चेत् / एव / विशेषः",
    why_dev                 = (
        "वृद्धस्य यूना सह एकशेषे तल्लक्षण एव विशेषो यदा भवति तदा एकशेषः सिध्यति — "
        "आ-प्रत्यय-लक्षितो विशेषो यत्र तत्र वृद्ध-यून-एकशेष-विधिः।"
    ),
    anuvritti_from          = ("1.2.64",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
