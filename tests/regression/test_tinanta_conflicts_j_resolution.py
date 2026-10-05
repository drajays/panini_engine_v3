"""Cells settled from CONFLICTS_J_RESOLUTION.md (KV/SK quotations): 7.3.72 क्सस्याचि, 7.3.100 आदत्, 7.2.72 असावीत्/अस्तावीत्, 7.2.77/78 not laṅ ध्वम्,
3.1.37 आसाञ्चक्रे, 7.2.61/63 जहर्थ…, 6.1.50 ममौ, 6.4.98 अघसत्."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from pipelines.dhatupatha import iter_dhatu_entries
from tools.autonomy_report import run_autonomously, start_state


def _run(dhatu, gana, lakara, p, v, pada):
    ref = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == dhatu and r.get("gana") == gana)["id"]
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lakara, p, v), pada=pada)), "", ref, 250).surface


@pytest.mark.parametrize("dhatu,gana,lakara,p,v,pada,want", [
    ("duha~", 2, "luG", 1, 1, "atmane", "aDukzi"), ("duha~", 2, "luG", 3, 2, "atmane", "aDukzAtAm"), ("vizx~", 3, "luG", 3, 3, "atmane", "avikzanta"),
    ("ada~", 2, "laG", 3, 1, "parasmai", "Adat"), ("ada~", 2, "laG", 2, 1, "parasmai", "AdaH"), ("ada~", 2, "luG", 3, 1, "parasmai", "aGasat"),
    ("zwuY", 2, "luG", 3, 1, "parasmai", "astAvIt"), ("zuY", 5, "luG", 3, 1, "parasmai", "asAvIt"),
    ("Iqa~", 2, "laG", 2, 3, "atmane", "EqQvam"), ("ISa~", 2, "laG", 2, 3, "atmane", "EqQvam"),
    ("Asa~", 2, "liT", 3, 1, "atmane", "AsAYcakre"),
    ("hf", 3, "liT", 2, 1, "parasmai", "jaharTa"), ("smf", 5, "liT", 2, 1, "parasmai", "sasmarTa"), ("stfY", 5, "liT", 2, 1, "parasmai", "tastarTa"),
    ("mIY", 9, "liT", 3, 1, "parasmai", "mamO"), ("mIY", 9, "liT", 3, 2, "parasmai", "mimyatuH"),
])
def test_cell(dhatu, gana, lakara, p, v, pada, want):
    assert _run(dhatu, gana, lakara, p, v, pada) == want
