from __future__ import annotations


def test_P021_vakya_visarga_t_sandhi_trace_and_surface():
    import sutras  # noqa: F401

    from pipelines.grAmas_tava_svam_vakya_P021_demo import derive_grAmas_tava_svam_vakya_P021

    s = derive_grAmas_tava_svam_vakya_P021()

    # flat_slp1 concatenates terms (no spaces).
    assert s.flat_slp1() == "grAmastavasvam"

    ids = [t["sutra_id"] for t in s.trace]
    assert ids[:3] == ["1.1.50", "8.2.1", "8.3.34"]

