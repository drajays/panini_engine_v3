"""
pipelines/IDe_lit_indh_demo.py — ईधे (IDe) glass-box demo.

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
from __future__ import annotations

import sutras  # noqa: F401

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
    s.meta["3_2_115_paroksha_lit_arm"] = True
    s = apply_rule("3.2.115", s)
    # Remove the lakāra placeholder term; this demo models liṭ effects via the
    # explicit `ta` ending + 3.4.81 and dvitva (6.1.8).
    if s.terms and (s.terms[-1].meta.get("upadesha_slp1") or "").strip() == "liT":
        s.terms.pop()

    # ātmanepada gate (narrow: just records pada)
    s.meta["1_3_12_arm"] = True
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
    s.meta["3_4_81_lit_esh_arm"] = True
    s = apply_rule("3.4.81", s)
    s = apply_rule("1.1.55", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    # normalize the remaining liṭ ending as `e`
    if s.terms and "pratyaya" in s.terms[-1].tags:
        s.terms[-1].meta["upadesha_slp1"] = "e"

    # indhi/bhavati paribhāṣā for kṅiti locus on liṭ-ending
    s.meta["1_2_6_indhi_bhavati_arm"] = True
    s = apply_rule("1.2.6", s)

    # n-lopa before kṅiti: inD -> iD
    s = apply_rule("6.4.24", s)

    # liṭ dvitva + abhyāsa operations (trim abhyāsa to just initial vowel i)
    s.meta["6_1_8_lit_dvitva_arm"] = True
    s = apply_rule("6.1.8", s)
    if len(s.terms) >= 2 and "abhyasa" in s.terms[0].tags:
        s.terms[0].meta["7_4_60_first_hal_only"] = True
    s = apply_rule("6.1.4", s)
    s = apply_rule("7.4.60", s)

    # i + i -> I (savarṇa dīrgha)
    s = apply_rule("6.1.101", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_IDe"]

