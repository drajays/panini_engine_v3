from __future__ import annotations


def test_derive_jizRuH():
    from pipelines.jiRNu_prathamA_ji import derive_jizRuH

    s = derive_jizRuH()
    assert s.render() == "jizRuH"
