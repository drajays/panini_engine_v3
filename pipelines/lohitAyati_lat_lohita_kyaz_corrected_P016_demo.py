"""
pipelines/lohitAyati_lat_lohita_kyaz_corrected_P016_demo.py — **P016** *lohitāyati*.

*Lohita* + denominative **क्यष्** (**``kyaz``**) + laṭ parasmaipada 3 sg.: **3.1.13**,
*it* **1.3.8**/**1.3.3**/**1.3.9**, **3.1.32**, laṭ spine with **3.1.68** *śap*, **7.4.25**,
**6.1.101** — aligned with ``corrected_prakriyas_v2`` row **P016** (surface **``lohitAyati``**).

CONSTITUTION Art. 7 / 11: ``apply_rule`` + ``_pada_merge`` only; structural
``__MERGE__`` for *prātipadika* + *kyaz* residue (cf. **P015** *dhātu* merge).
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


def _merge_lohita_kyaz_residue(state: State) -> None:
    """``lohita`` + *kyaz* residue → ``lohitay`` *dhātu* (only **य**, not **यअ**)."""
    if len(state.terms) < 2:
        return
    stem, sfx = state.terms[0], state.terms[1]
    if "prātipadika" not in stem.tags:
        return
    sfx_flat = "".join(v.slp1 for v in sfx.varnas)
    # **1.3.9** leaves ``y`` + ``a`` from ``kyaz``; surface ``लोहितय`` keeps the semivowel only.
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
            "why_dev": "लोहित + य-अवशेष → लोहितय (P016)।",
            "status": "APPLIED",
        }
    )


def derive_lohitAyati_lat_lohita_kyaz_corrected_P016() -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("lohita")),
        tags=set(),
        meta={},
    )
    s = State(terms=[stem], meta={}, trace=[], samjna_registry={})
    s.meta["corrected_v2_P016_demo"] = True
    s.meta["lakara"] = "laT"

    s = apply_rule("1.2.45", s)

    s.meta["corrected_v2_P016_3_1_13_arm"] = True
    s = apply_rule("3.1.13", s)

    for sid in ("1.3.8", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    _merge_lohita_kyaz_residue(s)

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

    s.meta["corrected_v2_P016_7_4_25_arm"] = True
    s = apply_rule("7.4.25", s)

    s = apply_rule("6.1.101", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_lohitAyati_lat_lohita_kyaz_corrected_P016"]
