from __future__ import annotations

import sutras  # noqa: F401

from pipelines.pUrvaparANAm_dvandva_demo import derive_pUrvaparANAm


def _ap(s, sid: str) -> bool:
    return any(e.get("sutra_id") == sid and e.get("status") == "APPLIED" for e in s.trace)

def _fired(s, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and e.get("status") in {"APPLIED", "AUDIT"}
        for e in s.trace
    )


def _sk(s, sid: str) -> bool:
    return any(e.get("sutra_id") == sid and e.get("status") == "SKIPPED" for e in s.trace)


def test_pUrvaparANAm_surface_and_key_steps() -> None:
    s = derive_pUrvaparANAm()
    assert s.flat_slp1() == "pUrvaparARAm"
    assert _ap(s, "1.1.27")
    assert _ap(s, "2.4.71")
    assert _ap(s, "__DVANDVA_MERGE__")
    assert _ap(s, "1.1.31")
    # suṭ blocked, nuṭ applies
    assert _sk(s, "7.1.52")
    assert _ap(s, "7.1.54")
    # nāmi + ṇatva
    assert _ap(s, "6.4.3")
    assert _fired(s, "8.2.1")
    assert _ap(s, "8.4.2")

