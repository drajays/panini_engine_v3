"""
Load dhātu rows from ``data/inputs/dhatupatha_upadesha.json`` for pipelines.

The file may be either a bare list (legacy) or an envelope with
``entries``, ``id_aliases``, and ``flag_overrides`` (see
``scripts/build_dhatupatha_upadesha_v3.py``).

Pipelines may set ``state.meta`` from ``flags`` (e.g. ``udatta`` for 7.2.10).
"""
from __future__ import annotations

import json
from copy import deepcopy
from functools import lru_cache
from pathlib import Path

_JSON = Path(__file__).resolve().parent.parent / "data" / "inputs" / "dhatupatha_upadesha.json"


@lru_cache(maxsize=1)
def _payload() -> dict | list:
    with open(_JSON, encoding="utf-8") as f:
        return json.load(f)


def _entries_list(raw: dict | list) -> list:
    if isinstance(raw, list):
        return raw
    return raw.get("entries") or []


def _envelope(raw: dict | list) -> dict:
    if isinstance(raw, list):
        return {"id_aliases": {}, "flag_overrides": {}, "entries": raw}
    return {
        "id_aliases": raw.get("id_aliases") or {},
        "flag_overrides": raw.get("flag_overrides") or {},
        "entries": raw.get("entries") or [],
    }


@lru_cache(maxsize=1)
def _by_id() -> dict[str, dict]:
    raw = _payload()
    env = _envelope(raw)
    return {e["id"]: e for e in env["entries"] if e.get("id")}


def get_dhatu_row(dhatu_id: str) -> dict:
    raw = _payload()
    env = _envelope(raw)
    aliases = env["id_aliases"]
    overrides = env["flag_overrides"]
    canonical_id = aliases.get(dhatu_id, dhatu_id)
    row = _by_id().get(canonical_id)
    if row is None:
        raise KeyError(f"unknown dhātu id: {dhatu_id!r}")
    out = deepcopy(row)
    # Merge pipeline-specific overrides (by request id or canonical id).
    for key in (dhatu_id, canonical_id):
        extra = overrides.get(key)
        if extra:
            out["flags"] = {**(out.get("flags") or {}), **extra}
    return out


def iter_dhatu_entries() -> list[dict]:
    """All envelope ``entries`` (read-only list of row dicts)."""
    return list(_entries_list(_payload()))


def list_dhatu_ids(*, tier: str | None = None) -> list[str]:
    """
    Stable-sorted list of ``id`` values.

    ``tier`` filters ``row['tier']`` when present (e.g. ``curated_extension``,
    ``bvadi_merged``).
    """
    ids: list[str] = []
    for e in iter_dhatu_entries():
        tid = e.get("id")
        if not tid:
            continue
        if tier is not None and e.get("tier") != tier:
            continue
        ids.append(tid)
    return sorted(ids)


def list_tfc_demo_ids() -> list[str]:
    """
    Dhātu row ids used for **tṛc** Streamlit demos (curated gaṇa extensions +
    tests). Same order as ``tests/forward/test_forward_krdanta_trc.py``.
    """
    preferred = (
        "BvAdi_ciY",
        "BvAdi_nIY",
        "BvAdi_zwuY",
        "BvAdi_DukfY",
        "BvAdi_hfY",
        "BvAdi_BU",
        "divAdi_tF",
    )
    out: list[str] = []
    for i in preferred:
        try:
            get_dhatu_row(i)
        except KeyError:
            continue
        out.append(i)
    return out
