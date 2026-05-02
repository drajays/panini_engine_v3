"""
pipelines/gArgyAH_garga_yaY_luk_P042_demo.py — P042 (गार्ग्याः)

Source: ``split_prakriyas_11/P042.json``.

Target SLP1: ``gArgyAH`` — *garga* + **yañ** (**4.1.105**), *it* on **yaY**, **7.2.117**
*vṛddhi*, structural ``gArga``+``ya`` → ``gArgya``, **4.1.2** (*jas*), **4.1.162**
*gotra*, **2.4.64** (*yañ* *luk* audit), **1.1.60**/**1.1.61**, **1.1.62**/**1.1.63**,
**7.1.9** (narrow **P042** ``jas``→``as``), **6.1.101**, ``_pada_merge``, **8.2.1** →
**8.2.66** → **8.3.15** → **8.2.30** (skip), **1.1.68**.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _p042_merge_to_gArgya(state: State) -> None:
    """Structural: ``gArga`` + ``ya`` (``yaY`` residue) → ``gArgya`` (P042)."""
    b = state.flat_slp1()
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("gArgya")),
        tags={"anga", "prātipadika", "pulliṅga", "P042_gArgya_stem"},
        meta={"upadesha_slp1": "gArgya"},
    )
    state.terms = [stem]
    state.trace.append(
        {
            "sutra_id": "__MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "यञ्-मेलनम्",
            "form_before": b,
            "form_after": state.flat_slp1(),
            "why_dev": "गार्ग + य → गार्ग्य (संरचनात्मकं, P042)।",
            "status": "APPLIED",
        }
    )


def derive_gArgyAH_garga_yaY_luk_P042() -> State:
    garga = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("garga")),
        tags={"anga", "prātipadika", "P042_garga_demo"},
        meta={"upadesha_slp1": "garga"},
    )
    s = State(terms=[garga], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.68", s)
    s = apply_rule("4.1.76", s)
    s = apply_rule("4.1.1", s)

    s.meta["P042_4_1_105_yaY_arm"] = True
    s = apply_rule("4.1.105", s)

    for sid in ("1.3.3", "1.3.8", "1.3.9", "1.3.10"):
        s = apply_rule(sid, s)

    s = apply_rule("6.4.1", s)
    s = apply_rule("7.2.117", s)

    _p042_merge_to_gArgya(s)

    s.meta["vibhakti_vacana"] = "1-3"
    s = apply_rule("4.1.2", s)

    s.meta["P042_4_1_162_arm"] = True
    s = apply_rule("4.1.162", s)

    s.meta["P042_2_4_64_arm"] = True
    s = apply_rule("2.4.64", s)

    s = apply_rule("1.1.60", s)
    s = apply_rule("1.1.61", s)

    s = apply_rule("1.1.62", s)
    s = apply_rule("1.1.63", s)

    s.meta["P042_7_1_9_jas_to_as_arm"] = True
    s = apply_rule("7.1.9", s)

    s = apply_rule("6.1.101", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)

    s = apply_rule("1.4.14", s)

    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    s = apply_rule("8.2.30", s)

    s.meta.pop("1_1_68_svadrupa_audit_done", None)
    s = apply_rule("1.1.68", s)
    return s


__all__ = ["derive_gArgyAH_garga_yaY_luk_P042"]
