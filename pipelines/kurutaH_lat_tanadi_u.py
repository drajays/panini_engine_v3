"""
pipelines/kurutaH_lat_tanadi_u.py — कुरुतः (kurutaH) glass-box demo.

Source: `/Users/dr.ajayshukla/my_scripts/separated_prakriyas/prakriya_03_2026-04-29_14_06_05.json`

Target SLP1: **kurutaH**

Narrow derivation slice used by the note:
  kf (tanādi) + u-vikaraṇa + laṭ (3rd dual parasmaipada: tas) →
  7.3.84 guṇa (kf→ka) + 1.1.51 r-para (kar) →
  1.2.4 kṅit behaviour on tas → 6.4.110 a→u (kur) →
  pada merge + tripāḍī ru/visarga (kurutaH).
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P00_upadesha_it_anunasik_hal_lopa,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_tin_tas_adesh_full,
    P00_lac_lat_attach,
    P00_tanadi_u_guna,

    P00_tripadi_rutva_visarga,
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

    s = P00_lac_lat_attach(s)
    s = P00_tin_tas_adesh_full(s)
    s.meta["3_1_79_tanadi_u_arm"] = True
    s = P00_tanadi_u_guna(s)
    s = apply_rule("1.2.4", s)
    s = apply_rule("1.1.5", s)

    # a → u before kṅit sārvadhātuka.
    s = apply_rule("6.4.110", s)

    # Merge and finish ru/visarga.
    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = P00_tripadi_rutva_visarga(s)
    return s


__all__ = ["derive_kurutaH"]

