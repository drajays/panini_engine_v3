"""
pipelines/AdIDhyakaH.py — आदीध्यकः (*āṅ* + *dīdhīṅ* + *ṇvul*, puṃ prathamā).

Source: ``/Users/dr.ajayshukla/Documents/my panini notes/आदीध्यकः.md``.

Target SLP1: **AdIDhyakaH** (visarga).
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


def derive_AdIDhyaka_pratipadika() -> State:
    """``A`` + ``dIDhI`` + *ṇvul* → ``AdIDhyaka`` (``6.1.77`` *ī*+*a* → *y*)."""
    return derive_krt(
        "dIDhI~N",
        krt_upadesha_slp1="Nvul",
        merge_pratipadika_label="AdIDhyaka",
        prefix_terms=[_A_upasarga()],
    )


def derive_AdIDhyakaH() -> State:
    """Puṃliṅga prathamā ekavacana (``su`` → ``H``)."""
    s = derive_AdIDhyaka_pratipadika()
    # Continue on the same State to preserve prakriyā trace.
    if s.terms:
        s.terms[0].tags.add("pulliṅga")
    s.meta["linga"] = "pulliṅga"
    s.meta["vibhakti_vacana"] = "1-1"
    s = run_subanta_preflight_through_1_4_7(s)
    s = run_subanta_sup_attach_and_finish(s)
    return s


__all__ = ["derive_AdIDhyaka_pratipadika", "derive_AdIDhyakaH"]
