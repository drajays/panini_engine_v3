"""
pipelines/recipes — Bridge recipe registry (optional fallback layer).

Tiṅanta bridges (Phase 5, 2026-05-31): all 21 former ``tinanta_bridges.py``
registrations were deleted — ``derive_autonomous_tinanta`` and ``derive()`` share
``_bootstrap_tinanta_derivation`` + ``_dispatch_tinanta_spine`` in
``pipelines/tinanta.py``.  The registry API remains for future non-tinanta bridges
if needed; it is currently empty.
"""
from __future__ import annotations

from typing import Callable

from engine.state import State

_BRIDGE_REGISTRY: dict[
    tuple[str, str],
    Callable[..., State],
] = {}


def register_bridge(
    lakara: str,
    prayoga: str,
    fn: Callable[..., State],
) -> None:
    """Register a bridge recipe for a (lakara, prayoga) derivation path."""
    _BRIDGE_REGISTRY[(lakara, prayoga)] = fn


def get_bridge(
    lakara: str,
    prayoga: str,
) -> Callable[..., State] | None:
    """Return the registered bridge for (lakara, prayoga), or None."""
    return _BRIDGE_REGISTRY.get((lakara, prayoga))


def list_bridges() -> list[tuple[str, str]]:
    """Return the list of registered (lakara, prayoga) bridges."""
    return sorted(_BRIDGE_REGISTRY.keys())
