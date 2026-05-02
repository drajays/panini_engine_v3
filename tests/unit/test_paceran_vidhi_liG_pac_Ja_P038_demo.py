from __future__ import annotations


def test_P038_paceran_surface_and_spine():
    import sutras  # noqa: F401

    from pipelines.paceran_vidhi_liG_pac_Ja_P038_demo import (
        derive_paceran_vidhi_liG_pac_Ja_P038,
    )

    s = derive_paceran_vidhi_liG_pac_Ja_P038()
    assert s.flat_slp1() == "paceran"

    ids = [t["sutra_id"] for t in s.trace]

    assert ids.index("3.3.161") < ids.index("3.4.102")
    assert ids.index("3.4.102") < ids.index("3.4.78")
    assert ids.index("3.4.78") < ids.index("3.4.105")
    assert ids.index("3.4.105") < ids.index("7.2.79")
    assert ids.index("7.2.79") < ids.index("6.4.105") < ids.index("6.1.70")
    assert ids.index("6.1.70") < ids.index("3.1.68")
    assert ids.index("3.1.68") < ids.index("6.1.87")
