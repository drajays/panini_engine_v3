"""
Conflicts between applicable sūtras are **not** resolved by list order.

This module is a thin, documented re-export of :mod:`engine.resolver` and
:mod:`engine.gates` (tripāḍī, pratiṣedha, SOI/DOI, ``CONFLICT_OVERRIDES``).
Use :func:`resolve` from here in audit scripts so the intended architecture
stays obvious.
"""
from __future__ import annotations

from engine.gates import asiddha_violates, is_blocked, is_tripadi
from engine.resolver import CONFLICT_OVERRIDES, UnresolvedConflict, resolve

__all__ = [
    "CONFLICT_OVERRIDES",
    "UnresolvedConflict",
    "asiddha_violates",
    "is_blocked",
    "is_tripadi",
    "resolve",
]
