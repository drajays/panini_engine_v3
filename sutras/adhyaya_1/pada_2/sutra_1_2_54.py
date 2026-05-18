"""
1.2.54  लुब्योगाप्रख्यानात्  —  PARIBHASHA

*Padaccheda:* **लुप्** / **योग-अप्रख्यानात्**

Lup (elision of a suffix) does not cause the word to lose its original
nature/recognition (prakhyāna), because the connection (yoga) still applies.
A word whose suffix is elided by lup retains its original identity.

Operational role (v3):
  - Registers the gate ``1_2_54_lup_yogAprakhyAnAt`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when determining whether lup-elision
    strips a word of its identity or classification.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_54_lup_yogAprakhyAnAt"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.54",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "lup yogAprakhyAnAt",
    text_dev                = "लुब्योगाप्रख्यानात्",
    padaccheda_dev          = "लुप् / योग-अप्रख्यानात्",
    why_dev                 = (
        "लुपि कृते अपि योगसम्बन्धान्न प्रख्यानहानिः — "
        "लुप्-विधौ शब्दः स्वस्वरूपं न जहाति इति परिभाषा।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
