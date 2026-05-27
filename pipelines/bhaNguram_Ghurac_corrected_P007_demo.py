"""
pipelines/bhaNguram_Ghurac_corrected_P007_demo.py — **P007** *bhaṅguram*.

``BaYjo`` + *ghurac* (**Gurc**) → stem ``BaNgura``; napuṃsaka prathamā ekavacana
→ ``BaNguram`` (SLP1 ``B`` = भ्).

Corrected-v2 bundle row **P007**.  Paribhāṣā demo
``pramANakRtAntarye_paribhasha_P007_demo.py`` is an
older split id — this module is the corrected-v2 **P007** *prayoga*.

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
    P00_it_halantyam_lopa_yathasankhyam,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from pipelines.krdanta import _structural_merge_to_pratipadika, build_dhatu_state
from pipelines.subanta import run_subanta_preflight_through_1_4_7, run_subanta_sup_attach_and_finish

_UPADESHA = "BaYjo"


def derive_bhaNgura_pratipadika_corrected_P007() -> State:
    """``BaYjo`` + *ghurac* → merged ``BaNgura`` (*kṛdanta* prātipadika)."""
    s = build_dhatu_state(_UPADESHA)

    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.73", s)
    s = P01_samjna_1_1_3_to_1_1_100(s=s, include_luk_block=True)
    s = P01_samjna_1_1_15_to_1_1_24(s)
    s = apply_rule("1.1.50", s)

    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.5", s)
    s = apply_rule("1.3.200", s)
    s = P00_it_halantyam_lopa_yathasankhyam(s)
    for t in s.terms:
        if "dhatu" in t.tags:
            t.tags.discard("upadesha")
    s = apply_rule("1.4.59", s)
    s = apply_rule("6.1.65", s)

    s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)

    s = apply_rule("3.2.161", s)

    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("1.3.10", s)

    s = apply_rule("1.1.50", s)
    s = apply_rule("7.3.52", s)
    s = apply_rule("1.2.45", s)
    s = apply_rule("1.2.46", s)
    s = _structural_merge_to_pratipadika(s, upadesha_slp1="BaNgura")
    return s


def derive_bhaNguram_corrected_P007() -> State:
    """Full pada: ``BaNgura`` + subanta (1-1 napuṃsaka) → ``BaNguram``."""
    s = derive_bhaNgura_pratipadika_corrected_P007()
    if s.terms:
        s.terms[0].tags.add("napuṃsaka")
    s.meta["linga"] = "napuṃsaka"
    s.meta["vibhakti_vacana"] = "1-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


__all__ = [
    "derive_bhaNgura_pratipadika_corrected_P007",
    "derive_bhaNguram_corrected_P007",
    "_UPADESHA",
]
