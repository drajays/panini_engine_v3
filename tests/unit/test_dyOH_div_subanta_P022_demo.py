from __future__ import annotations


def test_P022_json_spine_order_and_surface_dyOH():
    import sutras  # noqa: F401

    from pipelines.dyOH_div_subanta_P022_demo import derive_dyOH_div_subanta_P022

    s = derive_dyOH_div_subanta_P022()
    assert s.flat_slp1() == "dyOH"

    ids = [t["sutra_id"] for t in s.trace]

    # Core JSON spine should appear in order.
    i_412 = ids.index("4.1.2")
    i_1143 = ids.index("1.1.43")
    i_7184 = ids.index("7.1.84")
    i_821 = ids.index("8.2.1")
    i_8223 = ids.index("8.2.23")
    i_8266 = ids.index("8.2.66")
    i_8315 = ids.index("8.3.15")

    assert i_412 < i_1143 < i_7184 < i_821 < i_8223 < i_8266 < i_8315

