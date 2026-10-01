"""6.4.38 वा ल्यपि as a vyavasthita-vibhāṣā (Kāśikā: मकारान्तानां विकल्पो भवति,
अन्यत्र नित्यमेव लोपः — आगत्य/आगम्य but only आहत्य)."""
from __future__ import annotations

import sutras  # noqa: F401

from core.canonical_pipelines import P00_dhatu_upadesha_it_lopa, P00_lyap_krt
from engine.vikalpa import choose
from pipelines.agaty_gam_lyap_acah_lesson import _upasarga_a
from pipelines.krdanta import build_dhatu_state
from pipelines.subanta import _pada_merge


def _A_lyap(ref: str) -> str:
    s = build_dhatu_state(ref)
    s.terms = [_upasarga_a()] + s.terms
    s = P00_dhatu_upadesha_it_lopa(s)
    s = P00_lyap_krt(s)
    _pada_merge(s)
    return s.flat_slp1()


def test_han_lopa_is_nitya():
    assert _A_lyap("Adadi_02_0002") == "Ahatya"          # हनँ हिंसागत्योः
    with choose({"6.4.38": False}):
        assert _A_lyap("Adadi_02_0002") == "Ahatya"


def test_gam_lopa_stays_optional():
    assert _A_lyap("gamx~") == "Agatya"
    with choose({"6.4.38": False}):
        assert _A_lyap("gamx~") == "Agamya"
