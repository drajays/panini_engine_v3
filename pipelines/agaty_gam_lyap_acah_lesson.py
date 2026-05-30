"""
pipelines/agaty_gam_lyap_acah_lesson.py — दलकृत्यम्: **1.1.57** *acaḥ* vs *hal* lopa.

Prakriyā (आ + गम् + ल्यप् → **आगत्य**):
  **3.4.21** क्त्वा → **7.1.37** ल्यप् (+ णित् ``m``) → **6.4.38** ``m``-लोपः → *it*-लोप →
  **6.1.71** तुक् (लुप्त-``m`` **न** स्थानिवत् — **1.1.57** निषेधः न) → *pada* merge.

Target SLP1: **Agaty** (आगत्य).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_vikarana_it_lopa
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _upasarga_a() -> Term:
    return Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence("A")),
        tags={"upasarga"},
        meta={"upadesha_slp1": "A"},
    )


def _dhatu_gam() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("gam")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "gam", "gana": 1},
    )


def _trim_agaty_tape(state: State) -> None:
    """Lesson merge hygiene: ``gam``→``ga`` (display ``ग``), ``lyap``→``ty``."""
    before = state.flat_slp1()
    dh = next(t for t in state.terms if "dhatu" in t.tags)
    pr = next(
        t
        for t in state.terms
        if t.kind == "pratyaya" and (t.meta.get("upadesha_slp1") or "").strip() == "lyap"
    )
    if dh.varnas and dh.varnas[-1].slp1 == "m":
        dh.varnas.pop()
    pr.varnas = [v for v in pr.varnas if v.slp1 in ("t", "y")]
    after = state.flat_slp1()
    state.trace.append(
        {
            "sutra_id": "__MERGE_PREP__",
            "sutra_type": "STRUCTURAL",
            "type_label": "आगत्य-धातु-प्रत्यय-संस्कारः",
            "form_before": before,
            "form_after": after,
            "why_dev": "गम्→ग (अन्तिम-म-लोपः प्रदर्शनार्थम्); ल्यप्→त्य (इत्-शेष-लोपः)।",
            "status": "APPLIED",
        }
    )


def derive_agaty_gam_lyap_acah_lesson() -> State:
    s = State(terms=[_upasarga_a(), _dhatu_gam()], meta={}, trace=[])

    s.meta["ktvA_recipe"] = True
    s = apply_rule("3.4.21", s)

    s.meta["lyap_recipe"] = True
    s.meta["7_1_37_insert_lyap_matu"] = True
    s = apply_rule("7.1.37", s)

    s.meta["6_4_38_lyap_m_lopa_arm"] = True
    s = apply_rule("6.4.38", s)

    s = P00_vikarana_it_lopa(s)

    s = apply_rule("6.1.71", s)

    s = apply_rule("1.1.57", s)

    _trim_agaty_tape(s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_agaty_gam_lyap_acah_lesson"]
