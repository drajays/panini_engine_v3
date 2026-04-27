from __future__ import annotations


def test_derive_alAvIt():
    from pipelines.alAvIt_luN_lUY import derive_alAvIt

    s = derive_alAvIt()
    assert s.render() == "alAvIt"

