"""
pipelines/adhyagIzwa_luN_demo.py — अध्यगीष्ट (aDhyagIzwa) glass-box demo.

Source: `/Users/dr.ajayshukla/my_scripts/final/1_2_fully_corrected_prakriya.json`
Entry: 2026-04-29 14:05:49 / 14:05:58.

Target SLP1: **aDhyagIzwa**

This is a narrow luṅ demo that exists to exercise:
  - 2.4.45 (iN → gAN in luṅ) + 1.2.1 atideśa
  - 6.4.66 (gA → gI before ṅit + hal-ādi)
  - 8.3.59 ṣatva + 8.4.41 ṣṭutva in tripāḍī
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_luN_lakara_cli_sic, P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _pada_merge(state: State) -> None:
    # Local import (structural helper).
    from pipelines.subanta import _pada_merge as _pm  # noqa: PLC0415

    _pm(state)


def derive_aDhyagIzwa() -> State:
    # Dhātu only; we will structurally prepend the phonemic upasarga chunk `aDhy`
    # just before pada-merge (so 6.4.71 can see dhātu at terms[0]).
    dh = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("iN")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "iN"},
    )
    s = State(terms=[dh], meta={}, trace=[])
    s.meta["lakara"] = "luG"
    s.meta["pada"] = "Atmanepada"

    # Dhātu adhikāra for pratyaya-vidhāna.
    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    # luṅ spine: luG placeholder + cli → sic (it-lopa on sic).
    s = P00_luN_lakara_cli_sic(s)

    # Substitute iN → gAN (recipe-armed).
    s.meta["2_4_45_iNo_ga_luG_arm"] = True
    s = apply_rule("2.4.45", s)
    # Treat final N of gAN as it (halantyam) and lop it, so 7.2.35 sees I + i.
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    # Install ṅit-atideśa for the following pratyaya.
    s = apply_rule("1.2.1", s)

    # aṭ augment for luṅ.
    s = apply_rule("6.4.71", s)

    # ītva on gAN before hal-ādi ṅit pratyaya.
    s = apply_rule("6.4.66", s)

    # iṭ for sic (allow for demo).
    s.meta["7_2_35_allow_sic"] = True
    s.meta["luN_sic_ardhadhatuka"] = True
    s = apply_rule("7.2.35", s)
    s = apply_rule("6.1.101", s)  # I + i → I

    # Choose 3sg ātmanepada ending `ta`.
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    # Structural: prepend upasarga chunk `aDhy` (phonemic, post-sandhi) before pada-merge.
    upa = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("aDhy")),
        tags={"upasarga"},
        meta={"upadesha_slp1": "aDhy"},
    )
    s.terms.insert(0, upa)

    # Tripāḍī: ṣatva + ṣṭutva.
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.3.59", s)
    s = apply_rule("8.4.41", s)
    return s


__all__ = ["derive_aDhyagIzwa"]

