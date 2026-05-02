"""
pipelines/papatuH_lit_pA_P035_demo.py — **पपतुः** (*papatuḥ*, *liṭ* pra. dvi, *pā*).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P035.json``

Spine (``apply_rule`` + recipe meta):

  • *pā* (**pA**) + *liṭ* (**3.2.115**) → *tas* → *atus* (**3.4.82**) + **1.2.5** (*kit*)
  • **6.4.64** — terminal **ā** *lopa* before *kṅiti* *atus*
  • **6.1.2** — *ekāca* *dvitva* with *sthānivat* **pā** before **p** + *atus*
  • **7.4.59** — *abhyāsa* **pā** → **pa**
  • *pada* merge (concat ⇒ **papatus**; JSON n.10 *savarṇa-dīrgha* is folded here)
  • **8.2.1** → **8.2.66** / **8.3.15** (ru / visarga)
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    P00_tin_tas_adesh_full,
)
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_papatuH_lit_pA_P035() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pA")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "pA"},
    )
    dhatu.meta["1_4_22_affix_class"] = "dvi"

    s = State(terms=[dhatu], meta={}, trace=[])

    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s.meta["3_2_115_paroksha_lit_arm"] = True
    s = apply_rule("3.2.115", s)

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.meta["3_4_82_lit_atus_arm"] = True
    s = P00_tin_tas_adesh_full(s)

    s = apply_rule("3.4.82", s)
    s = apply_rule("1.2.5", s)

    s.meta["P035_6_4_64_A_lopa_atus_arm"] = True
    s = apply_rule("6.4.64", s)

    s.meta["P035_6_1_2_ekaca_dve_arm"] = True
    s = apply_rule("6.1.2", s)

    s.meta["P035_7_4_59_abhyasa_hrasva_arm"] = True
    s = apply_rule("7.4.59", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_papatuH_lit_pA_P035"]
