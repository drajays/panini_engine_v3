import sutras  # noqa: F401

from pipelines.IDe_lit_indh_demo import derive_IDe


def _fired(trace, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and (e.get("status") or "").upper() in {"APPLIED", "AUDIT"}
        for e in trace
    )


def test_IDe_surface() -> None:
    s = derive_IDe()
    assert s.flat_slp1() == "IDe"


def test_IDe_key_spine() -> None:
    s = derive_IDe()
    for sid in ("3.2.115", "3.4.81", "1.1.55", "1.2.6", "6.4.24", "6.1.8", "6.1.101"):
        assert _fired(s.trace, sid)

