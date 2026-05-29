from __future__ import annotations


def test_P037_AwIwat_surface_and_spine():
    import sutras  # noqa: F401

    from pipelines.AwIwat_luN_aT_Nic_caN_tip_P037_demo import (
        derive_AwIwat_luN_aT_Nic_caN_tip_P037,
    )

    s = derive_AwIwat_luN_aT_Nic_caN_tip_P037()
    assert s.flat_slp1() == "AwIwat"

    ids = [t["sutra_id"] for t in s.trace]

    assert ids.count("7.2.116") >= 1
    assert ids.index("3.1.48") < ids.index("3.4.77")
    assert ids.index("6.4.71") < ids.index("6.4.51")
    assert ids.index("6.1.11") < ids.index("7.4.93")
    assert ids.index("7.4.93") < ids.index("7.4.94") < ids.index("7.4.60")
    i760 = ids.index("7.4.60")
    later_6101 = [i for i, sid in enumerate(ids) if sid == "6.1.101" and i > i760]
    assert later_6101, "expected second 6.1.101 after abhyāsa trim (P037 cluster)"
