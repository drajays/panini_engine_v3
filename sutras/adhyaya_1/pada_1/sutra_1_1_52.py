"""
1.1.52  अलोऽन्त्यस्य  —  PARIBHASHA

Interpretive gate: when a later rule says “replace an *al*”, the **default**
target is the *antya* (last) sound of the relevant span.

Engine policy:
  - This sūtra does **not** mutate forms.
  - It only enables a gate in ``state.paribhasha_gates`` so VIDHIs that need
    “antya selection” can consult it (CONSTITUTION Art. 2).

This is a lightweight infrastructure paribhāṣā used for deterministic
selection; it does not override explicit index targeting in recipes.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1.1.52_alo_antyasya"


def cond(state: State) -> bool:
    return _GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = {
        "mode": "antya",
        "why": "अलोऽन्त्यस्य — अल्-आदेशे अन्त्य-अल्-ग्रहणम्।",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.52",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "alo antyasya",
    text_dev       = "अलोऽन्त्यस्य",
    padaccheda_dev = "अलः / अन्त्यस्य",
    why_dev        = "परिभाषा-गेट: अल्-आदेश-प्रसङ्गे अन्त्य-अल्-ग्रहणम्।",
    anuvritti_from = ("1.1.49",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

