"""
1.1.58  न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु  —  NIYAMA

Operational role (v3):
  - Registers a niyama (restriction) gate marking the operational contexts
    in which a prior anuvṛtti rule is blocked (asiddha).
  - The eight blocked contexts are:
      (1) padānta      — word-final operations
      (2) dvirvacana   — reduplication
      (3) vareya-lopa  — vareya elision
      (4) svara        — accent operations
      (5) savarṇa      — homogeneous (savarna) operations
      (6) anusvāra     — anusvāra insertion
      (7) dīrgha       — vowel lengthening
      (8) jaścara      — jhalām jaś-car operations
  - Registering this gate allows downstream rules to test whether they
    are in a blocked context before applying anuvṛtti.

Blindness:
  - cond() reads only state.paribhasha_gates — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_1_58_na_padAnta_etc"

# The eight operational contexts where the prior anuvṛtti is blocked.
_BLOCKED_CONTEXTS: frozenset = frozenset({
    "padAnta",
    "dvirvacana",
    "vareya_lopa",
    "svara",
    "savarNa",
    "anusvAra",
    "dIrgha",
    "jaScara",
})


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id            = "1.1.58",
    sutra_type          = SutraType.NIYAMA,
    r1_form_identity_exempt = True,
    text_slp1           = "na padAntadvirvacanavarey alopasvarasavarNAnusvAradIrgajaScarvidiSu",
    text_dev            = "न पदान्तद्विर्वचनवरेयलोपस्वरसवर्णानुस्वारदीर्घजश्चर्विधिषु",
    padaccheda_dev      = "न / पदान्त-द्विर्वचन-वरेय-लोप-स्वर-सवर्ण-अनुस्वार-दीर्घ-जश्चर्-विधिषु",
    why_dev             = "पदान्त-द्विर्वचन-वरेयलोप-स्वर-सवर्ण-अनुस्वार-दीर्घ-जश्चर्-विधिषु पूर्वसूत्रस्य अनुवृत्तिः न — एते प्रसङ्गाः असिद्धवत्।",
    anuvritti_from      = (),
    cond                = cond,
    act                 = act,
)

register_sutra(SUTRA)

__all__ = ["BLOCKED_CONTEXTS", "SUTRA"]
