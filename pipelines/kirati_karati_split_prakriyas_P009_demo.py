"""
pipelines/kirati_karati_split_prakriyas_P009_demo.py — **P009** (*kirati* note; JSON spine yields **karati**).

Source: ``…/my_scripts/final/split_prakriyas_11/P009.json``.

The JSON explicitly notes the classical target **kirati** (via 7.4.10 etc.), but the
recorded steps demonstrate the **7.3.84** guṇa path on **kF** yielding **karati**.
This pipeline implements that recorded spine (rule-based, apply_rule-only).

Spine:
  **3.1.91** → **3.1.1–3** → **3.2.123** → (structural +laT) → **3.4.77** → **3.4.78** (*tip*) →
  **3.1.77** (*Sa* vikaraṇa, recipe-armed) → **1.3.8** → **1.3.9** →
  **7.3.84** → **1.1.51** → **1.3.3** → **1.3.9** → (flat concat = karati).

CONSTITUTION Art. 7 / 11: ``apply_rule`` only (plus structural lakāra placeholder insertion).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_kirati_karati_split_prakriyas_P009() -> State:
    # Dhātu witness (kF) for the recorded guṇa demonstration.
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kF")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "kF"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["prakriya_P009_kirati_note_karati_spine"] = True

    # laṭ setup (structural placeholder + tip selection by 3.4.78).
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("laT"),
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

    # tudādi vikaraṇa Sa (recipe-armed; narrow slice extended for kF).
    s.meta["3_1_77_sa_arm"] = True
    s = apply_rule("3.1.77", s)

    # it on Sa initial S, then lopa → surface a.
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.9", s)

    # guṇa on kF (F → a, then 1.1.51 inserts r) before the following sārvadhātuka Sa.
    s = apply_rule("7.3.84", s)
    s = apply_rule("1.1.51", s)
    # After uRaN-rapara, the dhātu is no longer in upadeśa-state; otherwise the
    # inserted final 'r' would be mis-read as halantyam-it by a later 1.3.3 on *tip*.
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    # it on tip final p, then lopa → ti.
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    return s


__all__ = ["derive_kirati_karati_split_prakriyas_P009"]

