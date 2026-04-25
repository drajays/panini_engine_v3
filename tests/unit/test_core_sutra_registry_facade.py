from __future__ import annotations

import pytest

import sutras  # noqa: F401

from core.sutra_registry import SUTRA_REGISTRY, get_sutra, registry_size


def test_core_registry_matches_engine() -> None:
    from engine.registry import SUTRA_REGISTRY as ER

    assert SUTRA_REGISTRY is ER
    assert registry_size() == len(ER) > 100


def test_get_sutra_1_1_1() -> None:
    rec = get_sutra("1.1.1")
    assert rec.sutra_id == "1.1.1"
