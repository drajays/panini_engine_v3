from __future__ import annotations


def test_derive_popuvaH():
    from pipelines.popuv_yang_pUY import derive_popuvaH

    s = derive_popuvaH()
    assert s.render() == "popuvaH"
