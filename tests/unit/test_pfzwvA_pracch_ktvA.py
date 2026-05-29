import sutras  # noqa: F401

from pipelines.pfzwvA_pracch_ktvA_demo import derive_pfzwvA


def _fired(trace, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_pfzwvA_surface() -> None:
    s = derive_pfzwvA()
    assert s.flat_slp1() == "pfzwvA"


def test_pfzwvA_key_spine() -> None:
    s = derive_pfzwvA()
    for sid in ("1.2.8", "1.1.45", "6.1.108", "6.4.19", "8.2.36", "8.4.41", "1.1.40", "2.4.82"):
        assert _fired(s.trace, sid)

