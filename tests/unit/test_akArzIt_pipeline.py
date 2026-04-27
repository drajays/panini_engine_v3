from __future__ import annotations


def test_derive_akArzIt():
    from pipelines.akArzIt_luN_dukrY import derive_akArzIt

    s = derive_akArzIt()
    assert s.render() == "akArzIt"

