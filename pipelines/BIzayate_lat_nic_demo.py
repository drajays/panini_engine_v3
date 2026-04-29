"""
pipelines/BIzayate_lat_nic_demo.py — भीषयते (BIzayate) glass-box.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/भीषयते .md`

Target SLP1: **BIzayate**
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_upadesha_it_1_3_1_2_5,
    P00_lashakvataddhite_it_lopa_chain,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)


def _build_state() -> State:
    # ñi + bhI~ (upadeśa): initial ñi will be removed by 1.3.5 + 1.3.9.
    dhatu = Term(
        kind="prakriti",
        # Use non-anunāsika vowel for the root vowel (bhI), since 1.3.2/1.3.9
        # would otherwise fully elide a final anunāsika vowel in dhātu-upadeśa.
        varnas=parse_slp1_upadesha_sequence("YiBI"),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "YiBI"},
    )
    return State(terms=[dhatu], meta={}, trace=[])


def _lat_ta_and_sap(s: State) -> State:
    # Like canonical P00_lat_vartamane_tip_and_sap, but choose ātmanepada `ta`
    # and then apply 1.1.64 + 3.4.79 to get `te`.
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
    # Substitute to ta via 3.4.78
    s = apply_rule("3.4.77", s)
    s.meta["tin_adesha_pending"] = True
    s.meta["tin_adesha_slp1"] = "ta"
    s = apply_rule("3.4.78", s)
    # Insert Sap between dhātu and ta
    s.meta["3_1_68_kartari_recipe"] = True
    s = apply_rule("3.1.68", s)
    return s


def _structural_merge_zuk_and_nic_into_dhatu(s: State) -> State:
    """
    Structural: bhI + zuk + i → bhIzi (single dhātu term).
    Expects: [dhatu(BI), zuk(z), nic(i)] after it-lopa.
    """
    if len(s.terms) < 3:
        return s
    dh, zuk, nic = s.terms[0], s.terms[1], s.terms[2]
    if "dhatu" not in dh.tags:
        return s
    if (zuk.meta.get("upadesha_slp1") or "").strip() != "zuk":
        return s
    if "nic" not in nic.tags:
        return s
    before = s.flat_slp1()
    dh.varnas = [v.clone() for v in dh.varnas] + [v.clone() for v in zuk.varnas] + [v.clone() for v in nic.varnas]
    dh.meta["upadesha_slp1"] = "BIzi"
    dh.tags.add("sanadi")
    # Remove zuk and nic terms.
    s.terms = [dh] + s.terms[3:]
    s.trace.append(
        {
            "sutra_id": "__NIC_ZUK_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "णिच्-षुक्-मेलनम्",
            "form_before": before,
            "form_after": s.flat_slp1(),
            "why_dev": "भी + षुक् + णिच्-शेष (ष्+इ) → भीषि (संरचनात्मकं, न सूत्रम्)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_BIzayate() -> State:
    s = _build_state()

    # Dhātu it-lopa: 1.3.2 + 1.3.5 then 1.3.9 (ñi-lopa).
    s = P00_upadesha_it_1_3_1_2_5(s)
    s = apply_rule("1.3.9", s)
    if s.terms:
        s.terms[0].tags.discard("upadesha")
        # Normalize upadeśa identity to the post-lopa dhātu for downstream demo rules.
        s.terms[0].meta["upadesha_slp1"] = "BI"

    # Causative ṇic.
    s.meta["3_1_26_nic_arm"] = True
    s = apply_rule("3.1.26", s)
    s.meta.pop("3_1_26_nic_arm", None)

    # Fear-causation augment.
    s = apply_rule("1.1.46", s)
    s.meta["7_3_40_zuk_arm"] = True
    s = apply_rule("7.3.40", s)
    s.meta.pop("7_3_40_zuk_arm", None)

    # it-lopa on zuk (u~ and k).
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.9", s)

    # Merge to derived dhātu BIzi and tag dhātu again.
    s = _structural_merge_zuk_and_nic_into_dhatu(s)
    s = apply_rule("3.1.32", s)

    # Atmanepada override (trace fact for the note).
    s.meta["1_3_68_arm"] = True
    s = apply_rule("1.3.68", s)
    s.meta.pop("1_3_68_arm", None)

    # laṭ + ta + Sap
    s = _lat_ta_and_sap(s)

    # it-lopa on Sap (ś,p) etc.
    s = P00_lashakvataddhite_it_lopa_chain(s)

    # Aṅga saṃjñā and guṇa.
    s = apply_rule("1.4.13", s)
    s = apply_rule("7.3.84", s)

    # e + a → aya (eco'yavāyāvaḥ)
    s = apply_rule("6.1.78", s)

    # ta → te (Ti + 3.4.79).
    s = apply_rule("1.1.64", s)
    s = apply_rule("3.4.79", s)

    # Structural merge for final rendering.
    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    return s


__all__ = ["derive_BIzayate"]

