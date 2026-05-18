"""
1.2.32  तस्यादित उदात्तमर्धह्रस्वम्  (tasyādita udāttam ardhahrsvam)  —  PARIBHASHA

Meaning: Of a pluta vowel (prolonged, 3-mātrā), the udātta portion occupies
the first half — ardha-hrasva (half short = 1.5 mātrā). This sūtra defines
the internal accent structure of pluta vowels: the udātta quality resides in
the initial half-short portion of the three-mātrā prolongation.

Anuvṛtti: The accent-saṃjñā framework from 1.2.29 (udātta) and 1.2.31
(svarita) carries forward — this rule refines how udātta is situated within
a pluta vowel.

Scope: PARIBHASHA — sets the interpretive gate
``1_2_32_pluta_udAtta_ardha`` in both ``paribhasha_gates`` and
``samjna_registry``. Downstream rules consulting pluta accent structure check
this gate.

What this rule does NOT do: It does not assign pluta or udātta to any vowel
in any word. That assignment belongs to vidhi sūtras.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_32_pluta_udAtta_ardha"


def cond(state: State) -> bool:
    """Idempotent guard — fire only if the pluta-udātta gate is not yet set."""
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    """Set the pluta-udātta-ardha gate. No varṇa mutation."""
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


_WHY_DEV = (
    "प्लुत-स्वरस्य (त्रिमात्रिकस्य) आदिभागे — अर्धह्रस्वे (१.५ मात्रायाम्) — "
    "उदात्त-गुणः तिष्ठति। इयं परिभाषा प्लुत-स्वरस्य आन्तरिक-उदात्त-विन्यासं "
    "निर्धारयति। परवर्तिषु सूत्रेषु 'प्लुत-उदात्त' इति पदं यत्रोपयुज्यते "
    "तत्र इयमेव व्याख्या।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.32",
    sutra_type              = SutraType.PARIBHASHA,
    r1_form_identity_exempt = True,
    text_slp1               = "tasyAdita udAttam ardDahrasvam",
    text_dev                = "तस्यादित उदात्तमर्धह्रस्वम्",
    padaccheda_dev          = "तस्य / आदितः / उदात्तम् / अर्धह्रस्वम्",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = ("1.2.29", "1.2.31"),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
