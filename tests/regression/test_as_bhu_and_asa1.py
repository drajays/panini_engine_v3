"""adādi as → bhū before ārdhadhātuka (2.4.52: the old set listed āsa~ by mistake), bhvādi asa~ keeps its a (6.4.111/7.4.50/6.4.119 are adādi-only),
7.3.77 gam/iṣ in laṅ after the aṭ."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


def _run(dhatu, gana, lakara, p, v, pada="parasmai"):
    ref = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == dhatu and r.get("gana") == gana)["id"]
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lakara, p, v), pada=pada)), "", ref, 250).surface


@pytest.mark.parametrize("dhatu,gana,lakara,p,v,want", [
    ("asa~", 2, "liT", 3, 1, "baBUva"), ("asa~", 2, "luG", 3, 1, "aBUt"), ("asa~", 2, "lRT", 3, 1, "Bavizyati"), ("asa~", 2, "AsIrliG", 3, 1, "BUyAt"),
    ("asa~", 1, "laT", 3, 2, "asataH"), ("asa~", 1, "lRT", 3, 1, "asizyati"),
    ("gamx~", 1, "laG", 3, 1, "agacCat"), ("izu~", 6, "laG", 3, 1, "EcCat"),
])
def test_cell(dhatu, gana, lakara, p, v, want):
    assert _run(dhatu, gana, lakara, p, v) == want
