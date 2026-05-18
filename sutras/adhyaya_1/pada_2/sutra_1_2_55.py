"""
1.2.55  योगप्रमाणे च तदभावेऽदर्शनं स्यात्  —  PARIBHASHA

*Padaccheda:* **योग-प्रमाणे** / **च** / **तत्-अभावे** / **अदर्शनम्** / **स्यात्**

"In the case where yoga (connection/rule) is the authority, if that connection
is absent, [the result/word] is not seen/manifested."  This paribhāṣā governs
rule-application absence: when the authority for a form is a yoga (a sūtra
connection), and that yoga is not present, the expected form does not appear.

Operational role (v3):
  - Registers the gate ``1_2_55_yogapramANe`` in both ``paribhasha_gates``
    and ``samjna_registry``.
  - Downstream rules consult this gate when determining whether absence of a
    connecting rule implies absence of the derived form.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_55_yogapramANe"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.55",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "yogapramARe ca tadaBAve'darzanaM syAt",
    text_dev                = "योगप्रमाणे च तदभावेऽदर्शनं स्यात्",
    padaccheda_dev          = "योग-प्रमाणे / च / तत्-अभावे / अदर्शनम् / स्यात्",
    why_dev                 = (
        "योगः प्रमाणं यस्य तस्मिन् विषये तस्य योगस्य अभावे रूपस्य अदर्शनम् — "
        "योगसम्बन्धाभावे प्रयोगो न दृश्यते इति परिभाषा।"
    ),
    anuvritti_from          = ("1.2.54",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
