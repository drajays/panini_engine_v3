"""
pipelines/cayanam_ciY_lyuw_corrected_P006_demo.py — **P006** चयनम्.

``ciY`` + *lyuṭ* (*lyuw*, bhāva) → stem ``cayana``; napuṃsaka prathamā ekavacana
→ ``cayanam``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + structural merge / subanta drivers only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State
from core.canonical_pipelines import (
    P01_samjna_1_1_15_to_1_1_24,
    P01_samjna_1_1_3_to_1_1_100,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_it_halantyam_lopa_yathasankhyam,
)
from pipelines.krdanta import _structural_merge_to_pratipadika, build_dhatu_state
from pipelines.subanta import run_subanta_preflight_through_1_4_7, run_subanta_sup_attach_and_finish

_META_P006_3_3_115 = "corrected_v2_P006_3_3_115_arm"

_UPADESHA = "ciY"


def derive_cayana_pratipadika_corrected_P006() -> State:
    """``ciY`` + *lyuṭ* → ``cayana`` (merged prātipadika), with **3.3.115** in trace."""
    s = build_dhatu_state(_UPADESHA)

    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = P01_samjna_1_1_3_to_1_1_100(s=s, include_luk_block=True)
    s = P01_samjna_1_1_15_to_1_1_24(s)
    s = apply_rule("1.1.50", s)

    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.5", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)
    for t in s.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")
    s = apply_rule("1.4.59", s)
    s = apply_rule("6.1.65", s)

    s.meta["krt_artha"] = "bhave"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)

    s.meta[_META_P006_3_3_115] = True
    s = apply_rule("3.3.115", s)
    s.meta.pop(_META_P006_3_3_115, None)

    s.meta["krt_upadesha_slp1"] = "lyuw"
    s = apply_rule("3.4.68", s)
    s = apply_rule("3.1.133", s)
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("3.4.114", s)
    s = apply_rule("1.4.13", s)
    s = apply_rule("1.1.65", s)
    s = apply_rule("6.4.1", s)
    s = apply_rule("7.3.84", s)
    s = apply_rule("7.1.1", s)
    s = apply_rule("7.2.116", s)
    s = apply_rule("7.2.115", s)
    s = apply_rule("6.1.78", s)
    s = apply_rule("6.1.77", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.2.46", s)
    s = _structural_merge_to_pratipadika(s, upadesha_slp1="cayana")
    return s


def derive_cayanam_corrected_P006() -> State:
    """Full pada: ``cayana`` + subanta (1-1 napuṃsaka) → ``cayanam``."""
    s = derive_cayana_pratipadika_corrected_P006()
    if s.terms:
        s.terms[0].tags.add("napuṃsaka")
    s.meta["linga"] = "napuṃsaka"
    s.meta["vibhakti_vacana"] = "1-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


__all__ = [
    "derive_cayana_pratipadika_corrected_P006",
    "derive_cayanam_corrected_P006",
    "_UPADESHA",
]
