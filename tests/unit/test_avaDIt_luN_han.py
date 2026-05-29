from __future__ import annotations


def test_avaDIt_flat_and_key_trace_order():
    from pipelines.avaDIt_luN_han_P026_demo import derive_avaDIt

    s = derive_avaDIt()
    assert s.flat_slp1() == "avaDIt"

    ids = [e.get("sutra_id") for e in s.trace if e.get("sutra_id") not in ("__MERGE__",)]
    assert ids.index("2.4.43") < ids.index("6.4.71")
    assert ids.index("6.4.71") < ids.index("3.4.78")
    assert ids.index("3.4.114") < ids.index("7.2.35")
    assert ids.index("7.2.35") < ids.index("6.4.48")
    assert ids.index("6.4.48") < ids.index("1.1.56")
    assert ids.index("1.1.56") < ids.index("7.2.7")
    assert ids.count("7.2.7") >= 2
    assert ids.index("6.4.114") < ids.index("8.2.1")

    st7 = [e.get("status") for e in s.trace if e.get("sutra_id") == "7.2.7"]
    assert "SKIPPED" in st7 and "APPLIED" in st7

    st614 = [e.get("status") for e in s.trace if e.get("sutra_id") == "6.4.114"]
    assert "APPLIED" in st614
