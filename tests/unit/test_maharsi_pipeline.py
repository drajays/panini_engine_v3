from __future__ import annotations


def test_derive_maharziH():
    from pipelines.maharsi_mahAt_fzi import derive_maharziH

    s = derive_maharziH()
    assert s.render() == "maharziH"

