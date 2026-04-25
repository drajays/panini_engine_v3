"""
1.1.54  आदेशः परस्य  —  PARIBHASHA

Interpretive gate: when a later rule speaks of an “ādi/ādeśa” substitution,
the substitution is understood to apply to the **following** element (*para*),
not to the cause (*nimitta*) itself.

Engine policy:
  - No form mutation here.
  - Only enables a gate in ``state.paribhasha_gates``; operational sūtras may
    consult it when deciding whether to rewrite the next term/varna boundary.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1.1.54_adesh_parasya"


def cond(state: State) -> bool:
    return _GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = {
        "mode": "parasya",
        "why": "आदेशः परस्य — आदेश-प्रसङ्गे पर-ग्रहणम्।",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.54",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = "AdeH parasya",
    text_dev       = "आदेशः परस्य",
    padaccheda_dev = "आदेशः / परस्य",
    why_dev        = "परिभाषा-गेट: आदेश-नियोजनम् पर-स्थाने।",
    anuvritti_from = ("1.1.49",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

