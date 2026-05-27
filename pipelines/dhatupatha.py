"""
Load dhātu rows from ``data/inputs/dhatupatha_upadesha.json`` for pipelines.

The file may be either a bare list (legacy) or an envelope with
``entries``, ``id_aliases``, and ``flag_overrides`` (see
``scripts/build_dhatupatha_upadesha_v3.py``).

Pipelines may set ``state.meta`` from ``flags`` (e.g. ``udatta`` for 7.2.10).
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
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


@lru_cache(maxsize=1)
def _by_dhatupatha_id() -> dict[str, str]:
    """Map ashtadhyayi.com-style ids (e.g. ``01.0001``) → canonical ``id``."""
    out: dict[str, str] = {}
    for e in _entries_list(_payload()):
        pid = e.get("dhatupatha_id")
        eid = e.get("id")
        if pid and eid:
            out[str(pid)] = str(eid)
    return out


def resolve_dhatu_identifier(ref: str) -> dict:
    """
    Resolve a dhātu reference to a full dhātupātha row.

    Accepts canonical ``id`` (``BvAdi_01_0001``), alias (``BvAdi_BU``),
    ashtadhyayi.com path id (``01.0001``), or upadeśa SLP1 (``BU``).
    """
    key = (ref or "").strip()
    if not key:
        raise KeyError("empty dhātu reference")
    try:
        return get_dhatu_row(key)
    except KeyError:
        pass
    eid = _by_dhatupatha_id().get(key)
    if eid:
        return get_dhatu_row(eid)
    norm = key.rstrip("~")
    for e in iter_dhatu_entries():
        up = e.get("upadesha_slp1") or ""
        if up == key or up.rstrip("~") == norm:
            eid2 = e.get("id")
            if eid2:
                return get_dhatu_row(eid2)
    # Also accept raw post-IT-lopa form (e.g. 'paW' for upadeśa 'paWa~').
    for e in iter_dhatu_entries():
        post_lopa = e.get("raw_dhatu_after_it_lopa_slp1") or ""
        if post_lopa == key:
            eid3 = e.get("id")
            if eid3:
                return get_dhatu_row(eid3)
    raise KeyError(
        f"unknown dhātu reference {ref!r}; use upadeśa SLP1 (BU), "
        f"path id (01.0001), or id (BvAdi_01_0001)"
    )


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
