"""
1.2.73  ग्राम्यपशुसंघेष्वतरुणेषु स्त्री  —  VIDHI (SAMJNA gate)

*Padaccheda:* **ग्राम्य-पशु-संघेषु** / **अतरुणेषु** / **स्त्री**

For domestic animals (grāmya-paśu) appearing in groups (saṃgha), when
they are not young/calf-stage (atarṇeṣu — not tarṇa, i.e., adult), the
feminine form (strī) survives as the ekasheṣa remainder.  This is an
exception to the general ekasheṣa rule (1.2.64) where masculine would
normally survive; here the feminine prevails for adult domestic livestock
in collective contexts.

Anuvritti from 1.2.64 supplies the ekasheṣa framework within which this
special feminine-survival rule operates.

Operational role (v3):
  - Registers the gate ``1_2_73_grAmyapazu_strI`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - Downstream rules consult this gate when processing adult domestic
    animal pairs in ekasheṣa to select the feminine form.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_73_grAmyapazu_strI"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.73",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "grAmyapazusaMGezv ataruRezv strI",
    text_dev                = "ग्राम्यपशुसंघेष्वतरुणेषु स्त्री",
    padaccheda_dev          = "ग्राम्य-पशु-संघेषु / अतरुणेषु / स्त्री",
    why_dev                 = (
        "ग्राम्यपशूनां संघे अतरुणेषु एकशेषे स्त्रीशब्द एव शिष्यते — "
        "प्रौढ-ग्राम्यपशु-समूहे एकशेषे स्त्रीलिङ्गस्य ग्रहणम् इति विशेष-विधिः।"
    ),
    anuvritti_from          = ("1.2.64",),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
