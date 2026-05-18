"""
1.2.50  इद्गोण्याः  —  SAMJNA

*Padaccheda:* **इत्** / **गोण्याः**

A word meaning a secondary referent (goṇī = secondary name/signifier) that
carries the it-marker "i" is treated as a primary referent.  This sūtra
establishes a saṃjñā gate for the goṇī-with-id-marker classification.

Operational role (v3):
  - Registers the gate ``1_2_50_id_goNyAH`` in both ``paribhasha_gates``
    and ``samjna_registry``.
  - Downstream rules consult this gate when determining whether a goṇī term
    with an "i" it-marker qualifies as a primary referent.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_50_id_goNyAH"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.50",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "id goRyAH",
    text_dev                = "इद्गोण्याः",
    padaccheda_dev          = "इत् / गोण्याः",
    why_dev                 = (
        "इत्-संज्ञकं गोणी-शब्दं मुख्य-वाचकवद् उपचर्यते — "
        "इद्-इत्-मार्करयुक्तं गौण्यर्थं मुख्यसंज्ञाप्रदम् इति विधानम्।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
