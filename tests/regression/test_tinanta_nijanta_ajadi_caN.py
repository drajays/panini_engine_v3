"""ajādi ṇijanta + caṅ (6.1.2 second ekāc doubled, before 6.4.51) — AMENDMENT_19 (2026-10-06). Vidyut agrees."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("pada,pu,vc,want", [("parasmai", 3, 1, "Awiwwat"), ("parasmai", 1, 1, "Awiwwam"), ("atmane", 1, 1, "Awiwwe")])
def test_awwa_luG(pada, pu, vc, want):
    r = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == "awwa~" and r.get("gana") == 10)
    ref = r.get("id") or "awwa~"
    assert run_autonomously(start_state(NS(kind="tinanta", args=(ref, "luG", pu, vc), pada=pada)), "", ref, 250).surface == want
