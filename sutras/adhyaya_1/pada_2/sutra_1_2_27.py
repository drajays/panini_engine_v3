"""
1.2.27  ऊकालोऽज्झ्रस्वदीर्घप्लुतः  (ūkālo'j jhrasvadīrghaplutaḥ)  —  SAMJNA

Full parsing: "ūkālaḥ — ac — hrasva-dīrgha-plutaḥ"

Meaning: A vowel (ac) is characterised by three durations (kāla = unit of
time), enumerated as: hrasva (short, 1 mātrā), dīrgha (long, 2 mātrā), and
pluta (prolated, 3 mātrā). The marker "u" from the technical term "ūkāla"
signals this tripartite timing scheme.

Scope: Universal SAMJNA — registers the three-fold vowel-duration
classification into samjna_registry so that subsequent phonological rules
(guṇa, vṛddhi, sandhi, etc.) can consult whether a vowel is hrasva, dīrgha,
or pluta.

What this rule does NOT do: It does not alter any vowel in any pada. It
only fixes the definiendum — which SLP1 characters count as hrasva, which as
dīrgha, and the pluta marker (context-dependent, assigned by vidhi sūtras).

SLP1 vowel inventory:
  Short (hrasva): a i u f x
  Long  (dīrgha): A I U F X e o E O
    (e and o are inherently long in Sanskrit phonology; E = ai, O = au)
  Pluta: registered as boolean True; actual 3-mātrā marking is assigned
         contextually by later vidhi sūtras.
"""
from __future__ import annotations

from typing import FrozenSet

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

# ── Module-level frozensets (CONSTITUTION Art. 5) ───────────────────────────
HRASVA_SLP1: FrozenSet[str] = frozenset({"a", "i", "u", "f", "x"})
DIRGHA_SLP1: FrozenSet[str] = frozenset({"A", "I", "U", "F", "X", "e", "E", "o", "O"})
PLUTA: str = "pluta"   # marker; actual prolation is context-dependent


def cond(state: State) -> bool:
    """Idempotent guard — fire only if the registry is not yet populated."""
    return state.samjna_registry.get("hrasva") != HRASVA_SLP1


def act(state: State) -> State:
    """Register hrasva / dīrgha / pluta classifications. No varṇa mutation."""
    state.samjna_registry["hrasva"] = HRASVA_SLP1
    state.samjna_registry["dIrgha"] = DIRGHA_SLP1
    state.samjna_registry["pluta"]  = True
    return state


_WHY_DEV = (
    "अच् (स्वर) त्रिकालः — ह्रस्वः (१ मात्रा), दीर्घः (२ मात्रे), प्लुतः (३ मात्राः)। "
    "ऊकाल इत्यत्र 'उ' कालस्य सूचकः। "
    "इयं संज्ञा वर्णानां मात्रा-वर्गीकरणं करोति; पदेषु परिवर्तनं न।"
)

SUTRA = SutraRecord(
    sutra_id                = "1.2.27",
    sutra_type              = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1               = "UkAlo'j JrasvadIrgaplutaH",
    text_dev                = "ऊकालोऽज्झ्रस्वदीर्घप्लुतः",
    padaccheda_dev          = "ऊकालः अच् ह्रस्व-दीर्घ-प्लुतः",
    why_dev                 = _WHY_DEV,
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA", "HRASVA_SLP1", "DIRGHA_SLP1", "PLUTA"]
