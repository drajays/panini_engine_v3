from __future__ import annotations


def test_derive_AdIDhyakaH():
    from pipelines.AdIDhyakaH import derive_AdIDhyaka_pratipadika, derive_AdIDhyakaH

    s0 = derive_AdIDhyaka_pratipadika()
    assert s0.flat_slp1() == "AdIDhyaka"

    s = derive_AdIDhyakaH()
    assert s.render() == "AdIDhyakaH"
