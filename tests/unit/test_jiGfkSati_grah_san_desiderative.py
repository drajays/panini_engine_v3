import sutras  # noqa: F401

from pipelines.jiGfkSati_grah_san_desiderative_demo import derive_jiGfkSati


def _fired(trace, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_jiGfkSati_surface() -> None:
    s = derive_jiGfkSati()
    assert s.flat_slp1() == "jiGfkSati"


def test_jiGfkSati_key_spine() -> None:
    s = derive_jiGfkSati()
    for sid in ("3.1.7", "1.2.8", "1.1.45", "6.1.108", "6.1.1", "7.4.60", "7.4.62", "7.4.79", "8.2.31", "8.2.41", "8.3.46", "3.2.123"):
        assert _fired(s.trace, sid)

