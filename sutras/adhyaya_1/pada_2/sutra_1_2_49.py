"""
1.2.49  लुक् तद्धितलुकि  —  PARIBHASHA (NIYAMA)

*Padaccheda:* **लुक्** / **तद्धितलुकि**

When *luk* (zero-elision) of a *taddhita* suffix occurs, [the prior
operation that required that taddhita] also undergoes *luk* — the luk-chain
propagates back through the taddhita derivation.

Operational role (v3):
  - Registers the gate ``1_2_49_luk_tadDitaluki`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream recipes for taddhita-luk contexts check this gate to
    determine whether the full luk-chain should propagate.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_49_luk_tadDitaluki"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.49",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "luk tadDitaluki",
    text_dev                = "लुक् तद्धितलुकि",
    padaccheda_dev          = "लुक् / तद्धितलुकि",
    why_dev                 = (
        "तद्धितप्रत्ययस्य लुकि जाते पूर्वस्य लुक्-श्रृङ्खलापि प्रवर्तते "
        "— तद्धितलुक्-प्रसङ्गे लुग्-अनुवर्तनं सिद्ध्यति।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
