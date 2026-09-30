"""
pipelines/bhattikavya_1_1.py — जयमङ्गला on Bhaṭṭikāvya 1.1.

Eight padāni of the first śloka, each via ``apply_rule`` (Art. 7, 11):

  अभूत् · नृपः · विबुधसखः · परंतपः · गुणाः · वरः · सनातनः · उपागमत्

Tiṅanta cells reuse canonical ``pipelines.tinanta.derive``. Kṛt / taddhita /
samāsānta cells schedule the vidhāyaka named in the ṭīkā, then inflect.
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    P00_anga_samjna_6_4_1,
    P00_guna_rapara_ayadi,
    P00_krt_it_lopa,
    P06a_pratyaya_adhikara_3_1_1_to_3,
)
from core.phases.tripadi import execute_tripadi_phase
from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.krdanta import build_dhatu_state
from pipelines.tinanta import derive as derive_tinanta

__pipeline_category__ = "भट्टिकाव्य १.१"


def _applied(state: State) -> list[str]:
    return [x["sutra_id"] for x in state.trace if x.get("status") == "APPLIED" and x.get("sutra_id")]


def _krt_it_lasaku(s: State) -> State:
    s = apply_rule("1.3.8", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    return s


def _prathama(s: State, *, vacana: int = 1) -> State:
    from pipelines.subanta import (
        run_subanta_preflight_through_1_4_7,
        run_subanta_sup_attach_and_finish,
    )
    from engine.phases.pada_merger import pada_merge

    if s.terms:
        s.terms[0].tags.add("pulliṅga")
        s.terms[0].tags.add("prātipadika")
        s.terms[0].tags.add("anga")
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = f"1-{vacana}"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    pada_merge(s)
    return execute_tripadi_phase(s)


def _merge_pratipadika(s: State) -> State:
    from engine.phases.pada_merger import pada_merge

    s = apply_rule("1.2.46", s)
    pada_merge(s)
    if s.terms:
        s.terms[0].tags.update({"prātipadika", "anga", "pulliṅga"})
    return s


def derive_aBUt() -> State:
    """भू + लुङ् 3sg → अभूत् (३.२.११०, च्लि/सिच्, २.४.७७, ६.४.७१)."""
    return derive_tinanta("BU", "luG", "kartari", 3, 1)


def derive_upAgamat() -> State:
    """उप+आङ्+गम् + लुङ् 3sg → उपागमत् (३.१.५५ अङ्, ६.४.७१ अट्, ६.१.१०१)."""
    return derive_tinanta("gam", "luG", "kartari", 3, 1, upasargas=["upa", "A"])


def derive_nfpaH() -> State:
    """नृ + पा + क (३.२.३) → नृपः."""
    s = build_dhatu_state("pA")
    nf = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("nf")),
        tags={"upapada", "anga", "prātipadika"},
        meta={"upadesha_slp1": "nf"},
    )
    s.terms = [nf] + s.terms
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "ka"
    s.meta["krt_artha"] = "kartari"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.2.3", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = P00_anga_samjna_6_4_1(s)
    s = apply_rule("6.4.64", s)
    s = apply_rule("2.4.71", s)
    s = _merge_pratipadika(s)
    return _prathama(s)


def derive_vibuDasaKaH() -> State:
    """वि+बुध+क (३.१.१३५) and सखि+टच् (५.४.९१, ६.४.१४८) → विबुधसखः."""
    s = build_dhatu_state("buD")
    vi = Term(
        kind="upasarga",
        varnas=list(parse_slp1_upadesha_sequence("vi")),
        tags={"upasarga", "pratyaya"},
        meta={"upadesha_slp1": "vi"},
    )
    s.terms = [vi] + s.terms
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "ka"
    s = apply_rule("1.4.59", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.1.135", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = _merge_pratipadika(s)

    sakhi = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("saKi")),
        tags={"anga", "prātipadika", "samasa"},
        meta={"upadesha_slp1": "saKi"},
    )
    s.terms.append(sakhi)
    s = apply_rule("5.4.91", s)
    s = P00_krt_it_lopa(s)  # 1.3.7 चुटू + 1.3.3 (टच्)
    s = apply_rule("6.4.1", s)
    s = apply_rule("6.4.129", s)
    s = apply_rule("6.4.148", s)
    s = _merge_pratipadika(s)
    return _prathama(s)


def derive_paraMtapaH() -> State:
    """पर + ताप् + खच् (३.२.३९, ६.४.९४, ६.३.६७, ८.३.२३) → परंतपः."""
    s = build_dhatu_state("tAp")
    s.terms[0].meta["upadesha_slp1"] = "tap"
    para = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("para")),
        tags={"upapada", "anga", "prātipadika"},
        meta={"upadesha_slp1": "para"},
    )
    s.terms = [para] + s.terms
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "Kac"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.2.39", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = P00_anga_samjna_6_4_1(s)
    s = apply_rule("6.4.94", s)
    s = apply_rule("6.3.67", s)
    s = _merge_pratipadika(s)
    s = _prathama(s)
    s = apply_rule("8.3.23", s)
    return s


def derive_guNAH() -> State:
    """गुण + घञ् (३.३.१९ / ३.३.१६) → गुणाः."""
    s = build_dhatu_state("guRa")
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "GaY"
    s.meta["krt_artha"] = "karmani"
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.3.18", s)
    s = apply_rule("3.3.19", s)
    s = apply_rule("3.3.16", s)
    s = _krt_it_lasaku(s)
    s = apply_rule("3.4.114", s)
    s = apply_rule("7.2.116", s)
    s = _merge_pratipadika(s)
    return _prathama(s, vacana=3)


def derive_varaH() -> State:
    """वृ + अप् (३.३.५८) → वरः."""
    s = build_dhatu_state("vfY")
    s.meta["derivation_class"] = "krdanta"
    s.meta["krt_upadesha_slp1"] = "ap"
    s.meta["krt_artha"] = "karmani"
    s = apply_rule("1.3.1", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = P06a_pratyaya_adhikara_3_1_1_to_3(s)
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.3.58", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("3.4.114", s)
    s = P00_anga_samjna_6_4_1(s)
    s = P00_guna_rapara_ayadi(s)
    s = _merge_pratipadika(s)
    return _prathama(s)


def derive_sanAtanaH() -> State:
    """सना + ट्यु/तुट् (४.३.२३, ७.१.१) → सनातनः."""
    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("sanA")),
        tags={"anga", "prātipadika", "avyaya"},
        meta={"upadesha_slp1": "sanA"},
    )
    s = State(terms=[stem], meta={"derivation_class": "taddhita"}, trace=[])
    s = apply_rule("4.3.23", s)
    s = apply_rule("1.3.3", s)
    s = apply_rule("1.3.9", s)
    s = apply_rule("7.1.1", s)
    s = _merge_pratipadika(s)
    return _prathama(s)


WORDS = (
    ("अभूत्", "derive_aBUt", "भू + लुङ्"),
    ("नृपः", "derive_nfpaH", "नृ + पा + क"),
    ("विबुधसखः", "derive_vibuDasaKaH", "विबुध + सखि + टच्"),
    ("परंतपः", "derive_paraMtapaH", "पर + ताप् + खच्"),
    ("गुणाः", "derive_guNAH", "गुण + घञ्"),
    ("वरः", "derive_varaH", "वृ + अप्"),
    ("सनातनः", "derive_sanAtanaH", "सना + ट्यु"),
    ("उपागमत्", "derive_upAgamat", "उप+आङ्+गम् + लुङ्"),
)
