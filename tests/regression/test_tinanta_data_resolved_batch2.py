"""Cells settled by the ashtadhyayi.com sūtra data / Vidyut agreement (AMENDMENT 18/19): as laṭ/laṅ/loṭ (6.4.111 only before a
weak ending; 7.3.96 īṭ after as; 6.4.119 एधि/धेहि), han (2.4.42 vadha, 6.4.36 jahi, 6.4.98+7.3.54 aghnan), ghu āśīr e (6.4.67),
ksa-luṅ (3.1.45, no jus), 8.3.13+6.3.111 lopa+dīrgha, vidhi-liṅ ātmane 1sg śyan (3.1.68 sees the sthānī)."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


def _run(dhatu, gana, lakara, p, v, pada):
    ref = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == dhatu and r.get("gana") == gana)["id"]
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lakara, p, v), pada=pada)), "", ref, 250).surface


@pytest.mark.parametrize("dhatu,gana,lakara,p,v,pada,want", [
    ("asa~", 2, "laT", 3, 1, "parasmai", "asti"), ("asa~", 2, "laG", 3, 1, "parasmai", "AsIt"), ("asa~", 2, "laG", 2, 1, "parasmai", "AsIH"),
    ("asa~", 2, "loT", 1, 2, "parasmai", "asAva"), ("asa~", 2, "loT", 2, 1, "parasmai", "eDi"),
    ("hana~", 2, "AsIrliG", 3, 1, "parasmai", "vaDyAt"), ("hana~", 2, "loT", 2, 1, "parasmai", "jahi"), ("hana~", 2, "laG", 3, 3, "parasmai", "aGnan"),
    ("quDAY", 3, "AsIrliG", 3, 1, "parasmai", "DeyAt"), ("quDAY", 3, "loT", 2, 1, "parasmai", "Dehi"), ("qudAY", 3, "loT", 2, 1, "parasmai", "dehi"),
    ("duha~", 2, "luG", 3, 1, "parasmai", "aDukzat"), ("duha~", 2, "luG", 3, 3, "parasmai", "aDukzan"),
    ("liha~", 2, "laT", 3, 2, "parasmai", "lIQaH"), ("liha~", 2, "loT", 2, 1, "parasmai", "lIQi"),
    ("Raha~", 4, "liG", 1, 1, "atmane", "nahyeya"), ("DIN", 4, "liG", 1, 1, "atmane", "DIyeya"),
])
def test_cell(dhatu, gana, lakara, p, v, pada, want):
    assert _run(dhatu, gana, lakara, p, v, pada) == want
