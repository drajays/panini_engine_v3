"""
pipelines/trApuSam_jAtuSam_taddhita_demo.py

Implements the prakriyā from `त्रापुषम् .md`:
  - त्रापुषम् (trApuSam) from trapu + Nas + (aR + zuk)
  - जातुषम् (jAtuSam) from jatu + Nas + (aR + zuk)
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.lopa_ghost import term_is_sup_luk_ghost
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _build_gen_sg_state(stem_slp1: str) -> State:
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(stem_slp1)),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": stem_slp1},
    )
    return State(terms=[stem], meta={"vibhakti_vacana": "6-1"}, trace=[])


def _run_it_chain(state: State) -> State:
    # Enough for this demo: anunāsika-it, halantyam-it, lśakvataddhite, then lopa.
    for sid in ("1.3.2", "1.3.3", "1.3.8", "1.3.9"):
        state = apply_rule(sid, state)
    return state


def _structural_merge_agama_into_anga(state: State) -> State:
    """
    Structural (not a sūtra): after it-lopa, merge the `zuk` residue (z) into
    the aṅga so that aṅga↔taddhita adjacency logic (7.2.117) sees one aṅga.
    Expected frame here: [anga, z(agama), sup(Nas...), taddhita(a...)].
    """
    if len(state.terms) < 4:
        return state
    anga = state.terms[0]
    agm = state.terms[1]
    if "anga" not in anga.tags or "prātipadika" not in anga.tags:
        return state
    if agm.meta.get("upadesha_slp1") != "zuk":
        return state
    before = state.flat_slp1()
    merged_varnas = [v.clone() for v in anga.varnas] + [v.clone() for v in agm.varnas]
    anga.varnas = merged_varnas
    state.terms.pop(1)
    state.trace.append(
        {
            "sutra_id": "__ZUK_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "षुक्-मेलनम्",
            "form_before": before,
            "form_after": state.flat_slp1(),
            "why_dev": "षुक्-आगमस्य शेष-वर्णः (ष्) अङ्गे एव अन्तर्भाव्यते (संरचनात्मकं, न सूत्रम्)।",
            "status": "APPLIED",
        }
    )
    return state


def _structural_merge_non_ghost_terms_to_pratipadika(state: State, *, upadesha_slp1: str) -> State:
    all_varnas = []
    for t in state.terms:
        if term_is_sup_luk_ghost(t):
            continue
        all_varnas.extend(v.clone() for v in t.varnas)
    merged = Term(
        kind="prakriti",
        varnas=all_varnas,
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": upadesha_slp1},
    )
    before = state.flat_slp1()
    state.terms = [merged]
    state.trace.append(
        {
            "sutra_id": "__TADDHITA_MERGE__",
            "sutra_type": "STRUCTURAL",
            "type_label": "तद्धित-मेलनम्",
            "form_before": before,
            "form_after": state.flat_slp1(),
            "why_dev": "तद्धितान्त-प्रातिपदिक-रचना (संरचनात्मकं, न सूत्रम्)।",
            "status": "APPLIED",
        }
    )
    return state


def _derive_vikara_neuter_nom_sg(stem_slp1: str, *, out_upadesha_slp1: str) -> State:
    s = _build_gen_sg_state(stem_slp1)
    s = apply_rule("4.1.2", s)   # Nas
    s = apply_rule("1.1.46", s)  # kit/tit placement gate

    s.meta["4_3_138_arm"] = True
    s = apply_rule("4.3.138", s)
    s.meta.pop("4_3_138_arm", None)

    s = _run_it_chain(s)         # zuk -> z ; aR -> a (with R as it-marker)
    s = _structural_merge_agama_into_anga(s)
    s = apply_rule("1.2.46", s)  # ensure prātipadika tagging present
    # Recipe assertion for 2.4.71 (see sutra_2_4_71 doc): internal-avayava ready.
    s.meta["pratipadika_avayava_ready"] = True

    s.meta["2_4_71_luk_arm"] = True
    s = apply_rule("2.4.71", s)  # sup (Nas) luk -> ghost
    s.meta.pop("2_4_71_luk_arm", None)
    s.meta.pop("pratipadika_avayava_ready", None)

    s = apply_rule("6.4.1", s)
    s = apply_rule("7.2.117", s)  # ādi-vṛddhi due to ṇit taddhita

    # Merge to a single taddhitānta stem (e.g. trApuSa).
    s = _structural_merge_non_ghost_terms_to_pratipadika(s, upadesha_slp1=out_upadesha_slp1)

    # Now prathamā ekavacana napuṃsaka: su -> am -> amipūrva.
    s.terms[0].tags.add("napuṃsaka")
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)   # su (s~)
    s = apply_rule("7.1.24", s)  # su -> am
    s = apply_rule("6.1.107", s) # am i pūrvaḥ: drop stem-final a
    return s


def derive_trApuSam() -> State:
    return _derive_vikara_neuter_nom_sg("trapu", out_upadesha_slp1="trApuSa")


def derive_jAtuSam() -> State:
    return _derive_vikara_neuter_nom_sg("jatu", out_upadesha_slp1="jAtuSa")


__all__ = ["derive_trApuSam", "derive_jAtuSam"]

