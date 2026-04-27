from __future__ import annotations


def test_derive_loluvH():
    from pipelines.loluv_yang_lUY import derive_loluvH

    s = derive_loluvH()
    assert s.render() == "loluvaH"

