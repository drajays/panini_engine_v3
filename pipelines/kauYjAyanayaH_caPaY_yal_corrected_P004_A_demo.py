"""
pipelines/kauYjAyanayaH_caPaY_yal_corrected_P004_A_demo.py — **P004-A** कौञ्जायन्यः.

``kuYja`` + षष्ठी *Nas* + **च्फञ्** (**4.1.98**) → merged ``kauYjAyana`` (meta); then **यञ्**
(**4.1.105**) → ``kauYjAyanaya`` (meta); पुंलिङ्ग प्रथमा एकवचन surface **``kOYjAyanyaH``**
(vṛddhi **O** = **au** in engine SLP1) ↔ IAST *kauñjāyanyaḥ*.

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
    P00_anabhihite_shashthi_shese_2_3_50,
    P00_attach_sup_from_pratipadika,
    P00_taddhita_it_lopa_chain,
    P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi,
)
from pipelines.subanta import (
    _pada_merge,
    run_subanta_preflight_through_1_4_7,
    run_subanta_sup_attach_and_finish,
)

from sutras.adhyaya_2.pada_3.sutra_2_3_50 import (
    META_OVERRIDE_VV as META_2_3_50_OVERRIDE_VV,
    META_SHESE_ELIGIBLE as META_2_3_50_ELIGIBLE,
)

_STEM_UPA = "kuYja"


def _normalize_merged_pratipadika(s: State, *, upadesha_slp1: str) -> None:
    if not s.terms:
        return
    t0 = s.terms[0]
    t0.kind = "prakriti"
    for tg in ("prātipadika", "anga", "pulliṅga"):
        t0.tags.add(tg)
    t0.tags.discard("pada")
    t0.meta["upadesha_slp1"] = upadesha_slp1


def derive_kauYjAyanayaH_caPaY_yal_corrected_P004_A() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(_STEM_UPA)),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": _STEM_UPA},
    )
    stem.tags.add("pulliṅga")
    s = State(terms=[stem], meta={}, trace=[])
    s.meta["prakriya_P004_A_caPhaya"] = True
    s.meta["linga"] = "pulliṅga"
    s.meta[META_2_3_50_ELIGIBLE] = True

    s = apply_rule("2.1.1", s)
    s = P00_anabhihite_shashthi_shese_2_3_50(s)
    s = P00_attach_sup_from_pratipadika(s)
    s = apply_rule("4.1.82", s)
    s = apply_rule("4.1.92", s)

    s = apply_rule("4.1.98", s)

    s = apply_rule("1.1.1", s)
    s = apply_rule("1.1.50", s)
    s = P06b_pratyaya_through_taddhite_4_1_76(s)
    s = P00_taddhita_pratipadika_internal_sup_luk_then_anga_vidhi(s)

    s = apply_rule("6.4.1", s)
    for sid in ("1.3.7", "1.3.3", "1.3.8", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)

    s = apply_rule("7.1.2", s)
    s = P00_taddhita_it_lopa_chain(s)

    s = apply_rule("7.2.117", s)
    s = apply_rule("1.4.18", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)
    s = apply_rule("1.1.60", s)

    _pada_merge(s)
    _normalize_merged_pratipadika(s, upadesha_slp1="kauYjAyana")

    # ── Stage 2: *yuvāpatya* **yañ** ───────────────────────────────────────
    s = apply_rule("4.1.105", s)

    s = apply_rule("6.4.1", s)
    for sid in ("1.3.3", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)

    _pada_merge(s)
    _normalize_merged_pratipadika(s, upadesha_slp1="kauYjAyanaya")

    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    # Śeṣa ṣaṣṭhī was only for the first *taddhita* leg; clear before *subanta*.
    s.meta.pop(META_2_3_50_ELIGIBLE, None)
    s.meta.pop(META_2_3_50_OVERRIDE_VV, None)
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


__all__ = ["derive_kauYjAyanayaH_caPaY_yal_corrected_P004_A", "_STEM_UPA"]
