from __future__ import annotations


def test_P041_json_spine_and_surface_agnicit():
    import sutras  # noqa: F401

    from pipelines.agnicit_agni_ci_kvip_P041_demo import derive_agnicit_agni_ci_kvip_P041

    s = derive_agnicit_agni_ci_kvip_P041()
    assert s.flat_slp1() == "agnicit"

    ids = [t["sutra_id"] for t in s.trace]
    assert ids.index("3.2.76") < ids.index("3.2.91")
    assert ids.index("3.2.91") < ids.index("1.3.3")
    assert ids.index("1.3.10") < ids.index("6.1.67") < ids.index("1.1.60")
    assert ids.index("1.1.60") < ids.index("1.1.61") < ids.index("1.1.62")
    assert ids.index("1.1.5") < ids.index("7.3.86")
    assert ids.index("1.1.46") < ids.index("6.1.71")
    assert ids.index("6.1.71") < ids.index("4.1.2") < ids.index("6.1.68")
    assert ids.index("6.1.68") < ids.index("8.2.1") < ids.index("8.2.30")

    assert s.samjna_registry.get("3.2.91_agnau_ce_P041") is True
    assert s.samjna_registry.get("1.1.5_kngiti") is True
    assert s.samjna_registry.get("6.1.68_hal_sup_lopa_P041") is True

    rows_7386 = [t for t in s.trace if t.get("sutra_id") == "7.3.86"]
    assert rows_7386
    assert rows_7386[-1].get("status") == "SKIPPED"

    rows_8230 = [t for t in s.trace if t.get("sutra_id") == "8.2.30"]
    assert rows_8230
    assert rows_8230[-1].get("status") == "SKIPPED"
