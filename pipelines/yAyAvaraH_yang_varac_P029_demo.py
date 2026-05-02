"""
pipelines/yAyAvaraH_yang_varac_P029_demo.py — P029 **यायावरः** (*yā* + *yaṅ* + *varac*, m. sg.).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P029.json``

Spine (glass-box; **6.1.101** is a no-op once segments are merged — JSON lists it
for pedagogy):

  **1.1.68** → *bhūvādi* *it* → *yaṅ* spine (**3.1.22** … **3.1.32**) → *dvitva*
  (**6.1.1**/**6.1.9**/**6.1.4**) → **7.4.59** / **7.4.83** (*abhyāsa*) → **7.4.60**
  → **3.2.176** (*varac*) → *it* (**1.3.3**/**1.3.7**/**1.3.9**) → **6.1.70**
  (*lopo vyor vali* — JSON mislabels as **6.1.66**) → optional **6.1.101** →
  structural merge → ``P00_subanta_prathama_su_tripadi_visarga``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_bhuvadi_dhatu_it_anunasik_hal,
    P00_subanta_prathama_su_tripadi_visarga,
    P00_yang_adhikara_yaG_append_sanadi,
    P00_yang_dvitva_abhyasa_gate,
)
from pipelines.subanta import _pada_merge


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yA")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "yA"},
    )
    return State(terms=[dhatu], meta={}, trace=[], samjna_registry={})


def derive_yAyAvaraH_yang_varac_P029() -> State:
    s = _build_state()
    s.meta["pada"] = "parasmaipada"

    s = apply_rule("1.1.68", s)

    s = P00_bhuvadi_dhatu_it_anunasik_hal(s)
    s = P00_yang_adhikara_yaG_append_sanadi(s)
    s = P00_yang_dvitva_abhyasa_gate(s)

    s.meta["P029_7_4_59_abhyasa_hrasva_arm"] = True
    s = apply_rule("7.4.59", s)
    s.meta["P029_7_4_83_abhyasa_dirgha_arm"] = True
    s = apply_rule("7.4.83", s)
    s = apply_rule("7.4.60", s)

    s.meta["P029_3_2_176_varac_arm"] = True
    s = apply_rule("3.2.176", s)

    for t in s.terms:
        if "abhyasa" not in t.tags and ("dhatu" in t.tags or "krt" in t.tags):
            t.tags.add("prātipadika")
            t.tags.add("pulliṅga")

    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.7", s)
    s = apply_rule("1.3.9", s)

    s.meta["P029_6_1_70_vy_lopa_arm"] = True
    s = apply_rule("6.1.70", s)

    s = apply_rule("6.1.101", s)

    _pada_merge(s)
    s.meta["linga"] = "pulliṅga"
    return P00_subanta_prathama_su_tripadi_visarga(s)


__all__ = ["derive_yAyAvaraH_yang_varac_P029"]
