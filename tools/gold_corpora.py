"""
Reference gold corpora (CONSTITUTION Art. 6 firewall — read only from here).

``tools/validate_engine_against_source`` and ``tools/sig_benchmark`` use
this module to list JSON under ``data/reference/`` (subanta by directory,
or recursive scans for ``sig_benchmark`` / future *kṛdanta* / *taddhita*
trees).
"""
from __future__ import annotations

from pathlib import Path
from typing import List

_ROOT = Path(__file__).resolve().parent.parent


def data_reference_root() -> Path:
    return _ROOT / "data" / "reference"


def subanta_gold_dir() -> Path:
    return _ROOT / "data" / "reference" / "subanta_gold"


def tinanta_gold_dir() -> Path:
    return _ROOT / "data" / "reference" / "tinanta_gold"


def list_subanta_gold_jsons(base: Path | None = None) -> List[Path]:
    d = base or subanta_gold_dir()
    return sorted(p for p in d.glob("*.json") if p.is_file())


def list_tinanta_gold_jsons(base: Path | None = None) -> List[Path]:
    d = base or tinanta_gold_dir()
    return sorted(p for p in d.glob("*.json") if p.is_file())


def list_reference_gold_jsons(
    base: Path | None = None,
) -> List[Path]:
    """
    Recursively list ``*.json`` under ``data/reference/`` (or *base*).
    ``sig_benchmark`` filters contents (``cells`` + ``stem_slp1``, or
    ``recipe``, or ``steps`` + ``surface_target_slp1``, etc.).
    """
    root = (base or data_reference_root()).resolve()
    if not root.is_dir():
        return []
    return sorted(
        p for p in root.rglob("*.json")
        if p.is_file()
    )
