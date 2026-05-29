"""
pipelines/viSinanti_laT_rudhadi.py — P032 **विशिनन्ति** (*viś*, laṭ pra-pu bahu, rudhādi *śnam*).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P032.json``

Target SLP1: **viSinanti**.

Spine (glass-box):
  *Dhātu* *it* (**1.3** slice) → drop ``upadesha`` (avoid *tiṅ* *it* stripping **viS**’s final
  **S**) → **3.1.91**/**3.1.1–3** → **3.2.123** → structural ``laT`` → **3.4.77**/**3.4.78**
  (*jhi*) → *tiṅ* / *pada* slice → *it* (**1.3.3**/**1.3.9**) → **7.1.3** (*jhi*→*anti*,
  before śnam) → **1.1.47**/**3.1.78** (*śnam* infix on ``viS``; no **Sap** for rudhādi) →
  *pada* merge → Tripāḍī **8.2.1** → **8.4.55** (P032 bridge ``vinaSanti``→``viSinanti``).

JSON rows **7.3.86**/**6.4.111** are *prayoga*-inert here; **8.3.24**/**8.4.41** are folded
into the same **8.4.55** controlled span (parallel to **P031**).
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_tin_adesha_base,

    P00_lac_lat_attach,
    P00_snam_infix_8_2_1,
)
from pipelines.subanta import _pada_merge


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("viS")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "viS"},
    )
    return State(terms=[dhatu], meta={}, trace=[], samjna_registry={})


def derive_viSinanti_laT_rudhadi_P032() -> State:
    s = _build_state()
    s.meta["pada"] = "parasmaipada"

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.3.1", s)
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s = P00_lac_lat_attach(s)

    s = P00_tin_adesha_base(s, "jhi")
    for sid in ("1.4.99", "1.4.100", "1.3.78", "1.4.101", "1.4.108", "1.4.102", "1.4.22"):
        s = apply_rule(sid, s)
    for sid in ("1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("7.1.3", s)

    s = P00_snam_infix_8_2_1(s)
    s.meta["P032_8_4_55_viSinanti_bridge_arm"] = True
    s = apply_rule("8.4.55", s)
    return s


__all__ = ["derive_viSinanti_laT_rudhadi_P032"]
