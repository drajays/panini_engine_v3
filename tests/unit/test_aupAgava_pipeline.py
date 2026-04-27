from __future__ import annotations

from pipelines.aupagu_apatya_aupAgava import derive_aupAgavaH


def test_aupAgavaH_pipeline_final_form():
    s = derive_aupAgavaH()
    # Engine render() is SLP1; visarga is "H".
    assert s.render().endswith("H")
    # SLP1 surface (flat) should match the intended stem+visarga.
    assert s.flat_slp1().strip() == "OpagavaH"


def test_trace_includes_key_sutras():
    s = derive_aupAgavaH()
    ids = [row.get("sutra_id") for row in s.trace]
    assert "1.1.21" in ids
    assert "2.3.50" in ids
    assert "3.1.3" in ids
    assert "7.2.117" in ids

