"""
*śālā* + *tatra bhava* → *śālīya* / *mālā* → *mālīya*.

Pedagogical *śāstra* *śr̥ṅkhalā* and glass-box notes are in ``git`` history
and the engine wiki; the executable spine lives only in
``core.canonical_pipelines`` (CONSTITUTION Art. 7, 11: recipes call the dispatcher only).
"""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import (
    build_malIya_initial_state,
    build_salIya_initial_state,
    derive_mAlIya,
    derive_salIya,
    derive_salIyaH,
)

__all__ = [
    "build_malIya_initial_state",
    "build_salIya_initial_state",
    "derive_mAlIya",
    "derive_salIya",
    "derive_salIyaH",
]
