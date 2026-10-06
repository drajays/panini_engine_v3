"""
1.1.53  ङिच्च  —  PARIBHASHA

Śāstra intent (paired with **1.1.52** *alo ’ntyasya*):
  When an ādeśa bears the anubandha **ङ्** (*ṅit* / “ṅic”), the “antya-only
  replacement” intent is explicit even if the ādeśa string has multiple letters.

Engine policy (glass-box infrastructure):
  - This sūtra does **not** mutate forms.
  - It registers a gate in ``state.paribhasha_gates`` that downstream vidhis
    may consult when they implement ādeśa targeting for *ṅit* markers.

CONSTITUTION Art. 2/4: no paradigm coordinates; full anuvṛtti is baked into
``text_*``; runtime only stores the gate.
Pāṭha: ashtadhyayi.com data.txt row i=11053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State


_GATE_KEY = "1.1.53_Gic_ca"


def cond(state: State) -> bool:
    return _GATE_KEY not in state.paribhasha_gates


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = {
        "mode": "antya_even_for_multiletter_adesha_when_Gic",
        "why": "ङिच्च — ङित्-आदेशे बह्वक्षरत्वेऽपि अन्त्यादेश-नियमः।",
    }
    return state


SUTRA = SutraRecord(
    sutra_id       = "1.1.53",
    sutra_type     = SutraType.PARIBHASHA,
    text_slp1      = 'Nicca',
    text_dev       = 'ङिच्च',
    samagra_slp1   = "Nit antyasya alaH",
    samagra_dev    = "ङित् अन्त्यस्य अलः",
    padaccheda_dev = "ङिच् / च",
    why_dev        = "परिभाषा-गेट: ङित्-आदेशे (बह्वक्षरत्वेऽपि) अन्त्यादेश-नियमः।",
    anuvritti_from = ("1.1.52",),
    cond           = cond,
    act            = act,
)

register_sutra(SUTRA)

