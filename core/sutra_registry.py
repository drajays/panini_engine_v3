"""
``core.sutra_registry`` — facade over :mod:`engine.registry`.

The authoritative sūtra store is still ``SUTRA_REGISTRY`` populated at import
time from ``sutras/**/sutra_*.py`` (see ``import sutras``).  Do **not** add
a second ``register()``/``Sutra`` table here; that would fight
``CONSTITUTION.md`` (one sūtra, one file).
"""
from __future__ import annotations

from engine.registry import SUTRA_REGISTRY, get_sutra, register_sutra


def registry_size() -> int:
    return len(SUTRA_REGISTRY)


__all__ = ["SUTRA_REGISTRY", "get_sutra", "register_sutra", "registry_size"]
