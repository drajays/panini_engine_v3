"""7.4.66 (ur at) is para over 7.4.60 (halādiḥ śeṣaḥ) on the abhyāsa: sasmāra, not *sarsmāra.
Guards the resolver's order-matters check (engine/resolver.py, purva layer)."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,want", [("smf", "sasmAra"), ("tF", "tatAra"), ("hvf", "jahvAra")])
def test_liT_3sg(dhatu, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, "liT", 1, 1))), "", dhatu, 250).surface == want
