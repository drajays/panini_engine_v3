"""
``core/`` — stable import surface for tooling and future pipeline wiring.

Sūtra *definitions* and registration remain in ``sutras/`` and
``engine.registry`` (CONSTITUTION: one sūtra, one file). This package
re-exports those objects so integrators can ``from core import …``
without a parallel registration table.
"""

from __future__ import annotations

from core.samjna_store import State, Term, Varna, samjna_labels
from core.sutra_registry import SUTRA_REGISTRY, get_sutra, register_sutra, registry_size
from core.transliterate import dev_to_slp1, slp1_to_dev, slp1_to_iast

__all__ = [
    "SUTRA_REGISTRY",
    "Term",
    "State",
    "Varna",
    "dev_to_slp1",
    "get_sutra",
    "register_sutra",
    "registry_size",
    "samjna_labels",
    "slp1_to_dev",
    "slp1_to_iast",
]
