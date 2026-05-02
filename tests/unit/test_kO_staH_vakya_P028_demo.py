from __future__ import annotations


def test_derive_kO_staH_vakya_P028():
    from pipelines.kO_staH_vakya_P028_demo import derive_kO_staH_vakya_P028

    out = derive_kO_staH_vakya_P028()
    assert out == "kO staH"

