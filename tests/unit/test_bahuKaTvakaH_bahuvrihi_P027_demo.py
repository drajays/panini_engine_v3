from __future__ import annotations


def test_derive_bahuKaTvakaH_bahuvrihi_P027():
    from pipelines.bahuKaTvakaH_bahuvrihi_P027_demo import derive_bahuKaTvakaH_bahuvrihi_P027

    s = derive_bahuKaTvakaH_bahuvrihi_P027()
    assert s.render() == "bahuKaTvakaH"

    ids = [e.get("sutra_id") for e in s.trace]
    assert ids.index("2.2.24") < ids.index("5.4.154") < ids.index("7.4.15")
    assert "8.2.66" in ids and "8.3.15" in ids

