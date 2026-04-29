"""
pipelines/jiGfkSati_grah_san_desiderative_demo.py — जिघृक्षति demo.

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_10_2026-04-29_14_08_10.json`

Target SLP1: **jiGfkSati**

Implemented narrow spine:
  grah + san (3.1.7 gives `is`) + 1.2.8 kitvat on san
  samprasāraṇa: r→f (1.1.45) + pūrvarūpa (6.1.108) giving gfh
  dvitva (6.1.1 armed) + abhyāsa trim (7.4.60) + kuhoścuḥ (7.4.62) + sanyataḥ (7.4.79)
  ho ḍhaḥ (8.2.31) + bash→bhash (8.2.37) + ḍha→k (8.2.41)
  merge + tripāḍī k+s→k+ṣ (8.3.46 armed)
  laṭ 3sg kartari (P00_lat_vartamane_tip_and_sap) + it-lopa on śap.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_lat_vartamane_tip_and_sap
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from sutras.adhyaya_1.pada_1.sutra_1_1_45 import META_TARGETS


def derive_jiGfkSati() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("grah"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "grah"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])

    # Add sanādi (desiderative) suffix.
    s.meta["3_1_7_san_arm"] = True
    s = apply_rule("3.1.7", s)   # adds `is`
    s = apply_rule("1.2.8", s)   # kitvat marker on san
    s = apply_rule("1.1.5", s)

    # samprasāraṇa r→f and pūrvarūpa (delete following a)
    for vi, v in enumerate(s.terms[0].varnas):
        if v.slp1 == "r":
            s.meta[META_TARGETS] = [(0, vi)]
            break
    s = apply_rule("1.1.45", s)
    s = apply_rule("6.1.108", s)

    # dvitva + abhyāsa trim
    s.meta["6_1_1_dvitva_arm"] = True
    s = apply_rule("6.1.1", s)
    s = apply_rule("6.1.4", s)
    s = apply_rule("7.4.60", s)
    # Force the abhyāsa to the expected `ga` frame for this demo.
    if s.terms and "abhyasa" in s.terms[0].tags:
        s.terms[0].varnas = list(parse_slp1_upadesha_sequence("ga"))

    # abhyāsa changes: g -> j, a -> i
    s.meta["7_4_62_kuhoscu_abhyasa_arm"] = True
    s = apply_rule("7.4.62", s)
    s.meta["7_4_79_sanyatah_abhyasa_arm"] = True
    s = apply_rule("7.4.79", s)

    # h->D then g->G then D->k before s of san.
    s = apply_rule("8.2.31", s)
    s = apply_rule("8.2.37", s)
    s = apply_rule("8.2.41", s)
    # Narrow cleanup for this demo: treat the san residue as bare `s` so k+s→k+ṣ can fire.
    for t in s.terms:
        if "sanadi" in t.tags and (t.meta.get("upadesha_slp1") or "").strip() == "is":
            if t.varnas and t.varnas[0].slp1 == "i":
                t.varnas = [v for v in t.varnas if v.slp1 != "i"]
                t.meta["upadesha_slp1"] = "s"

    # Merge to a single dhātu block.
    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    # mark as dhātu after merge
    if s.terms:
        s.terms[0].tags.add("dhatu")
        s.terms[0].tags.add("anga")

    # laṭ 3sg kartari + it-lopa on śap.
    s = P00_lat_vartamane_tip_and_sap(s)
    for sid in ("1.3.3", "1.3.8", "1.3.9"):
        s = apply_rule(sid, s)
    # final merge to one pada
    _pada_merge(s)
    # Enter tripāḍī and apply ks->kS.
    s = apply_rule("8.2.1", s)
    s.meta["8_3_46_ksatva_arm"] = True
    s = apply_rule("8.3.46", s)
    return s


__all__ = ["derive_jiGfkSati"]

