"""
pipelines/AdIDhyanam.py — आदीध्यनम् (*āṅ* + *dīdhīṅ* + *lyuṭ*, napuṃsaka 2-1).

Source: ``/Users/dr.ajayshukla/Documents/my panini notes/आदीध्यनम्.md``.

Target SLP1: **AdIDhyanam** (prathamā napuṃsaka of stem ``AdIDhyana``).
"""
from __future__ import annotations

import sutras  # noqa: F401

from phonology.varna import parse_slp1_upadesha_sequence
from engine.state import State, Term

from pipelines.krdanta import derive_krt
from pipelines.subanta import run_subanta_preflight_through_1_4_7, run_subanta_sup_attach_and_finish


def _A_upasarga() -> Term:
    return Term(
        kind="upasarga",
        # Use ``AN`` (no ``~``) so 1.3.3 marks final ``N`` as it; ``~`` would
        # nasalize the vowel and incorrectly make ``A`` itself it via 1.3.2.
        varnas=parse_slp1_upadesha_sequence("AN"),
        tags={"upadesha"},
        meta={"upadesha_slp1": "AN"},
    )


def derive_AdIDhyana_pratipadika() -> State:
    """``A`` + ``dIDhI`` + *lyuṭ* → ``AdIDhyana`` (merged prātipadika)."""
    s = derive_krt(
        "dIDhI~N",
        krt_upadesha_slp1="lyuw",
        merge_pratipadika_label="AdIDhyana",
        prefix_terms=[_A_upasarga()],
    )
    return s


def derive_AdIDhyanam() -> State:
    """Full pada: prātipadika + *subanta* (2-1 ekavacana napuṃsaka)."""
    s = derive_AdIDhyana_pratipadika()
    if s.terms:
        s.terms[0].tags.add("napuṃsaka")
    s.meta["linga"] = "napuṃsaka"
    s.meta["vibhakti_vacana"] = "2-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


__all__ = ["derive_AdIDhyana_pratipadika", "derive_AdIDhyanam"]
