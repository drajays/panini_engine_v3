from __future__ import annotations


def test_cinvanti():
    from pipelines.cinvanti_lat_ciY import derive_cinvanti

    s = derive_cinvanti()
    assert s.render() == "cinvanti"
    assert "चिन्वन्ति" in s.flat_dev()


def test_sutra_7_1_3_registry():
    from engine import SUTRA_REGISTRY

    assert "7.1.3" in SUTRA_REGISTRY
