"""
pipelines/ratnaDAtamam_prakriya_22_demo.py — ``prakriya_22`` (*ratnadhātamam*).

Glass-box spine (JSON ``panini_engine_pipeline`` / corrected analysis):
  ``ratna`` + internal ``Sas`` + ``√dhā`` → **3.2.76** ``kvip`` → **1.2.46**;
  **2.4.71** *luk* on internal ``Sas``; **2.2.19** *upapada* frame note;
  ``P00_lashakvataddhite_it_lopa_chain`` on ``kvip``; **6.1.67** narrow *kvip*
  residue; structural *ratna* + ``DA`` → ``ratnaDA``; **5.3.55** ``tamap`` (``5_3_55_tamap_pullinga_arm``)
  + **1.1.22** + **1.2.46** + ``P00_taddhita_it_lopa_chain`` → ``ratnaDAtama``;
  *subanta* **2-1** ``am`` + **6.1.107** → ``ratnaDAtamam``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` + structural merge only; phase-boundary
``samjna_registry`` clear is documented for **1.2.46** re-entry after the *kṛt* leg.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from core.canonical_pipelines import (
    P00_lashakvataddhite_it_lopa_chain,
    P00_taddhita_it_lopa_chain,
    P00_taddhita_samartha_pragdivyata_adhikaras,
    P06a_pratyaya_adhikara_3_1_1_to_3,
    subanta_post_4_1_2,
)
from pipelines.subanta import run_subanta_preflight_through_1_4_7


def _ratna_upapada_karma() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("ratna")),
        tags={"anga"},
        meta={"upadesha_slp1": "ratna"},
    )


def _Sas_internal() -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Sas")),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": "Sas"},
    )


def _dha_dhatu() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("DA")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "DA"},
    )


def _structural_merge_ratnaDA(s: State) -> State:
    """``ratna`` + ``DA`` after *sup* ghost + empty *kvip* (not a sūtra)."""
    from engine.lopa_ghost import term_is_sup_luk_ghost

    b = s.flat_slp1()
    acc: list = []
    for t in s.terms:
        if term_is_sup_luk_ghost(t):
            continue
        if "krt" in t.tags and not t.varnas:
            continue
        acc.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika", "pulliṅga"},
        meta={"upadesha_slp1": "ratnaDA"},
    )
    s.terms = [merged]
    s.trace.append(
        {
            "sutra_id": "__RATNADHA_UPAPADA_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "उपपद-क्विप्-मेलनम्",
            "form_before": b,
            "form_after": s.flat_slp1(),
            "why_dev": "रत्न + धा → रत्नधा (संरचनात्मकं)।",
            "status": "APPLIED",
        }
    )
    return s


def _structural_merge_ratnaDAtama(s: State) -> State:
    """``ratnaDA`` + ``tama`` (*tamap* post-*it*) → ``ratnaDAtama``."""
    b = s.flat_slp1()
    acc: list = []
    for t in s.terms:
        acc.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=acc,
        tags={"anga", "prātipadika", "pulliṅga"},
        meta={"upadesha_slp1": "ratnaDAtama"},
    )
    s.terms = [merged]
    s.trace.append(
        {
            "sutra_id": "__RATNADHA_TAMA_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "तमप्-मेलनम्",
            "form_before": b,
            "form_after": s.flat_slp1(),
            "why_dev": "रत्नधा + तम → रत्नधातम (संरचनात्मकं)।",
            "status": "APPLIED",
        }
    )
    return s


def derive_ratnaDAtamam_prakriya_22() -> State:
    s = State(terms=[_ratna_upapada_karma(), _Sas_internal(), _dha_dhatu()], meta={}, trace=[])

    s.meta["3_2_76_kvip_arm"] = True
    s = apply_rule("3.2.76", s)
    s = apply_rule("1.2.46", s)

    s.meta["pratipadika_avayava_ready"] = True
    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)

    s.meta["2_2_19_upapada_atiNg_arm"] = True
    s = apply_rule("2.2.19", s)

    s = P00_lashakvataddhite_it_lopa_chain(s)

    s.meta["prakriya_22_kvip_residue_arm"] = True
    s = apply_rule("6.1.67", s)

    s = _structural_merge_ratnaDA(s)

    # Allow **1.2.46** again on the *taddhita* two-*Term* frame (cf. *kumārī* demo).
    s.samjna_registry.pop("1.2.46_generic_pratipadika", None)

    s = apply_rule("2.1.1", s)
    s = P00_taddhita_samartha_pragdivyata_adhikaras(s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s.meta["5_3_55_tamap_pullinga_arm"] = True
    s = apply_rule("5.3.55", s)
    s = apply_rule("1.1.22", s)
    s = apply_rule("1.2.46", s)
    s = P00_taddhita_it_lopa_chain(s)
    s = _structural_merge_ratnaDAtama(s)

    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "2-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    s = subanta_post_4_1_2(s)
    return s


__all__ = ["derive_ratnaDAtamam_prakriya_22"]
