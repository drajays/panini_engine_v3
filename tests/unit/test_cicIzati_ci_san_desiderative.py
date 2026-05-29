import sutras  # noqa: F401

from pipelines.cicIzati_ci_san_desiderative_demo import derive_cicIzati


def _fired(trace: list, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_cicIzati_surface() -> None:
    s = derive_cicIzati()
    assert s.flat_slp1() == "cicIzati"


def test_cicIzati_key_spine() -> None:
    s = derive_cicIzati()
    for sid in ("3.1.7", "1.2.8", "3.1.32", "6.1.1", "6.4.16", "3.2.123", "3.1.68", "8.3.59"):
        assert _fired(s.trace, sid)
