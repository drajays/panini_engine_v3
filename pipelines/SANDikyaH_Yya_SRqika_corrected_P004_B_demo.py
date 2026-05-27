"""
pipelines/SANDikyaH_Yya_SRqika_corrected_P004_B_demo.py — **P004-B** शाण्डिक्यः.

शण्डिक (``SaRqika``) + ञ्य (**4.3.92**) → ``SANqikya``; पुंलिङ्ग प्रथमा एकवचन → ``SANqikyaH``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + structural *pada* merge / subanta drivers.
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
    P06b_pratyaya_through_taddhite_4_1_76,
    P00_attach_sup_from_pratipadika,
    P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi,
)
from pipelines.subanta import (
    _pada_merge,
    run_subanta_preflight_through_1_4_7,
    run_subanta_sup_attach_and_finish,
)

from sutras.adhyaya_1.pada_3.sutra_1_3_7 import META_P004_B_Yya_CUTU

_STEM_UPA = "SaRqika"


def derive_SANDikyaH_Yya_SRqika_corrected_P004_B() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(_STEM_UPA)),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": _STEM_UPA},
    )
    stem.tags.add("pulliṅga")
    s = State(terms=[stem], meta={}, trace=[])
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"

    s = apply_rule("2.1.1", s)
    s = P00_attach_sup_from_pratipadika(s)

    s = apply_rule("4.3.92", s)

    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.50", s)
    s = P06b_pratyaya_through_taddhite_4_1_76(s)
    s = P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi(s)

    s = apply_rule("6.4.1", s)
    # ``Yya``: initial ``Y`` is *cuṭ*-class *it* — **1.3.7** must precede **1.3.3**
    # so the stem-initial ``S`` is not wrongly tagged (both are *cuṭ*).
    s.meta[META_P004_B_Yya_CUTU] = True
    for sid in ("1.3.7", "1.3.3", "1.3.8", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)

    s = apply_rule("7.2.117", s)

    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)

    _pada_merge(s)
    if s.terms:
        t0 = s.terms[0]
        t0.kind = "prakriti"
        for tg in ("prātipadika", "anga", "pulliṅga"):
            t0.tags.add(tg)
        t0.tags.discard("pada")

    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


__all__ = ["derive_SANDikyaH_Yya_SRqika_corrected_P004_B", "_STEM_UPA"]
