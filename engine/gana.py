"""engine/gana.py — the Gaṇapāṭha as a lexical fact (data/inputs/ganapatha_full.json, built by tools/build_ganapatha_full.py).

A sūtra that says ``gargādibhyaḥ`` asks ``in_gana("gargAdiH", stem)``; the list is a given of the language, like the dhātupāṭha, never a
derived property (engine/lexicon.py). An ākṛtigaṇa is open: the file lists its members, a caller may add more."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

_PATH = Path(__file__).resolve().parent.parent / "data" / "inputs" / "ganapatha_full.json"


@lru_cache(maxsize=1)
def _all() -> dict:
    return json.loads(_PATH.read_text(encoding="utf-8"))["ganas"]


def members(name: str) -> frozenset[str]:
    return frozenset(_all()[name]["members"])


def in_gana(name: str, stem_slp1: str) -> bool:
    return stem_slp1 in members(name)


def in_gana_of_sutra(sutra_id: str, stem_slp1: str) -> bool:
    """Is the stem in a gaṇa that the Gaṇapāṭha attaches to this sūtra (``gargādibhyaḥ`` → the gaṇa filed under 4.1.105)?"""
    return any(stem_slp1 in g["members"] for g in _all().values() if g.get("sutra") == sutra_id)
