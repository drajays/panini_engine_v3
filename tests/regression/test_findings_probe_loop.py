"""Autonomous loop vs the Kāśikā forms behind the brain's ENGINE_FINDINGS (cases live in tools/findings_probe.py).

Expected forms are the Kāśikā/Kaumudī udāharaṇas the carding job recorded (Art. 19), not engine output.
Known gaps are strict xfails: when one starts passing, move it out of KNOWN_GAPS.
"""
from __future__ import annotations

from types import SimpleNamespace as NS

import pytest

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state
from tools.findings_probe import CASES

KNOWN_GAPS = {
    ("BvAdi_01_1163", "liT", 3, 1),       # hve: 6.1.33 abhyastasya ca not modelled (juhAva)
    ("BvAdi_01_1162", "liT", 3, 1),       # vye: 6.1.46 na vyo liṭi + 6.1.17 for vyeñ (vivyAya)
    ("JuhotyAdi_03_0002", "loT", 1, 1),   # bhī: guṇa before pit āni (biBayAni)
    ("Adadi_02_0070", "laT", 3, 2),       # śās: 6.4.34 śāsa id aṅhaloḥ is a gate stub (SizwaH)
}


def _id(case):
    ref, lak, pu, vc, pada, _ = case
    return f"{ref}-{lak}-{pu}{vc}{'-' + pada if pada else ''}"


@pytest.mark.parametrize("case", CASES, ids=[_id(c) for c in CASES])
def test_loop_matches_kashika(case):
    ref, lak, pu, vc, pada, want = case
    got = run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250).surface
    if (ref, lak, pu, vc) in KNOWN_GAPS:
        if got in want:
            pytest.fail(f"{ref} {lak} {pu}-{vc} now gives {got}: remove it from KNOWN_GAPS")
        pytest.xfail(f"known rule gap: loop gives {got}, Kāśikā {sorted(want)}")
    assert got in want, f"{ref} {lak} {pu}-{vc}: loop gave {got}, Kāśikā {sorted(want)}"
