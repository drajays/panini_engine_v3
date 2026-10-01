from __future__ import annotations


def test_derive_AdIDhyanam():
    from pipelines.AdIDhyanam import derive_AdIDhyanam, derive_AdIDhyana_pratipadika

    s0 = derive_AdIDhyana_pratipadika()
    assert s0.flat_slp1() == "AdIDyana"

    s = derive_AdIDhyanam()
    assert s.flat_dev() in ("आदीध्यकः", "आदीध्यनम्")
    assert s.render() == "AdIDyanam"
