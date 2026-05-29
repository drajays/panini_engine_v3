from __future__ import annotations


def test_P024_surface_and_key_spine_order():
    import sutras  # noqa: F401

    from pipelines.mahoraskena_bahuvrihi_P024_demo import derive_mahoraskena_bahuvrihi_P024

    s = derive_mahoraskena_bahuvrihi_P024()
    assert s.flat_slp1() == "mahoraskena"

    ids = [t["sutra_id"] for t in s.trace]
    assert ids.index("2.2.24") < ids.index("5.4.151") < ids.index("1.2.46")
    assert ids.index("1.2.46") < ids.index("6.3.46") < ids.index("6.1.101")
    assert ids.index("6.1.101") < ids.index("6.1.87")
    assert "7.1.12" in ids
    assert ids.index("6.1.87") < ids.index("7.1.12")
