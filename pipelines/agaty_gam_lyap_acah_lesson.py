"""
pipelines/agaty_gam_lyap_acah_lesson.py — दलकृत्यम्: **1.1.57** *acaḥ* vs *hal* lopa.

Prakriyā (आ + गमॢँ + क्त्वा → **आगत्य**):
  गमॢँ (dhātupāṭha 01.1137) → it-lopa → गम् → **3.4.21** क्त्वा → **7.1.37** ल्यप्
  → **6.4.38** वा ल्यपि (dhātu-final म्-लोप) → it-लोप → **6.1.71** तुक् (लुप्त म् is a
  hal, so **1.1.57** gives no sthānivadbhāva) → *pada* merge.

Target SLP1: **Agatya** (आगत्य).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_dhatu_upadesha_it_lopa, P00_lyap_krt
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.krdanta import build_dhatu_state


def _upasarga_a() -> Term:
    return Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence("A")),
        tags={"upasarga"},
        meta={"upadesha_slp1": "A"},
    )


def derive_agaty_gam_lyap_acah_lesson() -> State:
    s = build_dhatu_state("gamx~")
    s.terms = [_upasarga_a()] + s.terms
    s = P00_dhatu_upadesha_it_lopa(s)           # गमॢँ → गम्

    s = P00_lyap_krt(s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_agaty_gam_lyap_acah_lesson"]
