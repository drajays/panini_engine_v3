"""7.2.73 yamaramanamātāṃ sak ca — AMENDMENT_19 (2026-10-06). Vidyut agrees."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("root,gana,pu,vc,want", [("Rama~", 1, 3, 1, "anaMsIt"), ("Rama~", 1, 1, 1, "anaMsizam"), ("yA", 2, 3, 1, "ayAsIt")])
def test_sak_iT(root, gana, pu, vc, want):
    r = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == root and r.get("gana") == gana)
    ref = r.get("id") or root
    assert run_autonomously(start_state(NS(kind="tinanta", args=(ref, "luG", pu, vc), pada="parasmai")), "", ref, 250).surface == want
