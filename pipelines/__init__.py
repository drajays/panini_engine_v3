"""
pipelines — end-to-end derivations (subanta, tinanta, ...).

This package intentionally does **not** import individual pipeline modules at
import time. Importing submodules here creates circular dependencies once
canonical scheduling wrappers live under ``core/`` (e.g. ``core.canonical_pipelines``
imports a few pipeline helpers).

Consumers should import the concrete pipeline they need, e.g.:

  - ``from pipelines import subanta``
  - ``from pipelines.krdanta import derive_pAcakaH``
"""

from __future__ import annotations

__all__ = []
