"""7.3.71 otaH Syani — the final o of an anga is lost before Syan (do, so, Co)."""
import pytest
from types import SimpleNamespace as NS
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,want", [("04.0043", "dyati"), ("04.0040", "Syati"), ("04.0041", "Cyati")])
def test_o_lopa_before_syan(dhatu, want):
    case = NS(kind="tinanta", args=(dhatu, "laT", 3, 1), pada=None)
    assert run_autonomously(start_state(case), want, want, 250).surface == want
