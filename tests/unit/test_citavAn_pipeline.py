from __future__ import annotations


def test_derive_citavAn():
    from pipelines.citavAn_prathamA_ciY import derive_citavAn

    s = derive_citavAn()
    assert s.render() == "citavAn"
