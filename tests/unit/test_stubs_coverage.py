"""
tests/unit/test_stubs_coverage.py
───────────────────────────────────

Tests for make_stub() / coverage_report() (v3.1 amendment).
"""
from __future__ import annotations

import pytest

from engine import (
    SutraType, SUTRA_REGISTRY, coverage_report, make_stub, is_stub,
    register_sutra,
)
import sutras  # noqa: F401 — populate registry


def test_make_stub_for_every_type_registers_cleanly():
    for t in SutraType:
        sid = f"0.9.{t.value}"
        SUTRA_REGISTRY.pop(sid, None)
        stub = make_stub(sid, t, text_dev=f"[stub {t.name}]")
        assert is_stub(stub)
        register_sutra(stub)
        assert SUTRA_REGISTRY[sid] is stub
        SUTRA_REGISTRY.pop(sid, None)


def test_coverage_report_shape():
    cov = coverage_report(SUTRA_REGISTRY)
    for key in ("registered", "implemented", "coverage_pct", "conditions",
                "moving_but_uncited", "stubs", "scaffolded", "by_type"):
        assert key in cov
    assert cov["registered"] == cov["total"] == len(SUTRA_REGISTRY)
    assert cov["stubs"] == 0              # no make_stub() records remain
    # Art. 16: a record is not a rule. Implemented counts only sūtras that are
    # invoked, move the state, are cited and are tested — far fewer than exist.
    assert cov["implemented"] < cov["registered"]
    assert cov["scaffolded"] == cov["registered"] - cov["implemented"]


def test_coverage_report_counts_stubs_correctly():
    # Registering a stub adds a *record*, never a rule (Art. 16).
    SUTRA_REGISTRY.pop("0.8.8", None)
    baseline = coverage_report(SUTRA_REGISTRY)

    stub = make_stub("0.8.8", SutraType.VIDHI)
    register_sutra(stub)
    mid = coverage_report(SUTRA_REGISTRY)
    assert mid["registered"] == baseline["registered"] + 1
    assert mid["stubs"] == 1
    assert mid["implemented"] == baseline["implemented"]        # unchanged
    assert mid["scaffolded"] == baseline["scaffolded"] + 1

    SUTRA_REGISTRY.pop("0.8.8", None)
