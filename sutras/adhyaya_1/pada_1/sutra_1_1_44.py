"""
1.1.44  न वेति विभाषा  —  PARIBHASHA

Operational role (v3):
  - Registers the meta-paribhāṣā gate that governs vibhāṣā (optionality).
  - Whenever the words "na" or "vā" appear in a sūtra text, that sūtra
    is to be treated as optional (vibhāṣā).
  - In the engine, vibhāṣā is handled by SutraType.VIBHASHA on specific
    sūtras; this paribhāṣā registers the interpretive gate.

Blindness:
  - cond() reads only state.paribhasha_gates — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_1_44_na_veti"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id            = "1.1.44",
    sutra_type          = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1           = "na veti viBASA",
    text_dev            = "न वेति विभाषा",
    padaccheda_dev      = "न / वा / इति / विभाषा",
    why_dev             = "\"न\" \"वा\" इति शब्दौ यत्र सूत्रे स्तः तत् सूत्रं विभाषार्थं — विकल्पेन प्रवर्तते।",
    anuvritti_from      = (),
    cond                = cond,
    act                 = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
