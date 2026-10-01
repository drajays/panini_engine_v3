"""Ratchets: unaccounted form changes in traces (Art. 11) and placeholder sūtra
files may only go down. Lower the ceilings when a fix lands."""
from __future__ import annotations

from tools.glassbox_gaps import all_gaps, placeholder_files

MAX_TRACE_GAPS = 48
MAX_PLACEHOLDERS = 915


def test_unaccounted_form_changes_do_not_grow():
    n = sum(len(v) for v in all_gaps().values())
    assert n <= MAX_TRACE_GAPS, (
        f"{n} form changes with no sūtra step (ceiling {MAX_TRACE_GAPS}); "
        "route the mutation through apply_rule — see python3 -m tools.glassbox_gaps --list")


def test_placeholder_sutras_do_not_grow():
    n = len(placeholder_files())
    assert n <= MAX_PLACEHOLDERS, (
        f"{n} placeholder sūtra files (ceiling {MAX_PLACEHOLDERS}); a new sūtra must do its operation")
