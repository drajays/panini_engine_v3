"""
1.2.69  नपुंसकमनपुंसकेनैकवच्चास्यान्यतरस्याम्  —  VIBHASHA (SAMJNA gate)

*Padaccheda:* **नपुंसकम्** / **अनपुंसकेन** / **एकवत्** / **च** / **अस्य** / **अन्यतरस्याम्**

A neuter (napuṃsaka) [word] paired with a non-neuter (anapuṃsaka) word —
optionally (anyatarasyām) the neuter form acts as singular (ekavat).  In
ekasheṣa, when a neuter and a non-neuter are paired, the neuter form
optionally survives and is treated as singular.

This is an optional extension of the ekasheṣa principle of 1.2.64,
specifically governing gender-mismatched pairs where one member is neuter.

Operational role (v3):
  - Registers the gate ``1_2_69_napuMsaka_anapuMsaka`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when determining whether a
    neuter–non-neuter pair may optionally use the neuter ekasheṣa form.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_69_napuMsaka_anapuMsaka"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.69",
    sutra_type              = SutraType.VIBHASHA,
    vibhasha_default        = True,
    r1_form_identity_exempt = True,
    text_slp1               = "napuMsakam anapuMsakena ekavac cAsyAnyatarasyAm",
    text_dev                = "नपुंसकमनपुंसकेनैकवच्चास्यान्यतरस्याम्",
    padaccheda_dev          = "नपुंसकम् / अनपुंसकेन / एकवत् / च / अस्य / अन्यतरस्याम्",
    why_dev                 = (
        "नपुंसकस्य अनपुंसकेन सह एकशेषे नपुंसकं रूपम् अन्यतरस्याम् एकवद् भवति — "
        "नपुंसक-अनपुंसक-युगले एकशेष-विकल्पे नपुंसकम् एकवचनवत् प्रयुज्यते।"
    ),
    anuvritti_from          = ("1.2.64",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
