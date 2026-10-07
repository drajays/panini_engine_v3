"""
engine/registries/subanta_origin_lookup.py — read-only origin facts for subanta stems.

``pipelines.subanta.derive()`` takes a bare stem string, not a Term with
derivation history, so it cannot itself know whether a stem like ``Bavat``
came from BU+śatṛ (hence ugit, 7.1.70) or whether a stem like ``kartṛ`` came
from kṛ+tṛc (hence tfc, 6.4.11). Those facts used to be either (a) a caller-
supplied flag the caller had to already know (``ugit=True``), or (b) a
spelling-suffix guess in ``bench/ashtadhyayi_gold.py`` (any ``-vat``/``-mat``
stem assumed ugit). Neither is a lexicon; both are the shortcut CONSTITUTION
Art. 6/18 warns against — the *consequence* of a derivation (ugit-ness) fed
back in as if it were a primitive input.

This module is the structured alternative: ``data/inputs/subanta_krt_origin_lexicon.json``
declares, per stem, WHERE it came from (root + kṛt-pratyaya, or a kvip
compound) and what that implies. Still hand-curated (not yet derived live
from a kṛt pipeline — most kṛt pratyayas here, e.g. kvasu/kānac/śatṛ, don't
have one; see docs/BRAIN_1_3_12_CROSSCHECK.md and docs/LEXICON_ARCHITECTURE.md),
but it is now a declared fact file, not a guess from the string's tail.

No rule mutates this registry; callers get a read-only flags dict.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, Optional


def _repo_root() -> Path:
    # engine/registries/subanta_origin_lookup.py → engine/registries → engine → repo
    return Path(__file__).resolve().parents[2]


def _lexicon_path() -> Path:
    return _repo_root() / "data" / "inputs" / "subanta_krt_origin_lexicon.json"


@lru_cache(maxsize=1)
def _entries() -> Dict[str, Dict[str, Any]]:
    path = _lexicon_path()
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    return data.get("entries") or {}


def origin_entry(stem_slp1: str) -> Optional[Dict[str, Any]]:
    """The full declared origin record for ``stem_slp1``, or None if not in the lexicon."""
    return _entries().get(stem_slp1.strip())


def origin_flags(stem_slp1: str) -> Dict[str, bool]:
    """Just the ``flags`` dict (e.g. ``{"ugit": True}``) for ``stem_slp1``, or ``{}`` if unknown."""
    entry = origin_entry(stem_slp1)
    return dict(entry.get("flags") or {}) if entry else {}


def is_known_stem(stem_slp1: str) -> bool:
    return stem_slp1.strip() in _entries()
