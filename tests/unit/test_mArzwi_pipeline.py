from __future__ import annotations


def test_derive_mArzwi():
    from pipelines.mArzwi_lat_mFj import derive_mArzwi

    s = derive_mArzwi()
    assert s.render() == "mArzwi"

