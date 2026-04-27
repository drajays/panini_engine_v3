from __future__ import annotations


def test_derive_marImfjaH():
    from pipelines.marImfja_prathamA_mFjU import derive_marImfjaH

    s = derive_marImfjaH()
    assert s.render() == "marImfjaH"
