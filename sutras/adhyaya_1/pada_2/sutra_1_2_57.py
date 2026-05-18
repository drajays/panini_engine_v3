"""
1.2.57  कालोपसर्जने च तुल्यम्  —  PARIBHASHA

*Padaccheda:* **काल-उपसर्जने** / **च** / **तुल्यम्**

"And [the rule applies] similarly when time (kāla) is the secondary element
(upasarjana)."  This paribhāṣā extends the preceding rule (1.2.56) to cases
where kāla (time) functions as the upasarjana (secondary/subordinate member):
the same principle of authority applies equally in such contexts.

Operational role (v3):
  - Registers the gate ``1_2_57_kAlopasarjane`` in both ``paribhasha_gates``
    and ``samjna_registry``.
  - Downstream rules consult this gate when processing compounds or
    expressions in which a time-element is subordinate (upasarjana).

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_57_kAlopasarjane"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.57",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "kAlopasarjane ca tulyam",
    text_dev                = "कालोपसर्जने च तुल्यम्",
    padaccheda_dev          = "काल-उपसर्जने / च / तुल्यम्",
    why_dev                 = (
        "यत्र कालः उपसर्जनं तत्रापि पूर्वसूत्रोक्तं तुल्यम् — "
        "कालोपसर्जनविषये च तदेव प्रमाणं प्रवर्तते इति परिभाषा।"
    ),
    anuvritti_from          = ("1.2.56",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
