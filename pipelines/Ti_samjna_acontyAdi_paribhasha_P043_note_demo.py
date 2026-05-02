"""
pipelines/Ti_samjna_acontyAdi_paribhasha_P043_note_demo.py — **P043** ṭi-saṃjñā note demo.

Source: ``…/my_scripts/final/split_prakriyas_11/P043.json``.

Paribhāṣā **1.1.64** *aco ’ntyādi ṭi* (illustration): the ``ṭi`` portion of a
string is taken from the **last** ``ac`` onward — e.g. ``paceyAtAm`` → ``Am``,
``agnicit`` → ``it``, ``somasut`` → ``ut`` (SLP1 tape).

**1.1.68** frames the topic (*svaṃ rūpaṃ …*) as in the JSON INPUT step.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_Ti_samjna_acontyAdi_paribhasha_P043_note() -> State:
    terms = [
        Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("paceyAtAm")),
            tags={"anga", "prātipadika", "prakriya_P043_illustration"},
            meta={"prakriya_P043_word": "paceyAtAm", "upadesha_slp1": "paceyAtAm"},
        ),
        Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("agnicit")),
            tags={"anga", "prātipadika", "prakriya_P043_illustration"},
            meta={"prakriya_P043_word": "agnicit", "upadesha_slp1": "agnicit"},
        ),
        Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence("somasut")),
            tags={"anga", "prātipadika", "prakriya_P043_illustration"},
            meta={"prakriya_P043_word": "somasut", "upadesha_slp1": "somasut"},
        ),
    ]
    s = State(terms=terms, meta={}, trace=[])
    s.meta["prakriya_P043_paribhasha_note_only"] = True
    s.meta["P043_1_1_64_queue"] = [
        "definition",
        "paceyAtAm",
        "agnicit",
        "somasut",
        "siddhi",
    ]
    s = apply_rule("1.1.68", s)
    for _ in range(5):
        s = apply_rule("1.1.64", s)
    return s


__all__ = ["derive_Ti_samjna_acontyAdi_paribhasha_P043_note"]
