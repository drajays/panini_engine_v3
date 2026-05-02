"""
pipelines/kO_staH_vakya_P028_demo.py — P028 (कौ स्तः) glass-box.

Source JSON: ``/Users/dr.ajayshukla/my_scripts/final/split_prakriyas_11/P028.json``

Target SLP1: **kO staH** (space kept as a vākya boundary).

We derive two independent padas, then return their juxtaposition:
  - ``kO`` from ``kim`` + nom.du sup ``O`` via **7.2.103** + **6.1.88**
  - ``staH`` from ``as`` + laṭ + ``tas`` with **2.4.72** (*Sap* luk) and **6.4.111**

No across-word sandhi is forced here; the space is semantic, not a varṇa tape.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3, P00_tin_tas_adesh_full
from pipelines.subanta import (
    SUBANTA_RULE_IDS_POST_4_1_2,
    PADA_MERGE_STEP,
    _pada_merge,
    build_initial_state,
    run_subanta_preflight_through_1_4_7,
)


def _derive_kO() -> str:
    s = build_initial_state("kim", 1, 2, "pulliṅga")
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    s.meta["P028_7_2_103_kim_kah_arm"] = True
    s = apply_rule("7.2.103", s)
    # Continue the canonical subanta tail (includes 6.1.88 and ru/visarga)
    for sid in SUBANTA_RULE_IDS_POST_4_1_2:
        if sid == PADA_MERGE_STEP:
            _pada_merge(s)
            continue
        s = apply_rule(sid, s)
    return s.render()


def _derive_staH() -> str:
    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("as"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "as", "karmakatva": "akarmaka"},
    )
    # Mark dvivacana class for 1.4.22 slice inside P00_tin_tas_adesh_full.
    dhatu.meta["1_4_22_affix_class"] = "dvi"
    s = State(terms=[dhatu], meta={}, trace=[])

    # Prevent later generic *it*-chains (inside tin selection) from treating the
    # dhātu-final ``s`` as *halantyam-it*.
    s.terms[0].tags.discard("upadesha")

    # Pratyaya adhikāra + laṭ placeholder + tas.
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

    # Add Sap then luk it by 2.4.72 (adādi).
    Sap = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Sap"),
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "Sap"},
    )
    s.terms.insert(1, Sap)
    s.meta["2_4_72_sap_luk_arm"] = True
    s = apply_rule("2.4.72", s)

    # apit sārvadhātuka → kṅiti (1.2.4), then as a-lopa (6.4.111).
    s = apply_rule("1.2.4", s)
    s.meta["P028_6_4_111_as_al_lopa_arm"] = True
    s = apply_rule("6.4.111", s)

    # Merge and ru/visarga for tas → taH.
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s.render()


def derive_kO_staH_vakya_P028() -> str:
    return f"{_derive_kO()} {_derive_staH()}"


__all__ = ["derive_kO_staH_vakya_P028"]

