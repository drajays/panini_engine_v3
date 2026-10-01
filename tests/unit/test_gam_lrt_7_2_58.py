"""7.2.58 गमेरिट् परस्मैपदेषु — Kāśikā: गमिष्यति, अगमिष्यत्; pratyudāharaṇa चेष्यति.

Found by bench/run.py against Vidyut: 7.2.10 blocked 7.2.35 and nothing
re-granted iṭ, so the engine gave *gamsyati*.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401
from pipelines.tinanta import derive

LRT = ["gamizyAmi", "gamizyAvaH", "gamizyAmaH",
       "gamizyasi", "gamizyaTaH", "gamizyaTa",
       "gamizyati", "gamizyataH", "gamizyanti"]


@pytest.mark.parametrize("i,gold", list(enumerate(LRT)))
def test_gam_lrt_parasmaipada(i, gold):
    purusha, vacana = 1 + i // 3, 1 + i % 3
    assert derive("gamx~", "lRT", "kartari", purusha, vacana).flat_slp1() == gold


def test_gam_lrg_parasmaipada():
    assert derive("gamx~", "lRG", "kartari", 3, 1).flat_slp1() == "agamizyat"


def test_gam_lut_8_3_24_makara():
    """8.3.24 covers म् (anuvṛtti मः from 8.3.23): गम्+ता → गंता → 8.4.58 गन्ता."""
    assert derive("gamx~", "luT", "kartari", 3, 1).flat_slp1() == "gantA"
    assert derive("gamx~", "luT", "kartari", 3, 3).flat_slp1() == "gantAraH"


def test_7_2_58_is_in_the_trace_after_7_2_10():
    s = derive("gamx~", "lRT", "kartari", 3, 1)
    applied = [e["sutra_id"] for e in s.trace if e["status"] == "APPLIED"]
    assert applied.index("7.2.10") < applied.index("7.2.58")


def test_atmanepada_keeps_7_2_10():
    s = derive("gamx~", "lRT", "kartari", 3, 1, upasargas=["sam"], pada="atmane")
    assert "iz" not in s.flat_slp1()


def test_other_anudatta_root_keeps_7_2_10():
    assert derive("nIY", "lRT", "kartari", 3, 1).flat_slp1() == "nezyati"
