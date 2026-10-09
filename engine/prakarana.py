"""engine/prakarana.py — the prakaraṇa modules (v3 Art. 23 §6, AMENDMENT 24).

Every sūtra belongs to at least one prakaraṇa, as Pushpa Dixit teaches them and as Pāṇini's own data delimits them (adhikāra head or anuvṛtti
descent). The map is generated in the brain (``ashtadhyayi-ai/graph/build_prakarana.py``) and vendored here as data; ``make prakarana-sync`` refreshes it.

This module only *reads* the map. It decides nothing yet: the scheduler still scans the registry (ROADMAP / docs/PRAKARANA_MACHINE_PLAN.md P1–P2 will
use it as the eligibility index, shadow-run first). Status per prakaraṇa: ``data`` (defined by the pāṭha), ``hyp`` (range guessed, needs a concept
card), ``pending`` (extent not found yet).
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

_PATH = Path(__file__).resolve().parent.parent / "data" / "inputs" / "prakarana_map.json"


@lru_cache(maxsize=1)
def _map() -> dict:
    return json.loads(_PATH.read_text(encoding="utf-8"))


def all_modules() -> dict[str, dict]:
    """``{P-id: {name, status, defined_by, start, end, n, sutras, cards, her_extent?}}``."""
    return _map()["prakaranas"]


def members(pid: str) -> list[str]:
    return all_modules()[pid]["sutras"]


def of(sutra_id: str) -> list[str]:
    """The prakaraṇa ids a sūtra belongs to (≥ 1 for every sūtra — see tests/constitutional/test_prakarana_complete.py)."""
    return _map()["sutra_to_prakarana"].get(sutra_id, [])
