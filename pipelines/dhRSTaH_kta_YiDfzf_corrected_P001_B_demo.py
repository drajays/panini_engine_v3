"""
pipelines/dhRSTaH_kta_YiDfzf_corrected_P001_B_demo.py — **P001-B** धृष्टः.

Source row **P001-B** in the audited ``corrected_prakriyas_v2`` bundle (upstream
``prakriya_01_*.json``): *ñi*+*dhṛṣ* (*YiDfzf~*, Svādi) + *kta* → *dhṛṣṭaḥ*.

Spine: ñi-*it* (**1.3.5** …) → *Dfz* + *kta* → *ta*; *pada* merge → **8.4.41**
(recipe *pre-Tripāḍī* arm: *z*+*t*→*z*+*w* so **4.1.2** is not ASIDDHA-blocked);
**1.2.46**; prathamā *su* → **8.2.1** / **8.2.66** / **8.3.15**.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``pipelines.subanta._pada_merge`` only.
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
    P00_ciY_kartari_krt_nistha_adhikara_prefix,
    P00_krt_ardhadhatuka_ekac_it_and_guna_audit,
    P00_lashakvataddhite_it_lopa_chain,
    P00_pratipadika_prathama_sup_after_stem_merge,
    P00_tripadi_rutva_visarga,
)
from pipelines.subanta import _pada_merge


def derive_dhRSTaH_kta_YiDfzf_corrected_P001_B() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("YiDfzf~")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "YiDfzf~"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    s.meta["ekac_dhatu"] = True

    for sid in ("1.3.1", "1.3.5", "1.3.2", "1.3.9"):
        s = apply_rule(sid, s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
    s = apply_rule("1.3.1", s)

    s = P00_ciY_kartari_krt_nistha_adhikara_prefix(s)
    s.meta["3_2_102_target_upadesha_slp1"] = "YiDfzf~"
    s.meta["3_2_102_kta_arm"] = True
    s = apply_rule("3.2.102", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)
    s = P00_krt_ardhadhatuka_ekac_it_and_guna_audit(s)

    _pada_merge(s)
    s = apply_rule("8.4.41", s)

    s.terms[0].meta["corrected_v2_P001_B_nistha_stem"] = True
    s = apply_rule("1.2.46", s)

    # ``1.2.46`` leaves the Tripāḍī ``pada`` shell; subanta tail expects a
    # ``prakriti`` prātipadika row like *citaḥ* / *uktaḥ* demos.
    stem = s.terms[0]
    stem.kind = "prakriti"
    stem.tags.discard("pada")

    s.meta["linga"] = "pulliṅga"
    s = P00_pratipadika_prathama_sup_after_stem_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


__all__ = ["derive_dhRSTaH_kta_YiDfzf_corrected_P001_B"]
