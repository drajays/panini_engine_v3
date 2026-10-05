"""ṇijanta curādi through the loop (3.1.35 ām in liṭ, caṅ-luṅ with dvitva after the aṭ, 6.4.51 before every ārdhadhātuka, 7.4.2 ṛdit,
7.1.4 not after caṅ, 6.4.120 liṭ only) and brū → vac (2.4.53), vac/hve/lip aṅ (3.1.52/53, vac+um 7.4.20)."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


def _run(dhatu, gana, lakara, p, v, pada):
    ref = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == dhatu and r.get("gana") == gana)["id"]
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lakara, p, v), pada=pada)), "", ref, 250).surface


@pytest.mark.parametrize("dhatu,gana,lakara,p,v,pada,want", [
    ("cura~", 10, "luG", 3, 1, "parasmai", "acUcurat"), ("kudf~", 10, "luG", 3, 1, "parasmai", "acukodat"), ("kudf~", 10, "luG", 3, 3, "parasmai", "acukodan"),
    ("laqa~", 10, "luG", 3, 1, "parasmai", "alIlaqat"), ("kudf~", 10, "AsIrliG", 3, 1, "parasmai", "kodyAt"),
    ("kudf~", 10, "liT", 3, 1, "parasmai", "kodayAYcakAra"),
    ("brUY", 2, "liT", 3, 1, "parasmai", "uvAca"), ("brUY", 2, "luT", 3, 1, "parasmai", "vaktA"), ("brUY", 2, "luG", 3, 1, "parasmai", "avocat"),
    ("vaca~", 2, "luG", 3, 1, "parasmai", "avocat"), ("hveY", 1, "luG", 3, 1, "parasmai", "ahvat"), ("lipa~", 6, "luG", 3, 1, "parasmai", "alipat"),
])
def test_cell(dhatu, gana, lakara, p, v, pada, want):
    assert _run(dhatu, gana, lakara, p, v, pada) == want
