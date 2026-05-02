"""
pipelines/juhoti_hu_lat_tip_Slu_P040_demo.py — P040 (जुहोति)

Source: ``split_prakriyas_11/P040.json``.

Target SLP1: ``juhoti`` — *hu* + *laṭ* + *tip*, *juhotyādi* **2.4.75** *śluḥ* (no *śap*),
**1.1.60**/**1.1.61**, **6.1.10** *ślau* *dvi*tva, **7.4.59** (vacuous here — *COND-FALSE*
skip), **7.4.62** *kuhoścuḥ*, **7.3.84** *guṇa*, **1.1.62** (*pratyaya-lakṣaṇam* note),
**6.1.87** (no *ādgauṇa* trigger on this tape — skip), **1.1.68**.

Structural: after **1.1.61**, remove the ``Slu`` placeholder ``Term`` (JSON ``hu+0+ti``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_tip_to_ti, P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _p040_remove_slu_placeholder(state: State) -> None:
    """Drop ``P040_slu_placeholder`` after **1.1.61** (*ślu*-saṃjñā spine)."""
    idxs = [i for i, t in enumerate(state.terms) if "P040_slu_placeholder" in t.tags]
    if not idxs:
        return
    for i in reversed(idxs):
        state.terms.pop(i)
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "श्लु-अवशेष-लोपः",
            "form_before": state.flat_slp1(),
            "form_after": state.flat_slp1(),
            "why_dev": "१.१.६१-अनन्तरं श्लु-प्रत्ययस्य संरचनात्मक-अपसारणम् (P040)।",
            "status": "APPLIED",
        }
    )


def derive_juhoti_hu_lat_tip_Slu_P040() -> State:
    hu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("hu")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "hu"},
    )
    hu.tags.add("P040_juhotyadi")
    s = State(terms=[hu], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.68", s)

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

    s = P00_tip_to_ti(s)

    s.meta["P040_2_4_75_arm"] = True
    s = apply_rule("2.4.75", s)

    s = apply_rule("1.1.60", s)
    s = apply_rule("1.1.61", s)
    _p040_remove_slu_placeholder(s)

    s.meta["P040_6_1_10_slau_arm"] = True
    s = apply_rule("6.1.10", s)

    s = apply_rule("7.4.59", s)

    s.meta["P040_7_4_62_abhyasa_arm"] = True
    s = apply_rule("7.4.62", s)

    s = apply_rule("3.4.113", s)

    s.meta["P040_7_3_84_arm"] = True
    s = apply_rule("7.3.84", s)

    s = apply_rule("1.1.62", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)

    s = apply_rule("6.1.87", s)

    s.meta.pop("1_1_68_svadrupa_audit_done", None)
    s = apply_rule("1.1.68", s)
    return s


__all__ = ["derive_juhoti_hu_lat_tip_Slu_P040"]
