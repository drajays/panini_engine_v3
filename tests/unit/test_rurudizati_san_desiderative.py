import sutras  # noqa: F401

from pipelines.rurudizati_san_desiderative_demo import derive_rurudizati


def _fired(trace, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_rurudizati_surface() -> None:
    s = derive_rurudizati()
    assert s.flat_slp1() == "rurudizati"


def test_rurudizati_key_spine() -> None:
    s = derive_rurudizati()
    for sid in ("3.1.7", "1.2.8", "3.1.32", "6.1.1", "7.4.60", "3.2.123", "3.1.68", "8.3.59"):
        assert _fired(s.trace, sid)

