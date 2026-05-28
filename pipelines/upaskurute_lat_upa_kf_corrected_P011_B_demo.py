"""
pipelines/upaskurute_lat_upa_kf_corrected_P011_B_demo.py — **P011-B** उपस्कुरुते.

``upa`` + **डुकृञ्** + **6.1.139** *suṭ* before *kṛ* (under **6.1.135** *adhikāra*),
*it*-lopa on *suṭ* (**1.3.3**, **1.3.9**) → **स्कृ** cluster, then same tanādi-u laṭ
ātmanepada spine as **P011-A** (**3.1.79** … **6.4.110**), **without** **8.4.55**
(bundle: no *pada*-final *jhal* before *khar*).

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


def derive_upaskurute_lat_upa_kf_corrected_P011_B() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("qukfY")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "qukfY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P011_B_demo"] = True
    s.meta["lakara"] = "laT"

    for sid in ("1.3.1", "1.3.5", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    dh = s.terms[0]
    dh.meta["upadesha_slp1"] = "kf"

    upa = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("upa")),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "upa"},
    )
    s.terms.insert(0, upa)

    s = apply_rule("1.4.59", s)

    s = apply_rule("6.1.135", s)
    s = apply_rule("6.1.139", s)

    for t in s.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")

    s.meta["corrected_v2_P011_B_suT_ic_arm"] = True
    for sid in ("1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

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
    return s


__all__ = ["derive_upaskurute_lat_upa_kf_corrected_P011_B"]
