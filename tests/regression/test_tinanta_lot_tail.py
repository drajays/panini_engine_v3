"""Tail fixes of 2026-10-06 (all agree with Vidyut): śānac (3.1.83) takes śnā's slot — no śap, no guṇa (iza~ loṭ izARa);
laghūpadha ṛ must be the upadhā (bfhi~ lṛṅ abfMhizyat, not *abarMhizyat)."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("root,gana,lak,pu,vc,want", [("iza~", 9, "loT", 2, 1, "izARa"), ("bfhi~", 1, "lRG", 3, 1, "abfMhizyat"), ("tfnhU~", 6, "lRG", 1, 1, "atfMhizyam")])
def test_tail(root, gana, lak, pu, vc, want):
    r = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == root and r.get("gana") == gana)
    ref = r.get("id") or root
    assert run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada="parasmai")), "", ref, 250).surface == want
