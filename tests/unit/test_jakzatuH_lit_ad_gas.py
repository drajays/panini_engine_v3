from __future__ import annotations

import sutras  # noqa: F401


def _fired(trace: list, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_jakzatuH_lit_ad_gas_P034_surface() -> None:
    from phonology.joiner import slp1_to_devanagari
    from engine.it_phonetic import term_phonetic_varnas

    from pipelines.jakzatuH_lit_ad_gas_P034_demo import derive_jakzatuH_lit_ad_gas_P034

    s = derive_jakzatuH_lit_ad_gas_P034()
    assert s.flat_slp1() == "jakzatuH"
    assert slp1_to_devanagari(term_phonetic_varnas(s.terms[0])) == "जक्षतुः"


def test_jakzatuH_lit_ad_gas_P034_spine() -> None:
    from pipelines.jakzatuH_lit_ad_gas_P034_demo import derive_jakzatuH_lit_ad_gas_P034

    s = derive_jakzatuH_lit_ad_gas_P034()
    for sid in (
        "2.4.40",
        "3.2.115",
        "3.4.82",
        "1.2.5",
        "6.4.100",
        "6.1.8",
        "7.4.60",
        "7.4.62",
        "7.4.59",
        "8.4.55",
        "8.2.66",
        "8.3.15",
    ):
        assert _fired(s.trace, sid), f"missing trace for {sid}"
