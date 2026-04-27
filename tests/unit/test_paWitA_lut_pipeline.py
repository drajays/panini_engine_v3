from __future__ import annotations


def test_derive_paWitA():
    from pipelines.paWitA_lut_prathamA import derive_paWitA

    s = derive_paWitA()
    assert s.flat_slp1() == "paWitA"
    assert s.render() == "paWitA"
