"""8.2.42-8.2.57 niṣṭhā-ta (kta) of a dhātu, through the general kṛdanta path; 8.2.29 cluster-initial s before a jhal (liṭ masj)."""
import pytest

import sutras  # noqa: F401
from tools.exercise_audit import run

KTA = dict(kala="BUta", artha="karman")


def _kta(dh, expected, sid):
    sp = ("krdanta", dh, "kta", "pulliṅga", 1, 1, tuple(sorted(KTA.items())))
    branches, err = run(sp)
    assert err is None, err
    match = [seen for surf, seen in branches if surf == expected]
    assert match, f"{expected} not in {[b[0] for b in branches]}"
    assert any("APPLIED" in seen.get(sid, ()) for seen in match), f"{sid} did not fire for {expected}"


@pytest.mark.parametrize("dh,expected,sid", [
    ("07.0002", "BinnaH", "8.2.42"),
    ("01.1052", "mlAnaH", "8.2.43"),
    ("02.0056", "prARaH", "8.2.43"),
    ("09.0016", "lUnaH", "8.2.44"),
    ("09.0020", "DUnaH", "8.2.44"),
    ("04.0029", "dInaH", "8.2.45"),
    ("09.0042", "kzIRaH", "8.2.46"),
    ("04.0080", "SuzkaH", "8.2.51"),
    ("01.1061", "kzAmaH", "8.2.53"),
    ("01.1151", "pakvaH", "8.2.52"),
    ("07.0013", "vinnaH", "8.2.56"),     # the vibhāṣā: vitta is the other reading
    ("03.0003", "hrIRaH", "8.2.56"),
    ("01.1056", "DyAtaH", "8.2.57"),     # the prohibition: no na for dhyā
    ("03.0004", "pUrtaH", "8.2.57"),
])
def test_nistha(dh, expected, sid):
    _kta(dh, expected, sid)


def test_liT_masj_num_then_skoH():
    """mamaNkTa: 7.1.60 num, then 8.2.29 drops the cluster-initial s before the jhal, 8.2.30, 8.4.58."""
    branches, err = run(("tinanta", "06.0151", "liT", "kartari", 2, 1))
    assert err is None
    assert "mamaNkTa" in [b[0] for b in branches]
    seen = next(s for surf, s in branches if surf == "mamaNkTa")
    assert "APPLIED" in seen["7.1.60"] and "APPLIED" in seen["8.2.29"]


def test_luT_lRT_masj_num_before_iT_question():
    """7.1.60 num precedes 7.2.10 in the shared _it_agama: maNktA / maNkzyati only, not *maktA / *makzyati."""
    for lk, want in (("luT", "maNktA"), ("lRT", "maNkzyati")):
        branches, err = run(("tinanta", "06.0151", lk, "kartari", 3, 1))
        assert err is None and want in [b[0] for b in branches]
        assert not {"maktA", "makzyati"} & {b[0] for b in branches}
