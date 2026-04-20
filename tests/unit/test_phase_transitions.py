"""
tests/unit/test_phase_transitions.py
──────────────────────────────────────

Tests for the three-phase model (v3.1 amendment).
"""
from __future__ import annotations

import pytest

from engine       import set_phase, PhaseError
from engine.state import State


def test_default_phase_is_angakarya():
    s = State()
    assert s.phase == "angakarya"
    assert s.tripadi_zone is False


def test_forward_transitions_valid():
    s = State()
    set_phase(s, "sandhi")
    assert s.phase == "sandhi"
    assert s.tripadi_zone is False
    set_phase(s, "tripadi")
    assert s.phase == "tripadi"
    assert s.tripadi_zone is True


def test_backward_transition_raises():
    s = State()
    set_phase(s, "sandhi")
    with pytest.raises(PhaseError):
        set_phase(s, "angakarya")


def test_skip_forward_transition_raises():
    s = State()
    # Cannot jump angakarya → tripadi directly.
    with pytest.raises(PhaseError):
        set_phase(s, "tripadi")


def test_self_transition_is_noop():
    s = State()
    set_phase(s, "sandhi")
    n_trace_before = len(s.trace)
    set_phase(s, "sandhi")  # idempotent — no error, no trace row
    assert s.phase == "sandhi"
    assert len(s.trace) == n_trace_before


def test_unknown_phase_raises():
    s = State()
    with pytest.raises(PhaseError):
        set_phase(s, "samasa")


def test_phase_transition_logged():
    s = State()
    set_phase(s, "sandhi")
    last = s.trace[-1]
    assert last["sutra_id"] == "__PHASE__"
    assert last["phase_from"] == "angakarya"
    assert last["phase_to"]   == "sandhi"
