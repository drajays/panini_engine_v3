"""
1.2.36  विभाषा छन्दसि  (vibhāṣā chandasi)  —  VIBHASHA

Meaning: [These accent rules apply] optionally (vibhāṣā) in Vedic / chandas
usage. This is a meta-vibhāṣā: it makes the preceding accent-assignment
rules (including the vaṣaṭkāra elevation of 1.2.35 and the ekaśruti
definition of 1.2.33) optional specifically within the Vedic context.
In other words, chandas-domain accent operations governed by this region are
not mandatory — they may or may not apply in a given derivation.

Anuvṛtti: The accent-saṃjñā framework from 1.2.29 (udātta) carries forward
as the base against which "chandasi" optionality is measured.

Scope: VIBHASHA (vibhasha_default=True — the optional gate is active by
default) — sets the gate ``"1_2_36_vibhASA_chandasi"`` in both
``paribhasha_gates`` and ``samjna_registry``.

What this rule does NOT do: It does not mutate any surface form. It does not
assign accent to any word. That belongs to vidhi sūtras.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_36_vibhASA_chandasi"


def cond(state: State) -> bool:
    """Idempotent guard — fire only if the chandasi-vibhāṣā gate is not yet set."""
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    """Set the chandasi-vibhāṣā interpretive gate."""
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


_WHY_DEV = (
    "छन्दसि (वेदे) पूर्वोक्ताः स्वर-विधयः विभाषया — विकल्पेन — प्रवर्तन्ते। "
    "इयं मेटा-विभाषा वैदिक-प्रसङ्गे स्वर-नियमानाम् ऐच्छिकत्वं घोषयति। "
    "अतः छन्दः-सन्दर्भे स्वर-प्रयोगः अनिवार्यः न — विकल्पाधीनः।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.36",
    sutra_type              = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    vibhasha_default        = True,
    text_slp1               = "vibASA Candasi",
    text_dev                = "विभाषा छन्दसि",
    padaccheda_dev          = "विभाषा / छन्दसि",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.29",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
