"""
pipelines/Bavitavyam_split_prakriyas_P002_demo.py — **P002** (**भवितव्यम्**).

Source: ``…/my_scripts/final/split_prakriyas_11/P002.json``.

Spine (``apply_rule`` + structural ``_pada_merge`` after **1.2.46**, as in other kṛdanta demos):

  **3.1.96** (*tavyat*) → **1.3.3** → **1.3.9** → **7.2.35** → **7.3.84** → **6.1.78** → **1.2.46** →
  ``napuṃsaka`` on the kṛt ``Term`` → ``_pada_merge`` → **4.1.2** → **7.1.24** → **6.1.107**.

**Edition note (JSON step 11 vs engine):** ``P002.json`` names **6.1.101** (*akaḥ savarṇe dīrghaḥ*) for
**a**+**am**. For **a**-final **napuṃsaka** + **am**, **6.1.107** (*अमि पूर्वः*) applies first, deletes the
stem-final **a**, blocks **6.1.101**, and yields **Bavitavyam** — the attested form. The recipe follows
**6.1.107** (same pattern as ``pipelines/Amalakam_prakriya_44_demo.py``).

``_pada_merge`` is structural (``__MERGE__`` trace), not a sūtra — see ``pipelines/subanta.py``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_BU_split_P002() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("BU")),
        tags={"dhatu", "anga", "prātipadika", "prakriya_P002_Bavitavyam_demo"},
        meta={"upadesha_slp1": "BU"},
    )


def derive_Bavitavyam_split_prakriyas_P002() -> State:
    s = State(terms=[_witness_BU_split_P002()], meta={}, trace=[])

    s.meta["prakriya_P002_3_1_96_tavyat_arm"] = True
    s = apply_rule("3.1.96", s)

    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("7.2.35", s)
    s = apply_rule("7.3.84", s)
    s = apply_rule("6.1.78", s)
    s = apply_rule("1.2.46", s)

    s.terms[-1].tags.add("napuṃsaka")

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)

    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.24", s)
    s = apply_rule("6.1.107", s)
    return s


__all__ = ["derive_Bavitavyam_split_prakriyas_P002", "_witness_BU_split_P002"]
