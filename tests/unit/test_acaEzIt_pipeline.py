from __future__ import annotations

from pipelines.acaEzIt_luN_ciY import derive_acaEzIt


def test_acaEzIt_final_form():
    s = derive_acaEzIt()
    assert s.flat_slp1().strip() == "acEzIt"


def test_trace_contains_key_sutras():
    s = derive_acaEzIt()
    ids = [r.get("sutra_id") for r in s.trace]
    for need in ("3.2.110", "3.1.43", "3.1.44", "7.2.1", "8.3.59"):
        assert need in ids

