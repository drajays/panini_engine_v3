from __future__ import annotations


def test_P039_json_spine_and_surface_viSAKaH():
    import sutras  # noqa: F401

    from pipelines.viSAKaH_taddhita_luk_aR_paribhasha_P039_demo import (
        derive_viSAKaH_taddhita_luk_aR_P039,
    )

    s = derive_viSAKaH_taddhita_luk_aR_P039()
    assert s.flat_slp1() == "viSAKaH"

    ids = [t["sutra_id"] for t in s.trace]

    assert ids.index("4.1.76") < ids.index("4.3.25") < ids.index("4.3.34")
    assert ids.index("4.3.34") < ids.index("1.1.60") < ids.index("1.1.61")
    assert ids.index("1.1.61") < ids.index("4.1.2") < ids.index("6.1.68")
    assert ids.index("6.1.68") < ids.index("8.2.1") < ids.index("8.2.66") < ids.index("8.3.15")
    assert s.samjna_registry.get("6.1.68_tApanta_sup_lopa_P039") is True
    assert s.samjna_registry.get("P039_4_3_34_aR_luk_structural") is True
