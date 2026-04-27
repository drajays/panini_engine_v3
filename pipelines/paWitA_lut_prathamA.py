"""
pipelines/paWitA_lut_prathamA.py — पठिता (*paṭha*, *luṭ*, prathama puruṣa, ekavacana).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/pathita.md``.

Target SLP1: **paWitA** (पठिता).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology    import mk
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P00_bhuvadi_dhatu_it_anunasik_hal, P00_tip_to_ti
from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from pipelines.subanta import _pada_merge


def _build_dhatu_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("paWa~"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "paWa~"},
    )
    return State(terms=[dhatu], meta={}, trace=[])


def derive_paWitA() -> State:
    s = _build_dhatu_state()
    s.meta["pada"] = "parasmaipada"

    s = P00_bhuvadi_dhatu_it_anunasik_hal(s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s = apply_rule("3.3.3", s)
    s.meta["3_3_15_lut_arm"] = True
    s = apply_rule("3.3.15", s)
    s.meta.pop("3_3_15_lut_arm", None)

    s.meta["3_1_33_tasi_lut_arm"] = True
    s = apply_rule("3.1.33", s)
    s.meta.pop("3_1_33_tasi_lut_arm", None)

    s = apply_rule("3.4.77", s)
    s = P00_tip_to_ti(s)

    s.meta["7_2_35_lut_tAsi_it_arm"] = True
    s = apply_rule("1.1.46", s)
    s = apply_rule("7.2.35", s)
    s.meta.pop("7_2_35_lut_tAsi_it_arm", None)

    s.meta["2_4_85_lut_prathama_arm"] = True
    s = apply_rule("2.4.85", s)
    s.meta.pop("2_4_85_lut_prathama_arm", None)

    if len(s.terms) >= 2:
        s.terms[-1].meta["dit_pratyaya"] = True

    s.meta["6_4_143_lut_tasi_arm"] = True
    s = apply_rule("6.4.143", s)
    s.meta.pop("6_4_143_lut_tasi_arm", None)

    # *ḍā* it-lopa: ``q`` (cuṭ) + ``A`` → ``A`` (residue).
    s.meta["1_3_7_lut_qA_arm"] = True
    for sid in ("1.3.7", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)
    s.meta.pop("1_3_7_lut_qA_arm", None)

    # Merge to ``paWit`` + ``A`` (``dit``) for **7.3.86** + **1.1.6** slice.
    all_v = []
    for t in s.terms[:-1]:
        all_v.extend(v.clone() for v in t.varnas)
    anga = Term(
        kind="prakriti",
        varnas=all_v,
        tags={"anga"},
        meta={"upadesha_slp1": "paWit"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=[v.clone() for v in s.terms[-1].varnas],
        tags={"pratyaya"},
        meta=dict(s.terms[-1].meta),
    )
    pr.meta["dit_pratyaya"] = True
    before = s.flat_slp1()
    s.terms = [anga, pr]
    after = s.flat_slp1()
    s.trace.append({
        "sutra_id": "__PATHITA_MERGE__",
        "sutra_type": "STRUCTURAL",
        "type_label": "पठिता-मेलनम्",
        "form_before": before,
        "form_after": after,
        "why_dev": "धातु+तास्-शेष+आ → अङ्ग + डित्-परः (संरचनात्मकं, न सूत्रम्)।",
        "status": "APPLIED",
    })

    s = apply_rule("1.1.6", s)
    s = apply_rule("7.3.86", s)

    s = apply_rule("1.4.14", s)
    _pada_merge(s)
    return s


__all__ = ["derive_paWitA"]
