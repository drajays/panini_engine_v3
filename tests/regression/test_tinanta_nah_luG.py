"""8.2.34 naho dhaḥ (apavāda of 8.2.31) in the autonomous loop: Raha~ (nahyati) luṅ → anAtsIt, anAdDAm. Vidyut agrees."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("pu,vc,want", [(3, 1, "anAtsIt"), (3, 2, "anAdDAm"), (1, 1, "anAtsam")])
def test_nah_luG(pu, vc, want):
    r = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == "Raha~" and r.get("gana") == 4)
    ref = r.get("id") or "Raha~"
    assert run_autonomously(start_state(NS(kind="tinanta", args=(ref, "luG", pu, vc), pada="parasmai")), "", ref, 250).surface == want
