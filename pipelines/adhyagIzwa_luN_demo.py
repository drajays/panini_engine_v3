"""
pipelines/adhyagIzwa_luN_demo.py — अध्यगीष्ट (aDhyagIzwa) glass-box demo.

Source: `/Users/dr.ajayshukla/my_scripts/final/1_2_fully_corrected_prakriya.json`
Entry: 2026-04-29 14:05:49 / 14:05:58.

Target SLP1: **aDhyagIzwa**

This is a narrow luṅ demo that exists to exercise:
  - 2.4.45 (iN → gAN in luṅ) + 1.2.1 atideśa
  - 6.4.66 (gA → gI before ṅit + hal-ādi)
  - 8.3.59 ṣatva + 8.4.41 ṣṭutva in tripāḍī
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_it_halantyam_lopa_yathasankhyam, P00_luN_lakara_cli_sic, P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _pada_merge(state: State) -> None:
    # Local import (structural helper).
    from pipelines.subanta import _pada_merge as _pm  # noqa: PLC0415

    _pm(state)


def derive_aDhyagIzwa() -> State:
    # Include upasarga aDi from the start so 6.1.77 can detect upasarga-dhatu boundary.
    upa = Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence("aDi")),
        tags={"upasarga"},
        meta={"upadesha_slp1": "aDi"},
    )
    dh = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("iN")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "iN"},
    )
    s = State(terms=[upa, dh], meta={}, trace=[])
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "Atmanepada"

    # Dhātu adhikāra for pratyaya-vidhāna.
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    # luṅ spine: luG placeholder + cli → sic (it-lopa on sic).
    s = P00_luN_lakara_cli_sic(s)

    # Substitute iN → gAN (natural, no arm needed).
    s = apply_rule("2.4.45", s)
    # N-it of gAN.
    s = P00_it_halantyam_lopa_yathasankhyam(s)
    # Install ṅit-atideśa for the following pratyaya.
    s = apply_rule("1.2.1", s)

    # aṭ augment for luṅ (finds dhatu by tag).
    s = apply_rule("6.4.71", s)
    # yaṇ at upasarga-dhatu boundary: aDi+a → aDy+a.
    s = apply_rule("6.1.77", s)

    # ītva on gAN before hal-ādi ṅit pratyaya.
    s = apply_rule("6.4.66", s)

    # iṭ on ardhadhatuka sic (natural detection).
    s = apply_rule("7.2.35", s)
    s = apply_rule("6.1.101", s)  # I + i → I

    # Choose 3sg ātmanepada ending `ta`.
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_form"] = "ta"
    s = apply_rule("3.4.78", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)  # tin it-lopa

    # Tripāḍī: ṣatva + ṣṭutva.
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.4.41", s)
    return s


__all__ = ["derive_aDhyagIzwa"]

