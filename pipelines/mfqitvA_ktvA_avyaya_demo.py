"""
pipelines/mfqitvA_ktvA_avyaya_demo.py — मृडित्वा (mfqitvA) glass-box demo.

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_06_2026-04-29_14_06_31.json`

Target SLP1: **mfqitvA**

Narrow spine:
  mfq + (tvA <- ktvA) + iṭ (7.2.35) → mfqitvA
  1.2.7 marks ktvā as kṅit-locus (kitvat) for guṇa-block intent
  1.1.40 avyaya → 2.4.82 sup-luk.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_mfqitvA() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mfq"),
        tags={"dhatu", "anga", "prātipadika"},
        meta={"upadesha_slp1": "mfq"},
    )
    # Model ktvā surface as `tvA` with ancestry marker.
    tvA = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("tvA"),
        tags={"pratyaya", "krt", "ardhadhatuka"},
        meta={"upadesha_slp1": "tvA", "upadesha_slp1_original": "ktvA"},
    )
    s = State(terms=[dhatu, tvA], meta={}, trace=[])

    # iṭ on ārdhadhātuka val-ādi kṛt (tvA starts with t).
    s = apply_rule("7.2.35", s)

    # kitvat (kṅit-locus) marker for this ktvā (special paribhāṣā).
    s = apply_rule("1.2.7", s)
    s = apply_rule("1.1.5", s)

    # Add sup to show avyaya→sup-luk.
    sup = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("s~"),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "s~"},
    )
    s.terms.append(sup)

    # avyaya + sup-luk
    s = apply_rule("1.1.40", s)
    s = apply_rule("2.4.82", s)
    return s


__all__ = ["derive_mfqitvA"]

