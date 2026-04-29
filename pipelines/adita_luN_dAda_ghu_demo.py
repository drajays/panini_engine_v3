"""
pipelines/adita_luN_dAda_ghu_demo.py — *adita* (**अदित**) luṅ 3.sg ātmanepada demo.

Source: ``separated_prakriyas/prakriya_14_2026-04-29_14_08_55.json``

Target SLP1: **adita**

Narrow spine (aligned with corrected JSON prose):
  *da~da* surface **dA**, luṅ + **sic** (**3.2.110**→**cli/sic**), **gha** (**1.1.20**),
  **स्थाद्वरे… इच्** (**1.2.17** demo), augment **अ** (**6.4.71**),
  **ā**-lop before **इ** (**6.4.64** demo), tin **ति** (**3.4.78** → ``ta``), *pada* merge +
  tripāḍī entry (**8.2.1**).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_luN_lakara_cli_sic, P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_adita() -> State:
    # Post–it-drop stem **dā** (**dA**) — *śāstrīya* label **da~da** in meta for **gha**/rules.
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("dA"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "da~da"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "Atmanepada"

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = P00_luN_lakara_cli_sic(s)

    s = apply_rule("1.1.20", s)

    s.meta["1_2_17_ghu_sici_ic_arm"] = True
    s = apply_rule("1.2.17", s)

    # Drop ``c``-it off **इच्** (demo path).
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    s = apply_rule("6.4.71", s)

    s.meta["6_4_64_A_lopa_kngitic_i_arm"] = True
    s = apply_rule("6.4.64", s)

    # ``lu`` placeholder → tin ``ta`` (ātmanepada third singular).
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    return s


__all__ = ["derive_adita"]
