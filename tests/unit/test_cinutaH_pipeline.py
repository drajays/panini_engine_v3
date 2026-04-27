from __future__ import annotations


def test_cinutaH_render():
    from pipelines.cinutaH_dvivacana_lat_ciY import derive_cinutaH

    s = derive_cinutaH()
    assert s.render() == "cinutaH"
    assert "चिनुतः" in s.flat_dev()


def test_sutra_3_1_73_registry():
    from engine import SUTRA_REGISTRY

    assert "3.1.73" in SUTRA_REGISTRY
    assert SUTRA_REGISTRY["3.1.73"].sutra_id == "3.1.73"
