"""
pipelines/ye_yad_jas.py — यद् + जस् → ये (prathamā bahu, tyadādi path).

``prakriya_16``-style spine (user JSON had some OCR noise: **1.1.20** / **1.2.20**
are not this *prayoga*; **6.1.84** must precede **6.1.97** / **6.1.87**).

Operational ``apply_rule`` order:
  **6.4.1** → **3.1.4** → **7.2.102** → **6.1.84** → **6.1.97** → **7.1.17** →
  **1.3.7** → **1.3.9** → **6.1.87** → **8.2.1** → **8.2.5** (accent *saṃjñā* on tape-less model).
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_jas_7_1_17_it_lopa_6_1_87
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_yad_anga() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yad")),
        tags={"anga", "prātipadika", "sarvanama", "tyadadi"},
        meta={"upadesha_slp1": "yad"},
    )


def _mk_jas_sup() -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("jas")),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "jas"},
    )


def derive_ye_yad_jas() -> State:
    s = State(terms=[_mk_yad_anga(), _mk_jas_sup()])
    s = apply_rule("6.4.1", s)
    s = apply_rule("3.1.4", s)
    s = apply_rule("7.2.102", s)
    s = apply_rule("6.1.84", s)
    s = apply_rule("6.1.97", s)
    s = P00_jas_7_1_17_it_lopa_6_1_87(s)
    s = apply_rule("8.2.1", s)
    s.meta["ye_yad_jas_recipe"] = True
    s = apply_rule("8.2.5", s)
    return s


__all__ = ["derive_ye_yad_jas"]
