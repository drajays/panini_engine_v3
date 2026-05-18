"""
1.2.35  उच्चैस्तरां वा वषट्कारः  (uccaistarāṃ vā vaṣaṭkāraḥ)  —  VIBHASHA

Meaning: The vaṣaṭkāra — the ritual Vedic exclamation "vaṣaṭ!" uttered by
the hotṛ priest at the moment of oblation — is optionally (vā) pronounced
even higher (uccaistarāṃ, comparative of uccaiḥ) than the ordinary udātta
pitch. This sūtra grants an optional super-udātta elevation specifically for
the vaṣaṭkāra in ritual recitation.

Anuvṛtti: The accent-saṃjñā framework from 1.2.29 (udātta = uccaiḥ) carries
forward; uccaistarāṃ is the comparative that surpasses that baseline.

Scope: VIBHASHA (vibhasha_default=True — the elevation applies by default
when this path is chosen) — registers the gate
``"1_2_35_vaza_wikAra_vibhASA"`` in both ``samjna_registry`` and
``paribhasha_gates``.

What this rule does NOT do: It does not mutate any surface form. It does not
assign accent to any specific word. That assignment belongs to vidhi sūtras.

Blindness:
  - cond() reads only ``state.samjna_registry`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_35_vaza_wikAra_vibhASA"


def cond(state: State) -> bool:
    """Idempotent guard — fire only if vaṣaṭkāra-vibhāṣā is not yet registered."""
    return state.samjna_registry.get(_GATE_KEY) is not True


def act(state: State) -> State:
    """Register the vaṣaṭkāra optional higher-accent gate."""
    state.samjna_registry[_GATE_KEY] = True
    state.paribhasha_gates[_GATE_KEY] = True
    return state


_WHY_DEV = (
    "वषट्कारः (यज्ञे 'वषट्' इति उच्चारणम्) उच्चैस्तराम् — "
    "उदात्तादपि उच्चतरः — वा (विकल्पेन) उच्चार्यते। "
    "इयं विभाषा वैदिक-यज्ञ-प्रसङ्गे वषट्काराय अतिरिक्त-उत्स्वरणम् "
    "विकल्पेन अनुजानाति।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.35",
    sutra_type              = SutraType.VIBHASHA,
    r1_form_identity_exempt = True,
    vibhasha_default        = True,
    text_slp1               = "uccEstarAM vA vazawkAraH",
    text_dev                = "उच्चैस्तरां वा वषट्कारः",
    padaccheda_dev          = "उच्चैस्तराम् / वा / वषट्कारः",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.29",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
