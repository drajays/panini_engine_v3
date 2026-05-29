from __future__ import annotations

import sutras  # noqa: F401

from pipelines.katarakatamA_vibhASa_jasi_demo import derive_katarakatame


def _ap(s, sid: str) -> bool:
    return any(e.get("sutra_id") == sid and e.get("status") == "APPLIED" for e in s.trace)


def _sk(s, sid: str) -> bool:
    return any(e.get("sutra_id") == sid and e.get("status") == "SKIPPED" for e in s.trace)


def test_vibhASa_jasi_accept_branch_katarakatame() -> None:
    s = derive_katarakatame(vibhasha_choice=True)
    assert s.flat_slp1() == "katarakatame"
    assert _ap(s, "1.1.31")
    assert _ap(s, "1.1.32")
    assert _ap(s, "7.1.17")


def test_vibhASa_jasi_decline_branch_katarakatamAH() -> None:
    s = derive_katarakatame(vibhasha_choice=False)
    assert s.flat_slp1() == "katarakatamAH"
    assert _ap(s, "1.1.31")
    # VIBHASHA declined → may trace as SKIPPED (vibhasha gate) or COND-FALSE,
    # but in any case it must not be APPLIED.
    assert not _ap(s, "1.1.32")
    # jas→śī must not run without sarvanāma
    assert _sk(s, "7.1.17")

