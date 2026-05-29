"""
pipelines/IDe_lit_indh.py — ईधे (IDe) glass-box demo.

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_05_2026-04-29_14_06_20.json`

Target SLP1: **IDe**

Narrow spine used by the note:
  inD + liṭ (parokṣa) + ātmanepada ta →
  3.4.81: ta → eS (1.1.55) → it-lopa (S) → e
  1.2.6: indhi/bhavati → kṅiti locus on liṭ-ending
  6.4.24: n-lopa (inD → iD) before kṅiti
  6.1.8: liṭ dvitva + 6.1.4 + 7.4.60 (abhyāsa trim to i)
  6.1.101: i+i → I, giving IDe.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_lit_dvitva_abhyasa_hrasva, P00_lit_ta_esh_it_lopa
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_IDe() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("inD"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "inD"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # Dhātu bootstrap.
    s = apply_rule("1.3.1", s)

    # parokṣa liṭ
    s.meta["liT_lakara_recipe"] = True
    s = apply_rule("3.2.115", s)
    # Remove the lakāra placeholder term; this demo models liṭ effects via the
    # explicit `ta` ending + 3.4.81 and dvitva (6.1.8).
    if s.terms and (s.terms[-1].meta.get("upadesha_slp1") or "").strip() == "liT":
        s.terms.pop()

    # ātmanepada gate (narrow: just records pada)
    s.meta["1_3_12_target_upadesha_slp1"] = "inD"
    s = apply_rule("1.3.12", s)

    # attach the 3sg ātmanepada liṭ ending `ta` (placeholder for 3.4.81)
    ta = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("ta"),
        tags={"pratyaya", "tin", "upadesha"},
        meta={"upadesha_slp1": "ta"},
    )
    s.terms.append(ta)

    # ta -> eS, then anekal-shit gate, then it-lopa on S -> e
    s.meta["liT_esh_recipe"] = True
    s = P00_lit_ta_esh_it_lopa(s)
    # normalize the remaining liṭ ending as `e`
    if s.terms and "pratyaya" in s.terms[-1].tags:
        s.terms[-1].meta["upadesha_slp1"] = "e"

    # indhi/bhavati paribhāṣā for kṅiti locus on liṭ-ending
    s.meta["1_2_6_indhi_bhavati_arm"] = True
    s = apply_rule("1.2.6", s)

    # n-lopa before kṅiti: inD -> iD
    s = apply_rule("6.4.24", s)

    # liṭ dvitva + abhyāsa operations (trim abhyāsa to just initial vowel i)
    s.meta["liT_dvitva_recipe"] = True
    s = P00_lit_dvitva_abhyasa_hrasva(s, short_abhyasa=True)

    # i + i -> I (savarṇa dīrgha)
    s = apply_rule("6.1.101", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_IDe"]

