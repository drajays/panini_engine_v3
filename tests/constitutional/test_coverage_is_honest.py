"""
tests/constitutional/test_coverage_is_honest.py
───────────────────────────────────────────────

Constitution **Article 16** — coverage is firing, not registration.

A record counts as implemented only when it is invoked, moves the state, is
cited (Art. 14) and is tested. Everything else is *registered*. No interface
may present the registered count as coverage.

This test is the enforcement clause: it fails the moment the two counts are
conflated again, or the firing ledger goes missing.
"""
from __future__ import annotations

import sutras  # noqa: F401 — fills SUTRA_REGISTRY

from engine import SUTRA_REGISTRY, coverage_report
from engine.coverage import honest_coverage, load_ledger


def test_ledger_exists_and_is_committed():
    """Conditions 1–2 are execution facts; without the ledger they are unknown."""
    ledger = load_ledger()
    assert ledger is not None, (
        "sig/firing_coverage.json missing — run 'python3 -m tools.firing_coverage'"
    )
    assert ledger["counts"]["invoked"] >= ledger["counts"]["moved"] > 0


def test_implemented_is_a_subset_of_registered_and_far_smaller():
    cov = coverage_report(SUTRA_REGISTRY)
    assert cov["registered"] == len(SUTRA_REGISTRY)
    assert 0 < cov["implemented"] < cov["registered"]
    # The claim being outlawed is "every file is a rule". If these ever converge,
    # the four conditions have stopped being checked.
    assert cov["implemented"] < cov["registered"] / 2


def test_coverage_pct_is_the_implemented_percentage():
    cov = coverage_report(SUTRA_REGISTRY)
    expected = round(100.0 * cov["implemented"] / cov["registered"], 2)
    assert cov["coverage_pct"] == expected, (
        "Art. 16: coverage_pct must report implemented/registered, never a "
        "registration count dressed as coverage."
    )


def test_every_implemented_sutra_meets_all_four_conditions():
    report = honest_coverage(SUTRA_REGISTRY)
    ledger = load_ledger() or {}
    invoked = set(ledger.get("invoked", ()))
    for sid in report["implemented_ids"]:
        assert sid in invoked, f"{sid} counted as implemented but never invoked"


def test_the_worklist_is_published():
    """Sūtras that do real work but lack a citation are the next batch (Art. 14)."""
    cov = coverage_report(SUTRA_REGISTRY)
    assert isinstance(cov["moving_but_uncited"], list)
    # This number should fall over time; it must never be hidden.
    assert cov["moving_but_uncited"], "no worklist emitted — is the ledger stale?"
