from __future__ import annotations


def test_P042_json_spine_and_surface_gArgyAH():
    import sutras  # noqa: F401

    from pipelines.gArgyAH_garga_yaY_luk_P042_demo import derive_gArgyAH_garga_yaY_luk_P042

    s = derive_gArgyAH_garga_yaY_luk_P042()
    assert s.flat_slp1() == "gArgyAH"

    ids = [t["sutra_id"] for t in s.trace]
    assert ids.index("4.1.105") < ids.index("1.3.9")
    assert ids.index("7.2.117") < ids.index("4.1.2")
    assert ids.index("4.1.2") < ids.index("4.1.162") < ids.index("2.4.64")
    assert ids.index("2.4.64") < ids.index("1.1.60") < ids.index("1.1.61")
    assert ids.index("1.1.61") < ids.index("1.1.62") < ids.index("1.1.63")
    assert ids.index("1.1.63") < ids.index("7.1.9") < ids.index("6.1.101")
    assert ids.index("6.1.101") < ids.index("8.2.1") < ids.index("8.2.66") < ids.index("8.3.15")
    assert ids.index("8.3.15") < ids.index("8.2.30")

    assert s.samjna_registry.get("4.1.162_gotra_P042") is True
    assert s.samjna_registry.get("2.4.64_P042_yanna_luk_audit") is True

    rows_8230 = [t for t in s.trace if t.get("sutra_id") == "8.2.30"]
    assert rows_8230
    assert rows_8230[-1].get("status") == "SKIPPED"
