"""
pipelines/paceran_vidhi_liG_pac_Ja_P038_demo.py — **पचेरन्** (*paceran*, *vidhi-liṅ*).

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P038.json``

Target SLP1: **paceran** — *pac* + *vidhi-liṅ* + *ātmanepada* *pra-bahu* *jha* → *ran*,
with **3.4.102** *sīyuṭ*, **3.4.105** *jha*→*ran*, **7.2.79** / **6.4.105** on the
augment, **6.1.70** (*vyor vali* narrow) for *y*-lopa before *ran*, **3.1.68** *śap*,
then **6.1.87** *ādg guṇaḥ* and *pada* merge.

**1.1.58** (*ekādeśa* vs *sthānivat*) is a *paribhāṣā* note in the JSON (**n12**);
no separate engine step.

**Dhātu *it*:** like **P037**, ``upadesha`` is removed from ``pac`` after **1.3.1**
so the root-final ``c`` is not treated as *halantyam-it*.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_paceran_vidhi_liG_pac_Ja_P038() -> State:
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pac")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "pac"},
    )
    s = State(terms=[dhatu], meta={}, trace=[], samjna_registry={})
    s.meta["lakara"] = "liG"
    s.meta["pada"] = "Atmanepada"

    s = apply_rule("1.1.68", s)
    s = apply_rule("1.3.1", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")

    s = apply_rule("3.1.91", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s.meta["P038_3_3_161_vidhi_liG_arm"] = True
    s = apply_rule("3.3.161", s)

    s.meta["3_4_102_sIyuw_arm"] = True
    s = apply_rule("3.4.102", s)

    s = apply_rule("3.4.69", s)

    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "Ja"
    s = apply_rule("3.4.78", s)

    s.meta["P038_3_4_105_arm"] = True
    s = apply_rule("3.4.105", s)

    for sid in ("1.4.99", "1.4.100", "1.3.78", "1.4.101", "1.4.108", "1.4.102", "1.4.22"):
        s = apply_rule(sid, s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    s.meta["P038_7_2_79_sIyuw_s_lopa_arm"] = True
    s = apply_rule("7.2.79", s)
    s.meta["P038_6_4_105_uw_trim_arm"] = True
    s = apply_rule("6.4.105", s)
    s.meta["P038_6_1_70_y_before_r_arm"] = True
    s = apply_rule("6.1.70", s)

    # **3.1.91** *adhikāra* is purged once execution passes chapter **7** (see
    # ``purge_closed_adhikaras``); reopen it before **3.1.68** *śap*.
    s = apply_rule("3.1.91", s)
    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)

    s = apply_rule("6.1.84", s)
    s = apply_rule("6.1.87", s)

    from pipelines.subanta import _pada_merge  # noqa: PLC0415

    _pada_merge(s)
    return s


__all__ = ["derive_paceran_vidhi_liG_pac_Ja_P038"]
