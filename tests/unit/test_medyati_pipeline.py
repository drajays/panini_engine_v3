from __future__ import annotations


def test_derive_medyati():
    from pipelines.medyati_lat_mid import derive_medyati

    s = derive_medyati()
    assert s.render() == "medyati"

