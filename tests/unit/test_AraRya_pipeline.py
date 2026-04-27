from __future__ import annotations

from pipelines.araNya_tatra_bhava_AraRyaH import derive_AraRyaH, derive_AraRya_pratipadika


def test_AraRya_pratipadika():
    s = derive_AraRya_pratipadika()
    assert s.flat_slp1().strip() == "AraNya"


def test_AraRyaH_final():
    s = derive_AraRyaH()
    assert s.flat_slp1().strip() == "AraNyaH"


def test_trace_contains_key_steps():
    s = derive_AraRyaH()
    ids = [row.get("sutra_id") for row in s.trace]
    for need in ("2.3.36", "4.3.53", "7.2.117"):
        assert need in ids

