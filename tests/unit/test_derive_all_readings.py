"""
pipelines.tinanta.derive_all_readings / pipelines.subanta.derive_all_readings

Thin, opt-in wrapper around engine.vikalpa.explore() over the *public*
derive() entry points (docs/FINAL_PLAN_2026-09.md item 6: "optional forms
(vikalpa) are still single-output"). derive() itself is unchanged — this is
an additive API, not a behavior change for existing callers.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine.vikalpa import Branch
from pipelines.subanta import derive as subanta_derive, derive_all_readings as subanta_all
from pipelines.tinanta import derive as tinanta_derive, derive_all_readings as tinanta_all


def test_tinanta_single_reading_matches_derive() -> None:
    """No वा rule reached ⇒ exactly one branch, identical to derive()'s own output."""
    single = tinanta_derive("BU", "laT", "kartari", 3, 1)
    branches = tinanta_all("BU", "laT", "kartari", 3, 1)
    assert len(branches) == 1
    assert isinstance(branches[0], Branch)
    assert branches[0].surface_slp1 == single.flat_slp1()
    assert branches[0].choices == ()


def test_subanta_single_reading_matches_derive() -> None:
    single = subanta_derive("rAma", 1, 1)
    branches = subanta_all("rAma", 1, 1)
    assert len(branches) == 1
    assert branches[0].surface_slp1 == single.flat_slp1()


def test_tinanta_all_readings_forwards_kwargs() -> None:
    """Keyword args (pada, upasargas, …) reach derive() through the wrapper
    exactly as they would through a direct derive() call."""
    single = tinanta_derive("kf", "laT", "kartari", 3, 1, pada="atmane")
    branches = tinanta_all("kf", "laT", "kartari", 3, 1, pada="atmane")
    assert branches[0].surface_slp1 == single.flat_slp1()


def test_subanta_all_readings_forwards_kwargs() -> None:
    single = subanta_derive("rAma", 1, 1, "strīliṅga")
    branches = subanta_all("rAma", 1, 1, "strīliṅga")
    assert branches[0].surface_slp1 == single.flat_slp1()
