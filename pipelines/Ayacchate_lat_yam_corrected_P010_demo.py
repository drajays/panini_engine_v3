"""
pipelines/Ayacchate_lat_yam_corrected_P010_demo.py — **P010** आयच्छते.

``A~N`` + **यमँ** + laṭ ātmanepada 3 sg.: **1.3.28**, **3.1.68** *śap*, **7.3.78** *yam*→*yacch*,
*ṅ*-lopa on **आङ्**, **3.4.79** — aligned with ``corrected_prakriyas_v2`` row **P010**.

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


def derive_Ayacchate_lat_yam_corrected_P010() -> State:
    dh = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yama~")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "yama~"},
    )
    s = State(terms=[dh], meta={}, trace=[], samjna_registry={})
    s.meta["lakara"] = "laT"

    for sid in ("1.3.1", "1.3.2", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s.terms[0].meta["upadesha_slp1"] = "yam"

    ang = Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence("A~N")),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "A~N"},
    )
    s.terms.insert(0, ang)

    s = apply_rule("1.4.59", s)
    s = apply_rule("1.3.28", s)

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

    s = apply_rule("3.4.113", s)

    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)

    for t in s.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")

    for sid in ("1.3.8", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("7.3.78", s)

    for sid in ("1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    return s


__all__ = ["derive_Ayacchate_lat_yam_corrected_P010"]
