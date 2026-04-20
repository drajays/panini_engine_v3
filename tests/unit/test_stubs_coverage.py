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
    assert "total" in cov
    assert "implemented" in cov
    assert "stubs" in cov
    assert "coverage_pct" in cov
    assert "by_type" in cov
    # All registry entries are real (non-stub) currently.
    assert cov["stubs"] == 0
    assert cov["implemented"] == cov["total"] == len(SUTRA_REGISTRY)
    assert cov["coverage_pct"] == 100.0


def test_coverage_report_counts_stubs_correctly():
    # Temporarily insert a stub, check coverage drops by 1.
    SUTRA_REGISTRY.pop("0.8.8", None)
    baseline = coverage_report(SUTRA_REGISTRY)

    stub = make_stub("0.8.8", SutraType.VIDHI)
    register_sutra(stub)
    mid = coverage_report(SUTRA_REGISTRY)
    assert mid["total"] == baseline["total"] + 1
    assert mid["stubs"] == 1
    assert mid["implemented"] == baseline["total"]

    SUTRA_REGISTRY.pop("0.8.8", None)
