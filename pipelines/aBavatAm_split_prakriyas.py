"""
pipelines/aBavatAm_split_prakriyas.py — legacy **P005** split-prakriyā (**अभवताम्**, *laṅ*).

Source: ``…/my_scripts/final/split_prakriyas_11/P005.json``.
This is **not** ``corrected_prakriyas_v2`` **P005-A** (*kurucarī*) / **P005-B** (*upasarajaḥ*);
those bundle rows need separate glass-box recipes.

Spine (rule-based ``apply_rule`` only; tin block factored as ``P00_laG_tin_tas_tAm_adesh_block``):

  **3.2.111** (*anadyatane laṅ*) → **3.1.91** → **3.1.1–3** → ``P00_laG_tin_tas_tAm_adesh_block`` ( **3.4.77**
  **3.4.78** *tas* → **3.4.101** *tas*→*tām*, saṃjñā slice, tin *it*-lopa ) → **3.1.68** *Sap*
  → *it* on *śap* (**1.3.8**, **1.3.3**, **1.3.9**) → **7.3.84** → **6.1.78** → **6.4.71** *aṭ*.

``state.meta['lakara']`` is **laG** throughout so **6.4.71** and **3.4.101** fire mechanically.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only (plus ``P00_*`` wrappers that are pure ``apply_rule`` lists).
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_laG_tin_tas_tAm_adesh_block, P00_lashakvataddhite_it_lopa_chain, P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_aBavatAm_split_prakriyas_P005() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("BU")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "BU"},
    )
    dhatu.meta["1_4_22_affix_class"] = "dvi"

    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["prakriya_P005_aBavatAm_split_prakriyas_11"] = True
    s.meta["lakara"] = "laG"

    s = apply_rule("3.2.111", s)
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s = P00_laG_tin_tas_tAm_adesh_block(s)

    s = apply_rule("3.1.68", s)
    s = P00_lashakvataddhite_it_lopa_chain(s)

    s = apply_rule("7.3.84", s)
    s = apply_rule("6.1.78", s)
    s = apply_rule("6.4.71", s)
    return s


__all__ = ["derive_aBavatAm_split_prakriyas_P005"]
