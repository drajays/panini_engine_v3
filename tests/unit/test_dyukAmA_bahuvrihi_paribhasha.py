from __future__ import annotations


def test_P023_json_spine_and_surface_dyukAmA():
    import sutras  # noqa: F401

    from pipelines.dyukAmA_bahuvrihi_paribhasha_P023_demo import derive_dyukAmA_bahuvrihi_P023

    s = derive_dyukAmA_bahuvrihi_P023()
    assert s.flat_slp1() == "dyukAmA"

    ids = [t["sutra_id"] for t in s.trace]

    # Key ordering checks (allow structural __MERGE__ in between).
    assert ids.index("6.1.127") < ids.index("6.1.77")
    assert ids.index("4.1.4") < ids.index("4.1.2") < ids.index("6.1.68")
    assert "2.2.14" in ids

