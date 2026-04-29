"""
pipelines/uditvA_uzitvA_ktvA_samprasaraNa_demo.py

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_07_2026-04-29_14_06_37.json`

Targets (SLP1):
  - **uditvA**  (vad + ktvA, with samprasāraṇa v→u + 6.1.108)
  - **uzitvA**  (vas + ktvA, with samprasāraṇa v→u + 8.3.60 s→z)

Note: The JSON is low-confidence; this file implements the note’s intended
glass-box spine using the existing samprasāraṇa mapper (1.1.45) plus 6.1.108,
then the standard avyaya→sup-luk chain (1.1.40 → 2.4.82).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from sutras.adhyaya_1.pada_1.sutra_1_1_45 import META_TARGETS


def _ktvA_with_sup() -> Term:
    # Model ktvā surface as `itvA` with ancestry marker for 1.1.40.
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("itvA"),
        tags={"pratyaya", "krt", "ardhadhatuka"},
        meta={"upadesha_slp1": "itvA", "upadesha_slp1_original": "ktvA"},
    )


def _sup_su() -> Term:
    return Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("s~"),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "s~"},
    )


def _samprasaran_v_to_u_on_first_term(s: State) -> State:
    # Find `v` in the primary dhātu and mark as samprasāraṇa target.
    if not s.terms:
        return s
    dh = s.terms[0]
    for vi, v in enumerate(dh.varnas):
        if v.slp1 == "v":
            s.meta[META_TARGETS] = [(0, vi)]
            break
    s = apply_rule("1.1.45", s)
    return s


def derive_uditvA() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("vad"),
        tags={"dhatu", "anga", "prātipadika"},
        meta={"upadesha_slp1": "vad"},
    )
    s = State(terms=[dhatu, _ktvA_with_sup(), _sup_su()], meta={}, trace=[])
    s = _samprasaran_v_to_u_on_first_term(s)
    s = apply_rule("6.1.108", s)
    s = apply_rule("1.1.40", s)
    s = apply_rule("2.4.82", s)
    return s


def derive_uzitvA() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("vas"),
        tags={"dhatu", "anga", "prātipadika"},
        meta={"upadesha_slp1": "vas"},
    )
    s = State(terms=[dhatu, _ktvA_with_sup(), _sup_su()], meta={}, trace=[])
    s = _samprasaran_v_to_u_on_first_term(s)
    s = apply_rule("6.1.108", s)
    s.meta["8_3_60_shasi_vasi_ghasi_arm"] = True
    s = apply_rule("8.3.60", s)
    s = apply_rule("1.1.40", s)
    s = apply_rule("2.4.82", s)
    return s


__all__ = ["derive_uditvA", "derive_uzitvA"]

