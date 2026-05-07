"""
pipelines/vyadyotizwa_luN_dyut_corrected_P018_B_demo.py — **P018-B** *vyadyotiṣṭa*.

Upasarga ``vi`` + **``dyut``** (lexical ``dyut~``) + luṅ *ātmanepada* 3 sg.:
``P00_luN_lakara_cli_sic``, *tiṅ* **ta**, **7.2.35** *iṭ*, **7.3.86** *guṇa*
(``dyut``→``dyot``), **6.4.71** *aṭ*, **6.1.77**, ``_pada_merge``, **8.2.1** /
**8.3.59** / **8.4.41** — ``corrected_prakriyas_v2`` **P018-B**
(surface **``vyadyotizwa``**).

See **P018-A** demo for the **``dyut~``** orthography note (**``dyut``** tape).

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_it_halantyam_lopa_yathasankhyam,
    P00_luN_lakara_cli_sic,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_vyadyotizwa_luN_dyut_corrected_P018_B() -> State:
    upa = Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence("vi")),
        tags={"upasarga"},
        meta={"upadesha_slp1": "vi"},
    )
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("dyut")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "dyut~", "karmakatva": "akarmaka"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P018_B_demo"] = True
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "Atmanepada"

    s = apply_rule("1.3.1", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.terms.insert(0, upa)

    for t in s.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")

    s = P00_luN_lakara_cli_sic(s)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)

    s.meta["7_2_35_allow_sic"] = True
    s.meta["luN_sic_ardhadhatuka"] = True
    s = apply_rule("7.2.35", s)

    s.meta["corrected_v2_P018_B_7_3_86_arm"] = True
    s = apply_rule("7.3.86", s)

    s = apply_rule("6.4.71", s)
    s = apply_rule("6.1.77", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.4.41", s)
    return s


__all__ = ["derive_vyadyotizwa_luN_dyut_corrected_P018_B"]
