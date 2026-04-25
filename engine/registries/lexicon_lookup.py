"""
engine/registries/lexicon_lookup.py — fast cached lexical membership checks.

This module is a **read-only registry loader** for:
  - ``data/inputs/dhatupatha_upadesha.json``  (dhātu inventory)
  - ``data/inputs/sup_upadesha.json``         (sup inventory, raw upadeśa)
  - ``data/inputs/tin_upadesha.json``         (tiṅ inventory, raw upadeśa)

It supports **logical inclusion/exclusion gates** needed by:
  - **1.2.45** (*adhātu* / *apratyaya* checks)
  - **1.2.46** (vyutpanna *kṛt/taddhita/samāsa* community)

No rule mutates these registries; callers get boolean membership only.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import AbstractSet, Any, Dict, FrozenSet


def _repo_root() -> Path:
    # engine/registries/lexicon_lookup.py → engine/registries → engine → repo
    return Path(__file__).resolve().parents[2]


def _inputs_dir() -> Path:
    return _repo_root() / "data" / "inputs"


def _read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _normalize_upadesha_slp1(s: str) -> str:
    """
    Normalize raw upadeśa SLP1 for **membership** checks.

    - sup inventory uses ``~`` as anunāsika marker; for *apratyaya* checks we
      treat ``s~`` and ``s`` as the same inventory item.
    """
    return s.replace("~", "").strip()


@lru_cache(maxsize=1)
def dhatu_upadesha_slp1_set() -> FrozenSet[str]:
    data = _read_json(_inputs_dir() / "dhatupatha_upadesha.json")
    entries = data.get("entries", [])
    out: set[str] = set()
    for e in entries:
        if not isinstance(e, dict):
            continue
        for k in ("upadesha_slp1", "raw_dhatu_after_it_lopa_slp1"):
            v = e.get(k)
            if isinstance(v, str) and v.strip():
                out.add(v.strip())
    return frozenset(out)


@lru_cache(maxsize=1)
def sup_upadesha_slp1_set() -> FrozenSet[str]:
    data = _read_json(_inputs_dir() / "sup_upadesha.json")
    out: set[str] = set()
    if isinstance(data, dict):
        for k, v in data.items():
            if str(k).startswith("_"):
                continue
            if isinstance(v, str) and v.strip():
                out.add(v.strip())
                out.add(_normalize_upadesha_slp1(v))
    return frozenset(out)


@lru_cache(maxsize=1)
def tin_upadesha_slp1_set() -> FrozenSet[str]:
    data = _read_json(_inputs_dir() / "tin_upadesha.json")
    out: set[str] = set()
    if isinstance(data, dict):
        for k, v in data.items():
            if str(k).startswith("_"):
                continue
            if isinstance(v, str) and v.strip():
                out.add(v.strip())
                out.add(_normalize_upadesha_slp1(v))
    return frozenset(out)


@lru_cache(maxsize=1)
def known_pratyaya_upadesha_slp1_set() -> FrozenSet[str]:
    return frozenset(set(sup_upadesha_slp1_set()) | set(tin_upadesha_slp1_set()))


def is_in_dhatupatha(upadesha_slp1: str) -> bool:
    return upadesha_slp1.strip() in dhatu_upadesha_slp1_set()


def is_known_sup(upadesha_slp1: str) -> bool:
    s = upadesha_slp1.strip()
    return s in sup_upadesha_slp1_set() or _normalize_upadesha_slp1(s) in sup_upadesha_slp1_set()


def is_known_tin(upadesha_slp1: str) -> bool:
    s = upadesha_slp1.strip()
    return s in tin_upadesha_slp1_set() or _normalize_upadesha_slp1(s) in tin_upadesha_slp1_set()


def is_known_pratyaya(upadesha_slp1: str) -> bool:
    s = upadesha_slp1.strip()
    ks = known_pratyaya_upadesha_slp1_set()
    return s in ks or _normalize_upadesha_slp1(s) in ks

