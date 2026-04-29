"""
pipelines/kurutaH_lat_tanadi_u_demo.py — कुरुतः (kurutaH) glass-box demo.

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_03_2026-04-29_14_06_05.json`

Target SLP1: **kurutaH**

Narrow derivation slice used by the note:
  kf (tanādi) + u-vikaraṇa + laṭ (3rd dual parasmaipada: tas) →
  7.3.84 guṇa (kf→ka) + 1.1.51 r-para (kar) →
  1.2.4 kṅit behaviour on tas → 6.4.110 a→u (kur) →
  pada merge + tripāḍī ru/visarga (kurutaH).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P00_upadesha_it_anunasik_hal_lopa,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_tin_tas_adesh_full,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_kurutaH() -> State:
    # Use upadeśa with it-markers so the standard it-chain yields `kf` (k + f).
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("qukfY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "qukfY"},
    )
    # Mark dvivacana class for 1.4.22 slice inside P00_tin_tas_adesh_full.
    dhatu.meta["1_4_22_affix_class"] = "dvi"

    s = State(terms=[dhatu], meta={}, trace=[])

    # Dhātu it-lopa.
    s = P00_upadesha_it_1_3_1_2_5(s)          # includes 1.3.5 for qu-
    s = P00_upadesha_it_anunasik_hal_lopa(s)  # then 1.3.3 + 1.3.9 (incl. Y)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        s.terms[0].meta["upadesha_slp1"] = "kf"

    # Pratyaya adhikāra + laṭ + tas (3rd dual parasmaipada).
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
    s = P00_tin_tas_adesh_full(s)

    # tanādi u-vikaraṇa (śap apavāda).
    s.meta["3_1_79_tanadi_u_arm"] = True
    s = apply_rule("3.1.79", s)

    # guṇa on dhātu ik-final (f → a) in presence of following sārvadhātuka u.
    s = apply_rule("7.3.84", s)
    s = apply_rule("1.1.51", s)  # complete r-para for f→a

    # sarvadhātukam apit → kṅiti context on tas.
    s = apply_rule("1.2.4", s)
    s = apply_rule("1.1.5", s)

    # a → u before kṅit sārvadhātuka.
    s = apply_rule("6.4.110", s)

    # Merge and finish ru/visarga.
    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_kurutaH"]

