from __future__ import annotations


def test_derive_citaH():
    from pipelines.citaH_prathamA_ciY import derive_citaH

    s = derive_citaH()
    assert s.render() == "citaH"
