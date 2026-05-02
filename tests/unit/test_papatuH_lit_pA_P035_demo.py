from __future__ import annotations

import sutras  # noqa: F401


def _fired(trace: list, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_papatuH_lit_pA_P035_surface() -> None:
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.papatuH_lit_pA_P035_demo import derive_papatuH_lit_pA_P035

    s = derive_papatuH_lit_pA_P035()
    assert s.flat_slp1() == "papatuH"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "पपतुः"


def test_papatuH_lit_pA_P035_spine() -> None:
    from pipelines.papatuH_lit_pA_P035_demo import derive_papatuH_lit_pA_P035

    s = derive_papatuH_lit_pA_P035()
    for sid in (
        "3.2.115",
        "3.4.82",
        "1.2.5",
        "6.4.64",
        "6.1.2",
        "7.4.59",
        "8.2.66",
        "8.3.15",
    ):
        assert _fired(s.trace, sid), f"missing trace for {sid}"
