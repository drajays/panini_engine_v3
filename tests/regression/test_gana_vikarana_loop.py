"""Other gaṇas through the loop: śap-luk (2.4.72) must not be undone by a second 3.1.68; śnam displaces śap; an apit
vikaraṇa that arrives after the tiṅ (śnu, śnā) is kit by 1.2.4 (cinuvaH, not *cenuvaH)."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [
    ("dviza~", "laT", 1, 1, "dvezmi"), ("duha~", "laT", 1, 1, "dohmi"), ("ada~", "laT", 1, 1, "admi"),
    ("ciY", "laT", 1, 2, "cinuvaH"), ("ciY", "laT", 3, 1, "cinoti"),
    ("ruDi~r", "laT", 1, 1, "ruRaDmi"), ("BU", "laT", 3, 1, "Bavati"),
])
def test_cell(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want
