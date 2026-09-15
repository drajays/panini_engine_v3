"""
bench/grids.py — the form grids both engines are asked to derive.

A grid is a list of cells, each a dict that either engine can act on. Keeping
the grid in one place is what makes the comparison reproducible: the oracle
runner and our runner read the same definition, so a disagreement is about
grammar, never about which cells were tried.
"""
from __future__ import annotations

from typing import Any, Iterator

# Stems with a cited gold paradigm in data/reference/subanta_gold/.
SUBANTA_STEMS: tuple[tuple[str, str], ...] = (
    ("rAma", "pum"),
    ("hari", "pum"),
    ("SamBu", "pum"),
    ("guru", "pum"),
    ("sarva", "pum"),
    ("anya", "pum"),
    ("jYAna", "napumsaka"),
    ("rADA", "stri"),
)

# kartari, the lakāras our tiṅanta pipeline claims. The dhātu is given as its
# *aupadeśika* form exactly as data/inputs/dhatupatha_upadesha.json carries it,
# so both engines are asked about the same root: a mismatched upadeśa produces
# a disagreement about spelling, not about grammar.
TINANTA_DHATUS: tuple[tuple[str, int], ...] = (
    ("BU", 1),        # 01.0001  भू    सत्तायाम्
    ("gamx~", 1),     # 01.1137  गम्   गतौ
    ("pA", 1),        # 01.0468  पा    पाने
    ("nIY", 1),       # नी    नयने
    ("qukfY", 8),     # 08.0010  कृ    करणे
)
# This engine's own lakāra spellings (data/inputs/tin_upadesha.json keys);
# bench/oracle_vidyut.py maps them to Vidyut's names. Asking either engine in
# the other's spelling produces a KeyError, not a disagreement.
LAKARAS: tuple[str, ...] = ("laT", "laG", "liT", "lRT", "loT")


def subanta_cells() -> Iterator[dict[str, Any]]:
    for stem, linga in SUBANTA_STEMS:
        for vibhakti in range(1, 9):
            for vacana in range(1, 4):
                yield {
                    "kind": "subanta",
                    "key": f"subanta:{stem}:{linga}:{vibhakti}:{vacana}",
                    "stem": stem,
                    "linga": linga,
                    "vibhakti": vibhakti,
                    "vacana": vacana,
                }


def tinanta_cells() -> Iterator[dict[str, Any]]:
    for dhatu, gana in TINANTA_DHATUS:
        for lakara in LAKARAS:
            for purusha in range(1, 4):
                for vacana in range(1, 4):
                    yield {
                        "kind": "tinanta",
                        "key": f"tinanta:{dhatu}:{lakara}:{purusha}:{vacana}",
                        "dhatu": dhatu,
                        "gana": gana,
                        "lakara": lakara,
                        "purusha": purusha,
                        "vacana": vacana,
                    }


def all_cells() -> list[dict[str, Any]]:
    return [*subanta_cells(), *tinanta_cells()]
