"""
pipelines/pfzwvA_pracch_ktvA_demo.py — पृष्ट्वा (pfzwvA) glass-box demo.

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_08_2026-04-29_14_06_46.json`

Target SLP1: **pfzwvA**

Narrow spine implemented:
  pfcC + ktvA (kitvat via 1.2.8) →
  samprasāraṇa r→f (1.1.45) + 6.1.108 (pūrvarūpa) →
  6.4.19: cC → S (before kṅiti) →
  8.2.36: S → z (recipe-armed) →
  8.4.41: t → w after z (z+t contact) →
  1.1.40 + 2.4.82: avyaya + sup-luk ghost.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from sutras.adhyaya_1.pada_1.sutra_1_1_45 import META_TARGETS


def derive_pfzwvA() -> State:
    dhatu = Term(
        kind="prakriti",
        # Use surface with explicit `r a` so 1.1.45 + 6.1.108 can act.
        varnas=parse_slp1_upadesha_sequence("pracC"),
        tags={"dhatu", "anga", "prātipadika"},
        meta={"upadesha_slp1": "pfcC"},
    )
    tvA = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("tvA"),
        tags={"pratyaya", "krt", "ardhadhatuka"},
        meta={"upadesha_slp1": "tvA", "upadesha_slp1_original": "ktvA"},
    )
    sup = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("s~"),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "s~"},
    )
    s = State(terms=[dhatu, tvA, sup], meta={}, trace=[])

    # iṭ prohibition signal (note mentions 7.2.10); keep it explicit & harmless.
    s.meta["ekac_dhatu"] = True
    s.meta["udatta_dhatu"] = False
    s = apply_rule("7.2.10", s)
    s = apply_rule("7.2.35", s)  # should be blocked/skipped

    # kitvat for ktvā after pracch.
    s = apply_rule("1.2.8", s)
    s = apply_rule("1.1.5", s)

    # samprasāraṇa r→f on dhātu and pūrvarūpa.
    for vi, v in enumerate(s.terms[0].varnas):
        if v.slp1 == "r":
            s.meta[META_TARGETS] = [(0, vi)]
            break
    s = apply_rule("1.1.45", s)
    s = apply_rule("6.1.108", s)

    # cch->ś then ś->ṣ then ṭutva.
    s = apply_rule("6.4.19", s)
    s.meta["8_2_36_sh_to_sh_arm"] = True
    s = apply_rule("8.2.36", s)
    # avyaya + sup-luk ghost (must happen while sup is a separate term).
    s = apply_rule("1.1.40", s)
    s = apply_rule("2.4.82", s)

    # Merge to a single pada so z+t become adjacent; then open tripāḍī.
    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.41", s)
    return s


__all__ = ["derive_pfzwvA"]

