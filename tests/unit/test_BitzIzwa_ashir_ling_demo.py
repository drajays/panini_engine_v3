import sutras  # noqa: F401

from pipelines.BitzIzwa_ashir_ling_demo import derive_BitzIzwa


def _fired(trace: list, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_BitzIzwa_surface() -> None:
    s = derive_BitzIzwa()
    assert s.flat_slp1() == "BitzIzwa"


def test_BitzIzwa_key_spine() -> None:
    s = derive_BitzIzwa()
    for sid in ("3.3.173", "3.4.78", "3.4.102", "3.4.107", "8.3.59", "8.4.55", "8.4.41"):
        assert _fired(s.trace, sid)

