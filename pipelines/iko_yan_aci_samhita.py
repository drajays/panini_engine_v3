"""
pipelines/iko_yan_aci_samhita.py — **6.1.77** *iko yaṇ aci* (adhikāra **6.1.72**).

Pedagogical *saṃhitā* pairs from the इको यणचि lesson: two *prakṛti* **Term**s,
``P00_samhita_iko_yanaci_spine`` (125 → 101 → 77), no recipe arms.

Apavāda demos: **6.1.101** (नदी+इयम्), **6.1.125** + pragṛhya (धेनू+इमे).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_samhita_iko_yanaci_spine
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


def _samhita_pair(left_slp1: str, right_slp1: str, *, left_tags: frozenset[str] | None = None) -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(left_slp1),
        tags=set(left_tags or ()),
        meta={"upadesha_slp1": left_slp1},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(right_slp1),
        tags={"nipāta"},
        meta={"upadesha_slp1": right_slp1},
    )
    return State(terms=[left, right], meta={}, trace=[])


def _derive_pair(left_slp1: str, right_slp1: str, *, left_tags: frozenset[str] | None = None) -> State:
    return P00_samhita_iko_yanaci_spine(_samhita_pair(left_slp1, right_slp1, left_tags=left_tags))


def derive_dadhi_atra() -> State:
    """दधि + अत्र → दध्यत्र (*i* → *y*)."""
    return _derive_pair("dadhi", "atra")


def derive_nadI_Urdhvam() -> State:
    """नदी + ऊर्ध्वम् → नद्यूर्ध्वम् (*ī* → *y*)."""
    return _derive_pair("nadI", "Urdhvam")


def derive_madhu_iti() -> State:
    """मधु + इति → मध्विति (*u* → *v*)."""
    return _derive_pair("madhu", "iti")


def derive_vadhU_AdesaH() -> State:
    """वधू + आदेशः → वध्वादेशः (*ū* → *v*)."""
    return _derive_pair("vadhU", "AdesaH")


def derive_pitf_icCA() -> State:
    """पितृ + इच्छा → पित्रिच्छा (*ṛ* → *r*)."""
    return _derive_pair("pitf", "icCA")


def derive_F_asya() -> State:
    """ॠ + अस्य → रस्य (*ṝ* → *r*)."""
    return _derive_pair("F", "asya")


def derive_l_AkRtiH() -> State:
    """ऌ + आकृतिः → लाकृतिः (*ḷ* → *l*)."""
    return _derive_pair("x", "AkRtiH")


def derive_nadI_iyam_savarNa_dirgha() -> State:
    """नदी + इयम् → नदीयम् (**6.1.101** blocks **6.1.77**)."""
    return _derive_pair("nadI", "iyam")


def derive_DhenU_ime_pragRhya() -> State:
    """धेनू + इमे — pragṛhya, no sandhi (**6.1.125**)."""
    return _derive_pair("DhenU", "ime", left_tags=frozenset({PRAGHYA_TERM_TAG}))


__all__ = [
    "derive_dadhi_atra",
    "derive_nadI_Urdhvam",
    "derive_madhu_iti",
    "derive_vadhU_AdesaH",
    "derive_pitf_icCA",
    "derive_F_asya",
    "derive_l_AkRtiH",
    "derive_nadI_iyam_savarNa_dirgha",
    "derive_DhenU_ime_pragRhya",
]
