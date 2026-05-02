from __future__ import annotations


def test_P025_paTayati_surface_and_spine_order():
    import sutras  # noqa: F401

    from pipelines.paTayati_paTu_Nic_P025_demo import derive_paTayati_paTu_Nic_P025

    s = derive_paTayati_paTu_Nic_P025()
    assert s.flat_slp1() == "paTayati"

    ids = [t["sutra_id"] for t in s.trace]
    assert ids.index("2.1.26") < ids.index("3.1.32")
    assert ids.index("6.4.155") < ids.index("1.1.57")
    assert ids.index("1.1.57") < ids.index("7.2.116")
    assert ids.index("3.1.68") < ids.index("7.3.84") < ids.index("6.1.78")


def test_P025_7_2_116_does_not_mutate():
    import sutras  # noqa: F401

    from pipelines.paTayati_paTu_Nic_P025_demo import derive_paTayati_paTu_Nic_P025

    s = derive_paTayati_paTu_Nic_P025()
    row = next((t for t in s.trace if t.get("sutra_id") == "7.2.116"), None)
    assert row is not None
    assert row.get("status") in {"SKIPPED", "BLOCKED"}
