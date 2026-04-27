"""
pipelines/cinvanti_lat_ciY.py — चिन्वन्ति (*ciñ*, laṭ, 3rd plural *parasmaipada*).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/चिन्वन्ति.md``

Target SLP1: **cinvanti** (चिन्वन्ति).  Scheduling is ``apply_rule`` only (CONSTITUTION
Art. 7 / 11).

*Śnu* (**3.1.73**), *jhi* → *anti* (**7.1.3**), then *nu* + *anti* → *nv* + *anti*
via **6.1.77** with ``6_1_77_ik_yan_aci_general_arm`` (*iko yaṇ aci*).  The
**6.4.77** / **6.4.87** ladder from the note is not modelled as separate *vidhi*s
yet (docstring on ``P00_ciY_lat_jhi_snu_tripadi_tail``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_ciY_dhatu_hal_it_then_bhuvadi,
    P00_ciY_lat_jhi_snu_tripadi_tail,
    P00_lat_vartamane_jhi_and_sap,
)


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


def derive_cinvanti() -> State:
    s = _build_state()
    s = P00_ciY_dhatu_hal_it_then_bhuvadi(s)
    s = P00_lat_vartamane_jhi_and_sap(s)
    s = P00_ciY_lat_jhi_snu_tripadi_tail(s)
    return s


__all__ = ["derive_cinvanti"]
