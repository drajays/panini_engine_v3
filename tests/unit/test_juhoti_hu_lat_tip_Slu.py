from __future__ import annotations


def test_P040_json_spine_and_surface_juhoti():
    import sutras  # noqa: F401

    from pipelines.juhoti_hu_lat_tip_Slu_P040_demo import derive_juhoti_hu_lat_tip_Slu_P040

    s = derive_juhoti_hu_lat_tip_Slu_P040()
    assert s.flat_slp1() == "juhoti"

    ids = [t["sutra_id"] for t in s.trace]
    assert ids.index("3.4.78") < ids.index("2.4.75")
    assert ids.index("2.4.75") < ids.index("1.1.60") < ids.index("1.1.61")
    assert ids.index("1.1.61") < ids.index("6.1.10")
    assert ids.index("6.1.10") < ids.index("7.4.62")
    assert ids.index("7.4.62") < ids.index("7.3.84")
    assert ids.index("7.3.84") < ids.index("1.1.62")
    assert s.samjna_registry.get("6.1.10_P040_slau_dvitva_done") is True

    # 7.4.59: *hrasva* vacuous on ``hu`` *abhyāsa* — expect a trace row, COND-FALSE.
    rows_7459 = [t for t in s.trace if t.get("sutra_id") == "7.4.59"]
    assert rows_7459
    assert rows_7459[-1].get("status") == "SKIPPED"
