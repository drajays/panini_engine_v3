from __future__ import annotations

import sutras  # noqa: F401

from phonology.joiner import slp1_to_devanagari
from pipelines.krdanta import derive_krt, derive_nAyakaH


def test_nayaka_pratipadika_flat():
    state = derive_krt("RIY", krt_upadesha_slp1="Nvul", merge_pratipadika_label="nAyaka")
    assert state.flat_slp1() == "nAyaka"


def test_nayaka_md_key_sutras_in_trace():
    state = derive_krt("RIY", krt_upadesha_slp1="Nvul", merge_pratipadika_label="nAyaka")
    path = [e.get("sutra_id") for e in state.trace if isinstance(e, dict)]
    for sid in ("6.1.65", "7.2.115", "6.1.78", "1.2.46", "__KRD_MERGE__"):
        assert sid in path, f"missing {sid!r} in {path}"


def test_nayakaH_surface():
    state = derive_nAyakaH()
    assert state.terms
    produced = slp1_to_devanagari(state.terms[0].varnas)
    assert produced == "नायकः"
