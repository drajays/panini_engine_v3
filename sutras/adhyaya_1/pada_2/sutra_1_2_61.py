"""
1.2.61  छन्दसि पुनर्वस्वोरेकवचनम्  —  VIDHI (SAMJNA gate)

*Padaccheda:* **छन्दसि** / **पुनर्वस्वोः** / **एकवचनम्**

In the Vedic/Chandas domain, for the nakṣatra "Punarvasu" (which
ordinarily appears in the dual), singular (ekavacana) is used.
This is a special Vedic grammatical rule governing the number of this
asterism name in the Vedic register.

Operational role (v3):
  - Registers the gate ``1_2_61_punarvasU_ekacanam`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream Chandas-context rules consult this gate when determining
    the vacana of "Punarvasu" in Vedic passages.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_61_punarvasU_ekacanam"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.61",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "Candasi punarvasvorekacanam",
    text_dev                = "छन्दसि पुनर्वस्वोरेकवचनम्",
    padaccheda_dev          = "छन्दसि / पुनर्वस्वोः / एकवचनम्",
    why_dev                 = (
        "छन्दसि विषये पुनर्वसु-नक्षत्रस्य द्विवचनस्थाने एकवचनं विधीयते — "
        "वैदिकप्रयोगे पुनर्वसोः एकवचनमेव साधु।"
    ),
    anuvritti_from          = ("1.2.60",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
