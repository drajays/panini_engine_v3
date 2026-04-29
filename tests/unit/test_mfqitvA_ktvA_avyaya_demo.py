import sutras  # noqa: F401

from pipelines.mfqitvA_ktvA_avyaya_demo import derive_mfqitvA


def _fired(trace, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_mfqitvA_surface() -> None:
    s = derive_mfqitvA()
    assert s.flat_slp1() == "mfqitvA"


def test_mfqitvA_key_spine() -> None:
    s = derive_mfqitvA()
    for sid in ("7.2.35", "1.2.7", "1.1.40", "2.4.82"):
        assert _fired(s.trace, sid)

