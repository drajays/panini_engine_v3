"""
1.2.64  सरूपाणामेकशेष एकविभक्तौ  —  VIDHI (SAMJNA gate)

*Padaccheda:* **सरूपाणाम्** / **एकशेषः** / **एकविभक्तौ**

Of *sarūpa* (same-form / identical-sounding) words occurring in the same
*vibhakti* (case), only ONE remains (*ekaśeṣa* — single-remainder).
Example: two occurrences of *rāmaḥ* (nominative singular) become *rāmau*
(nominative dual) — the dual form represents both referents via the
single-remainder principle.

This is the primary *ekaśeṣa* sūtra; 1.2.52 and 1.2.45/46 region rules
provide restrictions and extensions that anuvartate from it.

Operational role (v3):
  - Registers the gate ``1_2_64_sarUpANAm_ekazeza`` in both
    ``paribhasha_gates`` and ``samjna_registry``.
  - The actual operation of removing duplicate terms and adjusting vacana
    is performed by the recipe that calls this rule.  This sūtra's act()
    only sets the gate that permits downstream ekaśeṣa processing.

Blindness:
  - cond() reads only ``state.paribhasha_gates`` — no vibhakti, vacana,
    lakāra, surface Devanāgarī, data, or reference access (Art. 2).
  - No arm flags; no paradigm coordinates.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY = "1_2_64_sarUpANAm_ekazeza"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(_GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY] = True
    return state


SUTRA = SutraRecord(
    sutra_id                = "1.2.64",
    sutra_type              = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1               = "sarUpARAm ekazeza ekaviBaktO",
    text_dev                = "सरूपाणामेकशेष एकविभक्तौ",
    padaccheda_dev          = "सरूपाणाम् / एकशेषः / एकविभक्तौ",
    why_dev                 = (
        "एकविभक्तौ सरूपाणां शब्दानाम् एकः एव शिष्यते — "
        "द्वौ रामौ एकवचनौ → रामौ (द्विवचनम्) इत्येकशेष-न्यायः।"
    ),
    anuvritti_from          = (),
    cond                    = cond,
    act                     = act,
)

register_sutra(SUTRA)

__all__ = ["SUTRA"]
