"""
pipelines/upapada_krt.py — canonical upapada kṛt derivation functions.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P01_subanta_bootstrap,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    run_subanta_sup_attach_and_finish,
    P00_sup_it_lopa_aprkta,
)
from engine import apply_rule
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_kurucarI() -> State:
    """
    P005-A: kuru + Ni + car + ṭa (3.2.16) → kurucarī
    — strīliṅga prathamā ekavacana.
    """
    kuru = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kuru")),
        tags={"anga", "prātipadika", "upapada"},
        meta={"upadesha_slp1": "kuru"},
    )
    ni = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Ni")),
        tags={"sup", "pratyaya", "upadesha"},
        meta={"upadesha_slp1": "Ni"},
    )
    car = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("car")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "car"},
    )
    s = State(terms=[kuru, ni, car], meta={}, trace=[], samjna_registry={})
    s.meta["upapada_krt_kurucara_frame"] = True

    s = apply_rule("1.3.1", s)
    s = apply_rule("3.1.92", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.2.16", s)
    s = apply_rule("2.2.19", s)
    s = apply_rule("1.2.46", s)

    s.meta["pratipadika_avayava_ready"] = True
    s.meta["luk_2_4_71_recipe"] = True
    s = apply_rule("2.4.71", s)

    for sid in ("1.3.7", "1.3.9"):
        s = apply_rule(sid, s)

    # Structural merge: kuru + car + wa residue → kurucara
    acc: list = []
    for t in s.terms:
        if term_is_sup_luk_ghost(t):
            continue
        up = (t.meta.get("upadesha_slp1") or "").strip()
        if up == "kuru":
            acc.extend(v.clone() for v in t.varnas)
        elif up == "car":
            acc.extend(v.clone() for v in t.varnas)
        elif "krt" in t.tags and up == "wa":
            acc.extend(v.clone() for v in t.varnas)
    before = s.flat_slp1()
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika", "samasa_member", "krt"},
        meta={"upadesha_slp1": "kurucara", "corrected_v2_P005_A_kurucara_stem": True},
    )
    s.terms = [merged]
    s.trace.append({
        "sutra_id": "__MERGE__", "sutra_type": "STRUCTURAL",
        "type_label": "उपपद-कुरुचर",
        "form_before": before, "form_after": s.flat_slp1(),
        "why_dev": "कुरु + चर् + ट्-शेष → कुरुचर।", "status": "APPLIED",
    })

    s = apply_rule("1.2.46", s)
    s = apply_rule("4.1.15", s)

    for sid in ("1.3.8", "1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("6.4.1", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)

    # Merge kurucara + ī → kurucarī
    before2 = s.flat_slp1()
    acc2: list = []
    for t in s.terms:
        acc2.extend(v.clone() for v in t.varnas)
    merged2 = Term(
        kind="prakriti",
        varnas=acc2,
        tags={"anga", "prātipadika", "strīliṅga"},
        meta={"upadesha_slp1": "kurucarI"},
    )
    s.terms = [merged2]
    s.trace.append({
        "sutra_id": "__MERGE__", "sutra_type": "STRUCTURAL",
        "type_label": "कुरुचरी",
        "form_before": before2, "form_after": s.flat_slp1(),
        "why_dev": "कुरुचर् + ई → कुरुचरी।", "status": "APPLIED",
    })

    s = apply_rule("4.1.1", s)
    s.meta["vibhakti_vacana"] = "1-1"
    s = P00_sup_it_lopa_aprkta(s)
    s = apply_rule("6.1.68", s)
    return s


def derive_upasarajaH() -> State:
    """
    P005-B: upasara + Ni + jan + ḍa (3.2.97) → upasarajaḥ
    — pulliṅga prathamā ekavacana.
    """
    upasara = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("upasara")),
        tags={"anga", "prātipadika", "upapada"},
        meta={"upadesha_slp1": "upasara"},
    )
    ni = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Ni")),
        tags={"sup", "pratyaya", "upadesha"},
        meta={"upadesha_slp1": "Ni"},
    )
    jan = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("jan~")),
        tags={"dhatu", "anga", "upadesha"},
        meta={"upadesha_slp1": "jan~"},
    )
    s = State(terms=[upasara, ni, jan], meta={}, trace=[], samjna_registry={})
    s.meta["upapada_krt_upasaraja_frame"] = True

    s = apply_rule("1.3.1", s)
    s = apply_rule("3.1.92", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)

    s = apply_rule("1.3.2", s)
    s = apply_rule("3.2.97", s)
    for sid in ("1.3.3", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("2.2.19", s)
    s = apply_rule("1.2.46", s)

    s.meta["pratipadika_avayava_ready"] = True
    s.meta["luk_2_4_71_recipe"] = True
    s = apply_rule("2.4.71", s)

    for sid in ("1.3.7", "1.3.9"):
        s = apply_rule(sid, s)

    s = apply_rule("6.4.143", s)

    # Structural merge: upasara + j + a → upasaraja
    acc: list = []
    for t in s.terms:
        if term_is_sup_luk_ghost(t):
            continue
        acc.extend(v.clone() for v in t.varnas)
    before = s.flat_slp1()
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika", "samasa_member", "krt", "pulliṅga"},
        meta={"upadesha_slp1": "upasaraja"},
    )
    s.terms = [merged]
    s.trace.append({
        "sutra_id": "__MERGE__", "sutra_type": "STRUCTURAL",
        "type_label": "उपपद-उपसरज",
        "form_before": before, "form_after": s.flat_slp1(),
        "why_dev": "उपसर + ज् + अ → उपसरज।", "status": "APPLIED",
    })

    s = apply_rule("1.2.46", s)
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s = P01_subanta_bootstrap(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s
