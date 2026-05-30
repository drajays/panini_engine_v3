"""
pipelines/dIdhye_dIdhi_lat_parasmin_lesson.py — परस्मिन् (१.१.५७): *sva-nimitta* ए vs *para-nimitta* लोपः.

Prakriyā (दीधीङ् + लट् उत्तमैकवचन → **दीध्ये**):
  **3.2.123** लट् → **3.4.78** ``i`` (१sg आत्मनेपद) → **3.1.68** शप् → **2.4.72** लुक् →
  **3.4.79** ``i``→``e`` (स्वनिमित्तक आदेशः — **न** स्थानिवत्) → **7.4.53** निषेधः →
  **6.1.77** यणादेशः → **दीध्ये**.

Target SLP1: **dIdhye** (दीध्ये).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_tin_adesha_base, P00_adadi_sap_luk_tere
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _dhatu_dIdhI() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("dIdhI")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "dIdhI", "gana": 2},
    )


def _laT_placeholder() -> Term:
    varnas = list(parse_slp1_upadesha_sequence("laT"))
    if varnas and varnas[-1].slp1 == "T":
        varnas = varnas[:-1]
    return Term(
        kind="pratyaya",
        varnas=varnas,
        tags={"pratyaya", "upadesha", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )


def derive_dIdhye_dIdhi_lat_parasmin_lesson() -> State:
    s = State(terms=[_dhatu_dIdhI()], meta={}, trace=[])

    s.meta["lakara"] = "laT"
    s = apply_rule("3.2.123", s)
    s.terms.append(_laT_placeholder())

    s = P00_tin_adesha_base(s, "i")
    s.meta["3_1_68_kartari_recipe"] = True
    s = P00_adadi_sap_luk_tere(s)

    s = apply_rule("1.1.57", s)
    s = apply_rule("7.4.53", s)

    s = apply_rule("6.1.77", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_dIdhye_dIdhi_lat_parasmin_lesson"]
