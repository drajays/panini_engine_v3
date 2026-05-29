import sutras  # noqa: F401

from pipelines.vibhidatuH_lit_demo import derive_vibhidatuH


def _fired(trace, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_vibhidatuH_surface() -> None:
    s = derive_vibhidatuH()
    # liṭ (perfect) includes reduplication: vi + bi + bhid + atus → vibibhidatuH
    assert s.flat_slp1() == "vibiBidatuH"


def test_vibhidatuH_key_spine() -> None:
    s = derive_vibhidatuH()
    for sid in ("3.2.115", "3.4.82", "1.2.5", "6.1.8", "7.4.60", "8.4.54", "8.2.66", "8.3.15"):
        assert _fired(s.trace, sid)

