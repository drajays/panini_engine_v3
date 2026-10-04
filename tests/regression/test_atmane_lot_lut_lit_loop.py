"""ātmanepada loṭ / luṭ / liṭ through the loop: 3.4.93 only for the uttama, 3.4.91 sva/Dvam kept (no second ṭeḥ-e),
2.4.85 ḍā-rau-ras for ātmanepada prathama (apavāda of 3.4.79), 3.4.81 eś/irec structural (apavāda of 3.4.79)."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,lakara,p,v,want", [
    ("eDa~", "loT", 2, 1, "eDasva"), ("eDa~", "loT", 2, 3, "eDaDvam"), ("eDa~", "loT", 1, 1, "eDE"),
    ("eDa~", "loT", 1, 2, "eDAvahE"), ("eDa~", "loT", 3, 3, "eDantAm"),
    ("eDa~", "luT", 3, 1, "eDitA"), ("eDa~", "luT", 3, 2, "eDitArO"), ("eDa~", "luT", 3, 3, "eDitAraH"),
    ("sparDa~", "liT", 3, 1, "pasparDe"), ("sparDa~", "liT", 3, 3, "pasparDire"), ("sparDa~", "liT", 3, 2, "pasparDAte"),
])
def test_cell(dhatu, lakara, p, v, want):
    assert run_autonomously(start_state(NS(kind="tinanta", args=(dhatu, lakara, p, v))), "", dhatu, 250).surface == want
