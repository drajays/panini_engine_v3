"""
1.2.53  तदशिष्यं संज्ञाप्रमाणत्वात्  —  PARIBHASHA

*Padaccheda:* **तत्** / **अशिष्यम्** / **संज्ञा-प्रमाणत्वात्**

"That [rule] is not to be taught [again] because the saṃjñā [itself] is the
authority."  This paribhāṣā prevents redundant re-definition: once a saṃjñā
is established, it does not need to be re-stated.

Operational role (v3):
  - Registers the gate ``1_2_53_tad_aSizya`` in both ``paribhasha_gates``
    and ``samjna_registry``.
  - Downstream rules consult this gate to avoid redundant saṃjñā teaching.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_53_tad_aSizya"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.53",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "tad aSizyaM saMjYApramARatvAt",
    text_dev                = "तदशिष्यं संज्ञाप्रमाणत्वात्",
    padaccheda_dev          = "तत् / अशिष्यम् / संज्ञा-प्रमाणत्वात्",
    why_dev                 = (
        "संज्ञैव प्रमाणम् इति कृत्वा तस्य पुनः शासनम् अनावश्यकम् — "
        "एकदा निर्दिष्टायाः संज्ञायाः पुनर्विधानं न कर्तव्यम् इति परिभाषा।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
