from __future__ import annotations


def test_stutavAn():
    from pipelines.stutavAn_prathamA_stuY import derive_stutavAn

    assert derive_stutavAn().render() == "stutavAn"


def test_kRtavAn():
    from pipelines.kRtavAn_prathamA_kf import derive_kRtavAn

    # Short ṛ ``f`` in SLP1 tape (``kf`` row); *kit* blocks **7.3.84** *guṇa*.
    assert derive_kRtavAn().render() == "kftavAn"


def test_bhinnavAn():
    from pipelines.bhinnavAn_prathamA_Bidi import derive_bhinnavAn

    s = derive_bhinnavAn()
    assert s.render() == "BinnavAn"
    assert "भिन्नवान्" in s.flat_dev()


def test_mRuSTavAn():
    from pipelines.mRuSTavAn_prathamA_mfzu import derive_mRuSTavAn

    s = derive_mRuSTavAn()
    assert s.render() == "mfzwavAn"
    assert "मृष्टवान्" in s.flat_dev()
