"""ec-final roots in liṭ: ātva (6.1.45) before dvitva (6.1.8) — AMENDMENT_19 (2026-10-06). Vidyut agrees."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("root,pu,vc,want", [("glE", 3, 1, "jaglO"), ("zwyE", 3, 1, "tastyO"), ("zwyE", 1, 3, "tastyima"), ("glE", 3, 2, "jaglatuH")])
def test_ec_root_lit(root, pu, vc, want):
    r = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == root and r.get("gana") == 1)
    ref = r.get("id") or root
    assert run_autonomously(start_state(NS(kind="tinanta", args=(ref, "liT", pu, vc), pada="parasmai")), "", ref, 250).surface == want
