"""6.1.17 liṭy abhyāsasyobhayeṣām: the abhyāsa of the 6.1.16 class also takes samprasāraṇa (vi-vyāca, ji-jyau), before 7.4.60
(AMENDMENT 19). 6.4.19 chv-śūṭ stands only before a jhal-initial kit/ṅit in liṭ (pa-pracCa). Evidence: ashtadhyayi.com `संविव्ययुः`."""
from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


@pytest.mark.parametrize("dhatu,gana,p,v,want", [
    ("vyaca~", 6, 3, 1, "vivyAca"), ("vyaca~", 6, 3, 2, "vivicatuH"),
    ("vyaDa~", 4, 3, 1, "vivyADa"), ("jyA", 9, 3, 1, "jijyO"), ("jyA", 9, 3, 2, "jijyatuH"),
    ("praCa~", 6, 3, 1, "papracCa"), ("praCa~", 6, 3, 2, "papracCatuH"),
    ("o~vrascU~", 6, 3, 1, "vavraSca"),
])
def test_cell(dhatu, gana, p, v, want):
    from pipelines.dhatupatha import iter_dhatu_entries
    ref = next(r for r in iter_dhatu_entries() if r["upadesha_slp1"] == dhatu and r.get("gana") == gana)["id"]
    assert run_autonomously(start_state(NS(kind="tinanta", args=(ref, "liT", p, v), pada="parasmai")), "", ref, 250).surface == want
