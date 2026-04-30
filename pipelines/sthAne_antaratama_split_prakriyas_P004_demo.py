"""
pipelines/sthAne_antaratama_split_prakriyas_P004_demo.py — **P004** (**स्थानेऽन्तरतमः** illustrations).

Source: ``…/my_scripts/final/split_prakriyas_11/P004.json`` (paribhāṣā-illustration).

Spine (``apply_rule`` only):

  **1.1.50** — installs ``paribhasha_gates`` helpers used when choosing *ādeśa* by maximal
  place-of-articulation match (*sthāne ’ntaratamaḥ*; see ``sutra_1_1_50`` docstring).

  Then three narrow **6.1.101** (*akaḥ savarṇe dīrghaḥ*) tapes, each two *prātipadika*
  *aṅga* terms (sandhi across the term boundary), matching the classical examples cited
  under **1.1.50** in the engine docstring:

    * ``daRqa`` + ``agra`` → ``daRqAgra``
    * ``daDi`` + ``idam`` → ``daDIdam``
    * ``maDu`` + ``udayaH`` → ``maDUdayaH``

JSON mixes Devanagarī in titles with SLP1 targets; this recipe uses SLP1 tapes only.
No new **1.1.50** / **6.1.101** files — both sūtras already exist.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_P004() -> Term:
    """Minimal *prātipadika* witness so the derivation state is non-empty before **1.1.50**."""
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("a")),
        tags={"anga", "prātipadika", "prakriya_P004_sthAne_antaratama_demo"},
        meta={"upadesha_slp1": "a"},
    )


def _two_pratipadika_angas(left_slp1: str, right_slp1: str) -> list[Term]:
    return [
        Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence(left_slp1)),
            tags={"anga", "prātipadika"},
            meta={"upadesha_slp1": left_slp1},
        ),
        Term(
            kind="prakriti",
            varnas=list(parse_slp1_upadesha_sequence(right_slp1)),
            tags={"anga", "prātipadika"},
            meta={"upadesha_slp1": right_slp1},
        ),
    ]


def derive_sthAne_antaratama_split_prakriyas_P004() -> State:
    s = State(terms=[_witness_P004()], meta={}, trace=[])
    s.meta["prakriya_P004_paribhasha_1_1_50_then_6_1_101_illustrations"] = True

    s = apply_rule("1.1.50", s)

    for left, right in (
        ("daRqa", "agra"),
        ("daDi", "idam"),
        ("maDu", "udayaH"),
    ):
        s.terms = _two_pratipadika_angas(left, right)
        s = apply_rule("6.1.101", s)

    return s


__all__ = [
    "derive_sthAne_antaratama_split_prakriyas_P004",
    "_witness_P004",
    "_two_pratipadika_angas",
]
