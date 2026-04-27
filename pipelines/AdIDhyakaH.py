"""
pipelines/AdIDhyakaH.py — आदीध्यकः (*āṅ* + *dīdhīṅ* + *ṇvul*, puṃ prathamā).

Source: ``/Users/dr.ajayshukla/Documents/my panini notes/आदीध्यकः.md``.

Target SLP1: **AdIDhyakaH** (visarga).
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


def derive_AdIDhyaka_pratipadika() -> State:
    """``A`` + ``dIDhI`` + *ṇvul* → ``AdIDhyaka`` (``6.1.77`` *ī*+*a* → *y*)."""
    return derive_krt(
        "dIDhI~N",
        krt_upadesha_slp1="Nvul",
        merge_pratipadika_label="AdIDhyaka",
        prefix_terms=[_A_upasarga()],
        dhatu_meta={"dIdhIvevI_guna_vrddhi_nishedha": True},
        extra_state_meta={"6_1_77_after_krt_arm": True},
    )


def derive_AdIDhyakaH() -> State:
    """Puṃliṅga prathamā ekavacana (``su`` → ``H``)."""
    s = derive_AdIDhyaka_pratipadika()
    stem = s.flat_slp1()
    s2 = build_initial_state(stem, vibhakti=1, vacana=1, linga="pulliṅga")
    return run_subanta_pipeline(s2)


__all__ = ["derive_AdIDhyaka_pratipadika", "derive_AdIDhyakaH"]
