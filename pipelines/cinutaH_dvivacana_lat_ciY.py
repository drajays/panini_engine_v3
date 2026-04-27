"""
pipelines/cinutaH_dvivacana_lat_ciY.py — चिनुतः (*ciñ*, laṭ, 3rd dual *parasmaipada*).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/चिनुतः .md``

Target SLP1: **cinutaH** (चिनुतः).  Scheduling is ``apply_rule`` only (CONSTITUTION
Art. 7 / 11).  *Śnu* *vikaraṇa* is **3.1.73** (armed by recipe meta); *halantyam*
on *tas* is blocked by **1.3.3** + ``is_tin_vibhakti_pratyaya`` for *tusma* finals
(*na vibhaktau tusmāḥ*).

*Sunutaḥ* (*ṣañ abhiṣave* → *su* by **6.1.64**) is the same spine once **6.1.64**
exists in the engine and the *dhātu* row is wired — not implemented here.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_ciY_dhatu_hal_it_then_bhuvadi,
    P00_ciY_lat_tas_snu_tripadi_tail,
    P00_lat_vartamane_tas_and_sap,
)
from sutras.adhyaya_1.pada_3.kartari_pada_1_3_78 import find_primary_dhatu
from sutras.adhyaya_1.pada_4.dvi_eka_1_4_22 import DVI_EKA_NIMITTA_KEY


def _build_state() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ciY"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "ciY"},
    )
    s = State(terms=[dhatu], meta={}, trace=[])
    s.meta["pada"] = "parasmaipada"
    return s


def derive_cinutaH() -> State:
    s = _build_state()
    s = P00_ciY_dhatu_hal_it_then_bhuvadi(s)

    d0 = find_primary_dhatu(s)
    if d0 is None:
        raise RuntimeError("derive_cinutaH: primary dhātu not found")
    d0.meta[DVI_EKA_NIMITTA_KEY] = "dvi"

    s = P00_lat_vartamane_tas_and_sap(s)
    s = P00_ciY_lat_tas_snu_tripadi_tail(s)
    return s


__all__ = ["derive_cinutaH"]
