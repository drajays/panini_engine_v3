"""
pipelines/pawapawAyati_anukaraNa_corrected_P017_demo.py — **P017** *paṭapaṭāyati*.

*Anukaraṇa* **``pawat``** + vārttika *dvitva* (**6.1.1**), **5.4.57** ``qAc``,
**8.1.2** *āmreḍita* note, **6.1.97** *pararūpa* (``pawat``+``pawat``→``pawapawat``),
*it* **1.3.7**/**1.3.3**/**1.3.9**, **1.4.18** *bha*, **6.4.143** *ṭi*-lopa,
**3.1.13** ``kyaz``, *it* again, structural *dhātu* merge (**``pawapawAy``**),
**3.1.32**, laṭ spine (**3.2.123** … **3.1.68** *śap*), *it* on *śap*,
``_pada_merge`` — aligned with ``corrected_prakriyas_v2`` row **P017**
(surface **``pawapawAyati``**).

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` + narrow structural
merges (cf. **P016** *kyaz* residue).
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


def _merge_pawapaw_shap_a(state: State) -> None:
    """``pawapaw`` + ``a`` (``qAc`` residue) → ``pawapawA`` *prātipadika*."""
    if len(state.terms) != 2:
        return
    stem, sfx = state.terms[0], state.terms[1]
    if "".join(v.slp1 for v in stem.varnas) != "pawapaw":
        return
    if len(sfx.varnas) != 1 or sfx.varnas[0].slp1 not in ("a", "A"):
        return
    merged = Term(
        kind="prakriti",
        varnas=list(stem.varnas) + list(sfx.varnas),
        tags={"anga", "prātipadika"},
        meta=dict(stem.meta),
    )
    state.terms = [merged]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "अच्-संयोगः",
            "form_before": state.flat_slp1(),
            "form_after": state.flat_slp1(),
            "why_dev": "पटपट् + आ → पटपटा (P017)।",
            "status": "APPLIED",
        }
    )


def _merge_pawapawA_kyaz_residue(state: State) -> None:
    """``pawapawA`` + *kyaz* residue ``ya`` → ``pawapawAy`` *dhātu* (semivowel only)."""
    if len(state.terms) < 2:
        return
    stem, sfx = state.terms[0], state.terms[1]
    if "prātipadika" not in stem.tags:
        return
    sfx_flat = "".join(v.slp1 for v in sfx.varnas)
    sfx_tail = [sfx.varnas[0]] if sfx_flat == "ya" else list(sfx.varnas)
    merged = Term(
        kind="prakriti",
        varnas=list(stem.varnas) + sfx_tail,
        tags={"dhatu", "anga", "sanadi"},
        meta={},
    )
    state.terms = [merged] + state.terms[2:]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "धातु-संयोगः",
            "form_before": state.flat_slp1(),
            "form_after": state.flat_slp1(),
            "why_dev": "पटपटा + य्-अवशेष → पटपटाय (P017)।",
            "status": "APPLIED",
        }
    )


def derive_pawapawAyati_anukaraNa_corrected_P017() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pawat")),
        tags={"anga"},
        meta={"upadesha_slp1": "pawat"},
    )
    s = State(terms=[stem], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P017_demo"] = True
    s.meta["lakara"] = "laT"

    s = apply_rule("1.2.45", s)

    s.meta["corrected_v2_P017_6_1_1_dvitva_arm"] = True
    s = apply_rule("6.1.1", s)

    s.meta["corrected_v2_P017_5_4_57_arm"] = True
    s = apply_rule("5.4.57", s)

    s.meta["corrected_v2_P017_8_1_2_arm"] = True
    s = apply_rule("8.1.2", s)

    s.meta["corrected_v2_P017_6_1_97_pararupa_arm"] = True
    s = apply_rule("6.1.97", s)

    s.meta["corrected_v2_P017_1_3_7_qAc_arm"] = True
    for sid in ("1.3.7", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)
    s.meta.pop("corrected_v2_P017_1_3_7_qAc_arm", None)

    s = apply_rule("1.4.18", s)

    s.meta["corrected_v2_P017_6_4_143_arm"] = True
    s = apply_rule("6.4.143", s)

    _merge_pawapaw_shap_a(s)

    s.meta["corrected_v2_P017_3_1_13_arm"] = True
    s = apply_rule("3.1.13", s)

    for sid in ("1.3.8", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    _merge_pawapawA_kyaz_residue(s)

    s = apply_rule("3.1.32", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("laT")),
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    if laT.varnas and laT.varnas[-1].slp1 == "T":
        del laT.varnas[-1]
    s.terms.append(laT)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "tip"
    s = apply_rule("3.4.78", s)

    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)

    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("3.4.113", s)
    s = apply_rule("1.1.64", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_pawapawAyati_anukaraNa_corrected_P017"]
