"""
pipelines/yasAMsi_jas_shi_num_demo.py — यशांसि (yasAMsi) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/यशांसि.md`
Target SLP1: **yasAMsi**
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_yasAMsi() -> State:
    stem = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("yasas"),
        tags={"anga", "prātipadika", "napuṃsaka"},
        meta={"upadesha_slp1": "yasas"},
    )
    s = State(terms=[stem], meta={"linga": "napuṃsaka", "vibhakti_vacana": "1-3"}, trace=[])

    s = apply_rule("4.1.2", s)   # jas
    s = apply_rule("7.1.20", s)  # jas -> Si
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.9", s)   # S-lopa -> i
    s = apply_rule("1.1.42", s)  # sarvanamasthana
    s = apply_rule("7.1.72", s)  # num: append n
    s = apply_rule("6.4.10", s)  # a -> A before n+s

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.24", s)  # n -> M before s
    return s


__all__ = ["derive_yasAMsi"]

