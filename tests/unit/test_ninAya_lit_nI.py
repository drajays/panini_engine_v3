from __future__ import annotations

import sutras  # noqa: F401


def _fired(trace: list, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_ninAya_lit_nI_P036_surface() -> None:
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.ninAya_lit_nI_P036_demo import derive_ninAya_lit_nI_P036

    s = derive_ninAya_lit_nI_P036()
    assert s.flat_slp1() == "ninAya"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "निनाय"


def test_ninAya_lit_nI_P036_spine() -> None:
    from pipelines.ninAya_lit_nI_P036_demo import derive_ninAya_lit_nI_P036

    s = derive_ninAya_lit_nI_P036()
    for sid in (
        "3.2.115",
        "3.4.82",
        "7.3.84",
        "6.1.78",
        "8.4.41",
        "6.1.8",
        "7.4.59",
        "6.1.101",
    ):
        assert _fired(s.trace, sid), f"missing trace for {sid}"
