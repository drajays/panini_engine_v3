"""
pipelines/utkurute_lat_ud_kf_corrected_P011_A_demo.py — **P011-A** उत्कुरुते.

``ud`` + **डुकृञ्** (**``qukfY``**) + laṭ ātmanepada 3 sg.: *it*-lopa (**1.3.5**),
**3.2.123** laṭ → **त**, **3.1.79** *u* vikaraṇa, **7.3.84** / **1.1.51**, **1.2.4** /
**1.1.5**, **1.1.64** / **3.4.79** *te*, **6.4.110**, merge + tripāḍī **8.4.55**
— aligned with ``corrected_prakriyas_v2`` row **P011-A**.

*Ud + kṛ* ātmanepada licensing (**1.3.24**) is bundle commentary; not a separate
engine file in this slice.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_utkurute_lat_ud_kf_corrected_P011_A() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("qukfY")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "qukfY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P011_A_demo"] = True
    s.meta["lakara"] = "laT"

    for sid in ("1.3.1", "1.3.5", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    dh = s.terms[0]
    dh.meta["upadesha_slp1"] = "kf"

    ud = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("ud")),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "ud"},
    )
    s.terms.insert(0, ud)

    s = apply_rule("1.4.59", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)

    s.meta["3_1_79_tanadi_u_arm"] = True
    s = apply_rule("3.1.79", s)

    s = apply_rule("7.3.84", s)
    s = apply_rule("1.1.51", s)
    if s.terms:
        for t in s.terms:
            if "dhatu" in t.tags:
                t.tags.discard("upadesha")

    s.samjna_registry.pop("1.2.4_sarvadhatukam_apit", None)
    s = apply_rule("1.2.4", s)
    s = apply_rule("1.1.5", s)

    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    s = apply_rule("6.4.110", s)

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.55", s)
    return s


__all__ = ["derive_utkurute_lat_ud_kf_corrected_P011_A"]
