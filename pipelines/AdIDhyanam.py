"""
pipelines/AdIDhyanam.py — आदीध्यनम् (*āṅ* + *dīdhīṅ* + *lyuṭ*, napuṃsaka 2-1).

Source: ``/Users/dr.ajayshukla/Documents/my panini notes/आदीध्यनम्.md``.

Target SLP1: **AdIDhyanam** (prathamā napuṃsaka of stem ``AdIDhyana``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from phonology import mk
from engine.state import State, Term

from pipelines.krdanta import derive_krt
from pipelines.subanta import build_initial_state, run_subanta_pipeline


def _A_upasarga() -> Term:
    return Term(
        kind="prakriti",
        varnas=[mk("A")],
        tags={"upasarga", "anga"},
        meta={},
    )


def derive_AdIDhyana_pratipadika() -> State:
    """``A`` + ``dIDhI`` + *lyuṭ* → ``AdIDhyana`` (merged prātipadika)."""
    s = derive_krt(
        "dIDhI~N",
        krt_upadesha_slp1="lyuw",
        merge_pratipadika_label="AdIDhyana",
        prefix_terms=[_A_upasarga()],
        dhatu_meta={"dIdhIvevI_guna_vrddhi_nishedha": True},
    )
    return s


def derive_AdIDhyanam() -> State:
    """Full pada: prātipadika + *subanta* (2-1 ekavacana napuṃsaka)."""
    s = derive_AdIDhyana_pratipadika()
    stem = s.flat_slp1()
    s2 = build_initial_state(stem, vibhakti=2, vacana=1, linga="napuṃsaka")
    return run_subanta_pipeline(s2)


__all__ = ["derive_AdIDhyana_pratipadika", "derive_AdIDhyanam"]
