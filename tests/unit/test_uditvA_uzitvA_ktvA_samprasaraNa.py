import sutras  # noqa: F401

from pipelines.uditvA_uzitvA_ktvA_samprasaraNa_demo import derive_uditvA, derive_uzitvA


def _fired(trace, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_uditvA_surface_and_spine() -> None:
    s = derive_uditvA()
    assert s.flat_slp1() == "uditvA"
    for sid in ("1.1.45", "6.1.108", "1.1.40", "2.4.82"):
        assert _fired(s.trace, sid)


def test_uzitvA_surface_and_spine() -> None:
    s = derive_uzitvA()
    assert s.flat_slp1() == "uzitvA"
    for sid in ("1.1.45", "6.1.108", "8.3.60", "1.1.40", "2.4.82"):
        assert _fired(s.trace, sid)

